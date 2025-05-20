import pytest
from utils import utils_extract as extract
from datetime import datetime

class DummyResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception(f"HTTP {self.status_code}")

def test_scrape_page_success(monkeypatch):
    html = """
    <div class="collection-card">
      <h3 class="product-title">Test Shirt</h3>
      <div class="price-container"><span class="price">$10.00</span></div>
      <div class="product-details">
        <p>Rating: ⭐ 4.5 / 5</p>
        <p>2 Colors</p>
        <p>Size: M</p>
        <p>Gender: Unisex</p>
      </div>
      <img class="collection-image" src="http://example.com/image.jpg" />
    </div>
    """
    monkeypatch.setattr("requests.get", lambda url: DummyResponse(html))
    data = extract.fetch_products(pages=1)
    assert isinstance(data, list)
    assert len(data) == 1
    item = data[0]
    assert "title" in item
    assert "timestamp" in item
    datetime.fromisoformat(item["timestamp"])

def test_fetch_products_structure():
    data = extract.fetch_products(pages=1)
    assert isinstance(data, list)
    if data:
        sample = data[0]
        assert "title" in sample
        assert "price" in sample
        assert "rating" in sample
        assert "colors" in sample
        assert "size" in sample
        assert "gender" in sample
        assert "timestamp" in sample
