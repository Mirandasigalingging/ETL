import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extract_page(page_num):
    url = f"https://fashion-studio.dicoding.dev/?page={page_num}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching page {page_num}: {e}")
        return []

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='collection-card')
        results = []

        for item in products:
            try:
                img_tag = item.find('img', class_='collection-image')
                img_url = img_tag['src'] if img_tag else None

                title_tag = item.find('h3', class_='product-title')
                title = title_tag.get_text(strip=True) if title_tag else None

                price_tag = item.find('span', class_='price')
                price = price_tag.get_text(strip=True) if price_tag else None

                rating_tag = item.find('p', style=lambda s: s and 'Rating' in s)
                rating_text = rating_tag.get_text(strip=True) if rating_tag else None

                colors_tag = item.find('p', style=lambda s: s and 'Colors' in s)
                colors = colors_tag.get_text(strip=True) if colors_tag else None

                size_tag = item.find('p', style=lambda s: s and 'Size' in s)
                size = size_tag.get_text(strip=True) if size_tag else None

                gender_tag = item.find('p', style=lambda s: s and 'Gender' in s)
                gender = gender_tag.get_text(strip=True) if gender_tag else None

                results.append({
                    'img_url': img_url,
                    'title': title,
                    'price': price,
                    'rating': rating_text,
                    'colors': colors,
                    'size': size,
                    'gender': gender,
                    'timestamp': datetime.now().isoformat()
                })
            except Exception as e:
                print(f"Error parsing product: {e}")
                continue
        return results
    except Exception as e:
        print(f"Error parsing page {page_num}: {e}")
        return