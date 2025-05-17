import pandas as pd
import re

def transform_data(df):
    # Bersihkan kolom 'price' dari simbol $ dan ubah ke angka
    if 'price' in df.columns:
        df['price'] = df['price'].replace('[\$,]', '', regex=True)
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    # Ekstrak rating dari teks
    if 'rating' in df.columns:
        def extract_rating(text):
            if isinstance(text, str):
                match = re.search(r'⭐\s*([\d\.]+)', text)
                if match:
                    return float(match.group(1))
            return None
        df['rating'] = df['rating'].apply(extract_rating)
    # Hitung jumlah warna dari kolom 'colors'
    if 'colors' in df.columns:
        def count_colors(text):
            if isinstance(text, str):
                return len([c for c in text.split() if c])
            return 0
        df['colors'] = df['colors'].apply(count_colors)
    # Bersihkan 'size' dan 'gender'
    if 'size' in df.columns:
        df['size'] = df['size'].astype(str).str.replace('Size:', '', regex=False).str.strip()
    if 'gender' in df.columns:
        df['gender'] = df['gender'].astype(str).str.replace('Gender:', '', regex=False).str.strip()
    # Hapus baris null di kolom penting
    df = df.dropna(subset=['title', 'price'])
    # Hapus duplikat
    df = df.drop_duplicates()
    return df