import pytest
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_results_page import AmazonResultsPage

@pytest.mark.parametrize("item", ["laptop", "headphones"])
def test_amazon_search(page, item):
    home = AmazonHomePage(page)
    results = AmazonResultsPage(page)
    home.load()
    home.search_product(item)
    assert "results" in page.title().lower()
    count = results.get_result_count()
    assert count > 0
