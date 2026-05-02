import os
import sys
import pathlib

# Ensure project root is on sys.path so `scripts` is importable when running tests directly
ROOT = str(pathlib.Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from scripts.process_links import _extract_arxiv_page_data


def test_arxiv_extraction_from_fixture():
    here = os.path.dirname(__file__)
    fixture = os.path.join(here, 'fixtures', 'arxiv_sample.html')
    with open(fixture, 'r', encoding='utf-8') as f:
        html = f.read()

    result = _extract_arxiv_page_data(html)

    # Expected authors from fixture
    expected = ['Zihao Li', 'Jiaru Zou', 'Feihao Fang']
    assert 'authors' in result
    # Ensure extractor finds each expected author (order preserved)
    for name in expected:
        assert any(name in a for a in result['authors']), f"Missing author {name}"

    assert result['title'] == 'Test ArXiv Paper Title'
    assert 'context' in result and 'Abstract' in result['context']


def test_extraction_quality_detection():
    """Test the quality detection for fallback triggering."""
    from scripts.process_links import is_extraction_quality_poor

    # Good extraction should NOT trigger fallback
    good = {
        'title': 'Real Title',
        'authors': ['Author Name'],
        'context': 'A' * 500,
    }
    assert not is_extraction_quality_poor(good), "Good extraction should not trigger fallback"

    # Unknown author + short content should trigger fallback
    poor = {
        'title': 'Real Title',
        'authors': ['Unknown'],
        'context': 'Short',
    }
    assert is_extraction_quality_poor(poor), "Poor extraction should trigger fallback"

    # Unknown title + unknown author should trigger fallback
    very_poor = {
        'title': 'Unknown title',
        'authors': ['Unknown'],
        'context': 'A' * 500,
    }
    assert is_extraction_quality_poor(very_poor), "Very poor extraction should trigger fallback"

    # arXiv pages with unknown authors should trigger fallback even if content is long
    arxiv_poor = {
        'title': 'Step-level Optimization for Efficient Computer-use Agents',
        'authors': ['Unknown'],
        'context': 'A' * 1000,
    }
    assert is_extraction_quality_poor(arxiv_poor, url='https://arxiv.org/html/2604.27151v1'), \
        "arXiv pages with unknown authors should trigger fallback"


if __name__ == '__main__':
    test_arxiv_extraction_from_fixture()
    print('arXiv extractor test: OK')

