import re
import pandas as pd
import numpy as np

EXCHANGE_RATE = 16_000

def transform(data: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(data)

    # Bersihkan dan konversi price
    df["price"] = df["price"].str.replace("[$,]", "", regex=True).astype(float) * EXCHANGE_RATE

    # Bersihkan dan konversi rating
    df["rating"] = df["rating"].str.extract(r"([\d.]+)").astype(float)

    # Bersihkan dan konversi colors
    df["colors"] = df["colors"].str.extract(r"(\d+)").astype(float)
    df["colors"] = df["colors"].astype(int)

    # Bersihkan size dan gender
    df["size"] = df["size"].apply(lambda x: x.replace("Size:", "").strip() if isinstance(x, str) else x)
    df["gender"] = df["gender"].apply(lambda x: x.replace("Gender:", "").strip() if isinstance(x, str) else x)

    # Hapus baris tidak lengkap
    df = df.dropna(subset=["price", "rating", "colors", "size", "gender", "timestamp"])

    # Hapus baris dengan title 'Unknown Product'
    df = df[df["title"] != "Unknown Product"]

    return df

def clean_data(df):
    # Hapus duplikat
    df = df.drop_duplicates()

    # Ganti 'Pants' dan 'Unknown Product' di kolom 'title' jadi NaN
    df['title'] = df['title'].replace(['Pants', 'Unknown Product'], np.nan)

    # Ganti nilai 0 di kolom penting jadi NaN
    df['price'] = df['price'].replace(0, np.nan)
    df['rating'] = df['rating'].replace(0, np.nan)
    df['colors'] = df['colors'].replace(0, np.nan)

    # Hapus baris NaN di kolom penting
    df = df.dropna(subset=['title', 'price', 'rating', 'colors'])

    # Validasi rating di antara 1-5
    df['rating'] = df['rating'].apply(lambda x: x if 1 <= x <= 5 else np.nan)
    df = df.dropna(subset=['rating'])

    # Duplikat lagi
    df = df.drop_duplicates()

    return df
