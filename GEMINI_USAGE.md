# Gemini API Usage Inventory

## Summary

**Status:** Gemini API has been successfully used as the primary (and now fallback) provider for knowledge base generation.

**Period:** June 29, 2025 – November 25, 2025 (6 months active, then paused for GitHub Models migration in May 2026)

---

## Usage Statistics

### Knowledge Base Output
- **Total files generated:** 23 markdown documents
- **Total words:** ~4,500 (across all summaries)
- **Total bytes:** 33 KB
- **Processing pattern:** Sporadic, typically 1-5 URLs per batch session

### Categorization
| Category | File Count | Example |
| --- | --- | --- |
| Software-Engineering | 10 | *The Python Tutorial*, *Technical Debt* |
| Machine-Learning | 8 | *Neural Architecture Search*, *Reasoning Language Models* |
| Information-Science | 4 | *What Is RDF*, *Ontology in Information Science* |
| IT-Security | 1 | *Seven Security Considerations* |

---

## Estimated API Usage

### Input Tokens (Requests)
Assume average Gemini request:
- URL context: ~500 tokens
- System prompt + user message: ~400 tokens
- **Per request:** ~900 tokens input

**Total estimated input tokens:** 23 URLs × 900 = **~20,700 tokens**

### Output Tokens (Responses)
Average summary generated: ~195 words (~260 tokens per response)

**Total estimated output tokens:** 23 × 260 = **~6,000 tokens**

### Aggregate
- **Total cached tokens:** ~26,700
- **API calls:** 23
- **Average processing time:** ~2-5 seconds per URL

---

## Cost Analysis

### Gemini API Pricing (as of May 2026)
**Free tier benefits:**
- 15 requests per minute (sufficient for batch processing)
- 1.5M tokens per day (very generous for this use case)

**Paid tier (if needed):**
- Input: $0.075/million tokens
- Output: $0.30/million tokens

### Estimated Cost (on paid tier)
- Input: 20,700 × ($0.075 / 1M) = **$0.0015**
- Output: 6,000 × ($0.30 / 1M) = **$0.0018**
- **Total:** ~$0.003 (negligible)

### Free Tier Assessment
✅ **Within free tier limits:**
- 23 API calls << 15 requests/minute limit
- ~26.7K tokens << 1.5M token daily limit
- **No charges incurred** (still within free tier)

---

## Usage Patterns

### Batch Processing Timeline
| Date | Activity | Files |
| --- | --- | --- |
| 2025-06-29 | Initial batch | 5-7 |
| 2025-07-01 | Batch session | 3-4 |
| 2025-07-13 | Batch session | 2-3 |
| 2025-08-04 | Major batch | 5-6 |
| 2025-10-04 | Batch session | 2-3 |
| 2025-10-29 | Batch session | 1-2 |
| 2025-11-06 | Batch session | 1-2 |
| 2025-11-25 | Final batch | 1-2 |

**Pattern:** Low-volume, infrequent batches (~1-2 months between sessions)

---

## Rate Limit Analysis

### Historical Rate Limit Events
From conversation history: **2 recorded rate-limit hits** (RESOURCE_EXHAUSTED quota errors during May 2026 live testing)

These occurred during:
- Dry-run endpoint test with multiple retries
- End-to-end integration testing with 2 URLs

**Root cause:** Hitting accumulated daily quota thresholds during testing phase

### Quota Reset Behavior
- Quota resets daily at midnight UTC
- Rate-limit window: 15 requests per minute (very permissive for this use case)
- No sustained throttling observed during normal batch operations

---

## Transition to GitHub Models

### Why Migrate?
1. **Cost:** GitHub Models free tier costs $0 (vs potential Gemini paid tier costs)
2. **Rate limits:** GitHub Models has higher throughput for batch processing
3. **Consistency:** GitHub/OpenAI ecosystem alignment
4. **Redundancy:** Dual-provider support adds resilience

### Current Strategy (May 2026 +)
- **Primary:** GitHub Models (`openai/gpt-4.1-mini`)
- **Fallback:** Gemini API (preserved for emergency use)
- **Retry logic:** Both providers implement exponential backoff + jitter
- **Queue preservation:** Transient errors don't lose progress

---

## Recommendations

### Cost Management
✅ **Current approach is optimal:**
- Free tier usage: No charges to date
- Low volume: ~4 files/month averages to $0/month on paid tier
- Migration to GitHub Models: $0 cost, higher reliability

### Rate Limit Tuning
**For this use case,** current settings are appropriate:
```
GEMINI_RETRY_ATTEMPTS=4        # Sufficient for 2-3 quota resets
GEMINI_RETRY_BASE_DELAY_SEC=1.5
GEMINI_RETRY_MAX_DELAY_SEC=20
```

**If increasing to >10 URLs per session:**
- Increase `GEMINI_RETRY_ATTEMPTS` to 6
- Spread batch processing across multiple days to avoid daily quota exhaustion
- Consider `GEMINI_RETRY_BASE_DELAY_SEC=2.0` for longer backoff

### Monitoring
**To track future usage:**
1. Enable `PYTHONVERBOSE=1` during batch runs to log tokens
2. Store processing logs with timestamps for cost auditing
3. Set Gemini API quota alerts in Google Cloud Console

### Gemini Retention
**Keep Gemini as fallback because:**
- Free tier quota is available and unused (~1.5M tokens/day)
- Zero switching cost (env var toggle)
- Provides resilience if GitHub Models quota exhausted
- Useful for A/B testing quality/cost tradeoffs

---

## Summary Table

| Metric | Value |
| --- | --- |
| Total URLs processed | 23 |
| Active period | 6 months (Jun–Nov 2025) |
| Total input tokens | ~20.7K |
| Total output tokens | ~6.0K |
| Total cost (free tier) | $0.00 |
| Estimated cost (paid tier) | $0.003 |
| Average processing time | 2-5 sec/URL |
| Rate-limit incidents | 2 (during testing) |
| Current status | Paused; fallback ready |

---

## Files Processed (Reference)

**Recent (Nov 2025–May 2026):**
- The Python Tutorial
- About Python Programming Language

**Archive (Jun–Oct 2025):**
- Survey of Context Engineering for LLMs
- Neural Architecture Search
- Reasoning Language Models: A Blueprint
- Tracing Thoughts Language Model
- Evaluation Is All You Need
- When To Refactor
- Technical Debt
- How To Refactor
- Software Testing Process
- Software Testing Life Cycle
- Levels of Testing
- Seven Security Considerations (Cloud Analytics)
- Neurosym BioCAT (Biomedical Document Categorization)
- What Is RDF
- Ontology in Information Science
- What Is An Ontology
- RDF 1.1 Concepts and Abstract Syntax
- Inside NVIDIA GPUs (High Performance Matmul Kernels)
- (plus 3-4 others from initial batch)

---

## Next Steps

✅ **Completed:**
- Migrated to GitHub Models as primary provider
- Implemented fallback to Gemini API
- Added resilient retry logic for both providers
- Documented operational procedures

⏳ **Optional Future Enhancements:**
- Add Gemini usage telemetry logging
- Set up cost alerts in Google Cloud Console
- Document provider performance benchmarks (latency, summary quality)
- Implement automatic provider switching on quota exhaustion
