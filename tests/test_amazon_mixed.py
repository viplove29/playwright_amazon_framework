import requests
from pages.amazon_home_page import AmazonHomePage

def test_ui_api_combo(page):
    home = AmazonHomePage(page)
    home.load()
    home.search_product("books")
    assert "books" in page.title().lower()

    response = requests.get("https://fakestoreapi.com/products")
    assert response.status_code == 200
    assert len(response.json()) > 0
