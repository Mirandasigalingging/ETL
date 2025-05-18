import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        return ""

def scrape_products_from_page(url):
    html = fetch_page(url)
    if not html:
        return []
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for item in soup.select("div.collection-card"):
        try:
            title = item.select_one("h3.product-title").get_text(strip=True)
            price = item.select_one(".price").get_text(strip=True)
            rating_text = item.select_one("div.product-details p").get_text(strip=True)
            colors_text = item.select("div.product-details p")[1].get_text(strip=True)
            size_text = item.select("div.product-details p")[2].get_text(strip=True)
            gender_text = item.select("div.product-details p")[3].get_text(strip=True)
            image_url = item.select_one("img.collection-image")['src']
            products.append({
                "title": title,
                "price": price,
                "rating": rating_text,
                "colors": colors_text,
                "size": size_text,
                "gender": gender_text,
                "image_url": image_url,
                "timestamp": datetime.utcnow().isoformat()
            })
        except Exception as e:
            logger.warning(f"Error parsing product: {e}")
            continue
    return products

def fetch_products(pages=50):
    base_url = "https://fashion-studio.dicoding.dev"
    all_products = []

    for page_num in range(1, pages + 1):
        url = base_url if page_num == 1 else f"{base_url}/page{page_num}"
        print(f"Scraping {url}")
        page_data = scrape_products_from_page(url)
        all_products.extend(page_data)
    return all_products
