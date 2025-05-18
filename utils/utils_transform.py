import pandas as pd
import re
import numpy as np

def clean_price(price_str):
    if not price_str or 'Unavailable' in price_str:
        return 0
    try:
        num = float(re.sub(r'[$,]', '', price_str))
        return int(num * 16000)
    except:
        return 0

def clean_rating(rating_str):
    match = re.search(r"([\d.]+)", rating_str)
    if match:
        return float(match.group(1))
    return 0.0

def clean_colors(colors_str):
    match = re.search(r"(\d+)", colors_str)
    if match:
        return int(match.group(1))
    return 0

def clean_size(size_str):
    return size_str.replace("Size:", "").strip()

def clean_gender(gender_str):
    return gender_str.replace("Gender:", "").strip()

def process_data(raw_list):
    df = pd.DataFrame(raw_list)
    # Bersihkan kolom
    df['price'] = df['price'].apply(clean_price)
    df['rating'] = df['rating'].apply(clean_rating)
    df['colors'] = df['colors'].apply(clean_colors)
    df['size'] = df['size'].apply(clean_size)
    df['gender'] = df['gender'].apply(clean_gender)

    # Hapus data invalid
    df = df[df['title'].str.lower() != 'unknown product']
    df = df.dropna(subset=['price', 'rating', 'colors', 'size', 'gender'])
    return df
