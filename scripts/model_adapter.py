import os
import json
import time
import random
from types import SimpleNamespace
from datetime import datetime
from typing import Optional

try:
    from .summary_model import SummaryOutput
except ImportError:
    from summary_model import SummaryOutput


class TransientAPIError(RuntimeError):
    """Raised when provider failures are transient and should be retried later."""


class ModelAdapter:
    """Adapter that exposes a stable generate_summary(prompt, url) API.

    Behavior:
    - If GITHUB_TOKEN is present, will attempt to call GitHub Models (placeholder).
    - Otherwise, if GEMINI_API_KEY is present, uses the installed google-genai client.
    """

    def __init__(self, github_token: Optional[str] = None, gemini_key: Optional[str] = None):
        self.github_token = github_token or os.environ.get('GITHUB_TOKEN')
        self.gemini_key = gemini_key or os.environ.get('GEMINI_API_KEY')

    @staticmethod
    def _is_gemini_transient_error(error: Exception) -> bool:
        message = str(error).lower()
        transient_tokens = [
            'resource_exhausted',
            'quota',
            '429',
            '500',
            '502',
            '503',
            '504',
            'unavailable',
            'deadline exceeded',
            'timeout',
            'temporarily',
        ]
        return any(token in message for token in transient_tokens)

    def generate_summary(self, prompt: str, url: str) -> Optional[SummaryOutput]:
        if self.github_token:
            return self._call_github_models(prompt, url)
        if self.gemini_key:
            return self._call_gemini_api(prompt, url, self.gemini_key)
        raise RuntimeError('No model credentials found: set GITHUB_TOKEN or GEMINI_API_KEY')

    def _call_gemini_api(self, prompt: str, url: str, api_key: str) -> Optional[SummaryOutput]:
        try:
            # Local import to avoid requiring google-genai when using GitHub adapter
            from google import genai
            from google.genai import types
        except Exception as e:
            print('google-genai client not available or failed to import:', e)
            return None

        client = genai.Client(api_key=api_key)
        model = "gemini-3.1-pro-preview"
        tools = [
            types.Tool(url_context=types.UrlContext()),
            types.Tool(googleSearch=types.GoogleSearch()),
        ]
        generate_content_config = types.GenerateContentConfig(
            tools=tools,
        )

        contents = [
            types.Content(role="user", parts=[types.Part.from_text(text=prompt)])
        ]

        retry_attempts = max(1, int(os.environ.get('GEMINI_RETRY_ATTEMPTS', '4')))
        retry_base_delay = max(0.0, float(os.environ.get('GEMINI_RETRY_BASE_DELAY_SEC', '1.5')))
        retry_max_delay = max(retry_base_delay, float(os.environ.get('GEMINI_RETRY_MAX_DELAY_SEC', '20')))

        response_text = []
        saw_transient_error = False
        last_error = None
        for attempt in range(1, retry_attempts + 1):
            try:
                response_text = []
                for chunk in client.models.generate_content_stream(
                    model=model,
                    contents=contents,
                    config=generate_content_config,
                ):
                    if text := getattr(chunk, 'text', None):
                        response_text.append(text)
                break
            except Exception as e:
                last_error = e
                if self._is_gemini_transient_error(e):
                    saw_transient_error = True
                    print(f'Gemini transient error (attempt {attempt}/{retry_attempts}): {e}')
                    if attempt >= retry_attempts:
                        break
                    delay = min(retry_max_delay, retry_base_delay * (2 ** (attempt - 1)) + random.uniform(0.0, 0.5))
                    print(f'Retrying after {delay:.2f}s...')
                    time.sleep(delay)
                    continue

                print(f'Gemini non-retryable error: {e}')
                raise

        if not response_text and last_error is not None and saw_transient_error:
            raise TransientAPIError('Gemini transient failure (429/5xx/quota/transport). Retry later.')
        if not response_text and last_error is not None and not saw_transient_error:
            raise last_error

        response = SimpleNamespace(text="".join(response_text))

        # Attempt to parse JSON from response similar to previous logic
        try:
            json_str = response.text.strip()
            if '```json' in json_str:
                start = json_str.find('```json') + 7
                end = json_str.find('```', start)
                if end == -1:
                    json_str = json_str[start:]
                else:
                    json_str = json_str[start:end]
            elif '{' in json_str:
                start = json_str.find('{')
                end = json_str.rfind('}') + 1
                json_str = json_str[start:end]

            json_str = json_str.strip()
            if not json_str:
                raise ValueError('Empty JSON string from model')

            data = json.loads(json_str)
            data.setdefault('author', 'Unknown')
            if not data.get('date'):
                data['date'] = datetime.now().strftime('%d-%m-%Y')
            if 'category' in data:
                data['category'] = data['category'].replace(' ', '-')
            if 'filename' in data and not data['filename'].endswith('.md'):
                data['filename'] = data['filename'].strip().replace(' ', '-').lower()
                if not data['filename'].endswith('.md'):
                    data['filename'] += '.md'

            return SummaryOutput(**data)
        except Exception as e:
            print('Error parsing Gemini response:', e)
            print('Raw response snippet:', (response.text or '')[:1000])
            return None

    def _call_github_models(self, prompt: str, url: str) -> Optional[SummaryOutput]:
        try:
            import requests
        except Exception as e:
            print('requests library not available:', e)
            return None

        token = self.github_token
        if not token:
            raise RuntimeError('GITHUB_TOKEN not found in environment or adapter')

        model = os.environ.get('GITHUB_MODEL', 'openai/gpt-4.1-mini')
        endpoint_override = os.environ.get('GITHUB_MODELS_ENDPOINT')
        if endpoint_override:
            endpoints = [endpoint_override]
        else:
            endpoints = [
                'https://models.github.ai/inference/chat/completions',
                'https://api.github.com/inference/chat/completions',
            ]

        headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github+json',
            'User-Agent': 'tldr-model-adapter/0.1',
        }

        payload = {
            'model': model,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'max_tokens': int(os.environ.get('GITHUB_MAX_TOKENS', '1000')),
        }

        retry_attempts = max(1, int(os.environ.get('GITHUB_RETRY_ATTEMPTS', '4')))
        retry_base_delay = max(0.0, float(os.environ.get('GITHUB_RETRY_BASE_DELAY_SEC', '1.5')))
        retry_max_delay = max(retry_base_delay, float(os.environ.get('GITHUB_RETRY_MAX_DELAY_SEC', '20')))

        data = None
        last_error = None
        saw_transient_error = False
        for endpoint in endpoints:
            for attempt in range(1, retry_attempts + 1):
                try:
                    resp = requests.post(endpoint, headers=headers, json=payload, timeout=60)
                except requests.RequestException as e:
                    last_error = e
                    saw_transient_error = True
                    print(f'GitHub Models request transport error at {endpoint} (attempt {attempt}/{retry_attempts}): {e}')
                    if attempt >= retry_attempts:
                        break

                    delay = min(retry_max_delay, retry_base_delay * (2 ** (attempt - 1)) + random.uniform(0.0, 0.5))
                    print(f'Retrying after {delay:.2f}s...')
                    time.sleep(delay)
                    continue

                status = resp.status_code
                if status == 429 or 500 <= status < 600:
                    saw_transient_error = True
                    last_error = RuntimeError(f'HTTP {status}')
                    print(f'GitHub Models transient error at {endpoint} (attempt {attempt}/{retry_attempts}): HTTP {status}')
                    try:
                        print('Response text (truncated):', resp.text[:1000])
                    except Exception:
                        pass

                    if attempt >= retry_attempts:
                        break

                    retry_after_header = resp.headers.get('Retry-After')
                    if retry_after_header and retry_after_header.isdigit():
                        delay = min(retry_max_delay, float(retry_after_header))
                    else:
                        delay = min(retry_max_delay, retry_base_delay * (2 ** (attempt - 1)) + random.uniform(0.0, 0.5))
                    print(f'Retrying after {delay:.2f}s...')
                    time.sleep(delay)
                    continue

                if status >= 400:
                    last_error = RuntimeError(f'HTTP {status}')
                    print(f'GitHub Models non-retryable error at {endpoint}: HTTP {status}')
                    try:
                        print('Response text (truncated):', resp.text[:1000])
                    except Exception:
                        pass
                    break

                try:
                    data = resp.json()
                    break
                except Exception as e:
                    last_error = e
                    print(f'GitHub Models returned non-JSON response at {endpoint}: {e}')
                    try:
                        print('Response text (truncated):', resp.text[:1000])
                    except Exception:
                        pass
                    break

            if data is not None:
                break

        if data is None:
            print('GitHub Models request failed on all endpoints.')
            if last_error is not None:
                print('Last error:', last_error)
            if saw_transient_error:
                raise TransientAPIError('GitHub Models transient failure (429/5xx/transport). Retry later.')
            return None

        # Extract text content from common response shapes
        text = ''
        try:
            if isinstance(data, dict) and 'choices' in data and data['choices']:
                choice = data['choices'][0]
                if isinstance(choice, dict):
                    if 'message' in choice and isinstance(choice['message'], dict):
                        text = choice['message'].get('content', '')
                    elif 'text' in choice:
                        text = choice.get('text', '')
                    else:
                        # Fallback: stringify choice
                        text = json.dumps(choice)
            elif isinstance(data, dict) and 'output' in data:
                out = data['output']
                if isinstance(out, list):
                    parts = []
                    for item in out:
                        if isinstance(item, dict):
                            parts.append(item.get('content', ''))
                        else:
                            parts.append(str(item))
                    text = '\n'.join(parts)
                else:
                    text = str(out)
            else:
                text = json.dumps(data)
        except Exception as e:
            print('Error extracting text from GitHub Models response:', e)
            text = json.dumps(data)

        # Now attempt to parse JSON object from the model output similar to Gemini path
        try:
            json_str = text.strip()
            if '```json' in json_str:
                start = json_str.find('```json') + 7
                end = json_str.find('```', start)
                if end == -1:
                    json_str = json_str[start:]
                else:
                    json_str = json_str[start:end]
            elif '{' in json_str:
                start = json_str.find('{')
                end = json_str.rfind('}') + 1
                json_str = json_str[start:end]

            json_str = json_str.strip()
            if not json_str:
                raise ValueError('Empty JSON string from model')

            parsed = json.loads(json_str)
            parsed.setdefault('author', 'Unknown')
            if not parsed.get('date'):
                parsed['date'] = datetime.now().strftime('%d-%m-%Y')
            if 'category' in parsed:
                parsed['category'] = parsed['category'].replace(' ', '-')
            if 'filename' in parsed and not parsed['filename'].endswith('.md'):
                parsed['filename'] = parsed['filename'].strip().replace(' ', '-').lower()
                if not parsed['filename'].endswith('.md'):
                    parsed['filename'] += '.md'

            return SummaryOutput(**parsed)
        except Exception as e:
            print('Error parsing GitHub Models output as JSON:', e)
            print('Model output snippet:', (text or '')[:1000])
            return None
