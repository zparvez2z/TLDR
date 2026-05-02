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


if __name__ == '__main__':
    test_arxiv_extraction_from_fixture()
    print('arXiv extractor test: OK')

