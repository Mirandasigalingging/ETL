import pandas as pd
import numpy as np
import re

def process_data(data):
    df = pd.DataFrame(data)
    
    # Bersihkan kolom 'price' dan tangani nilai tidak valid
    def clean_price(x):
        if pd.isnull(x) or x == 'Price Unavailable':
            return 0
        try:
            return int(float(re.sub(r'[$,]', '', x)) * 16000)
        except:
            return 0
    
    df['price'] = df['price'].apply(clean_price)
    
    # Bersihkan kolom 'rating'
    def clean_rating(x):
        if pd.isnull(x):
            return 0
        match = re.search(r"([\d.]+)", x)
        return float(match.group(1)) if match else 0
    
    df['rating'] = df['rating'].apply(clean_rating)
    
    # Bersihkan kolom 'colors'
    def clean_colors(x):
        if pd.isnull(x):
            return 0
        match = re.search(r"(\d+)", x)
        return int(match.group(1)) if match else 0
    
    df['colors'] = df['colors'].apply(clean_colors)
    
    # Bersihkan 'size'
    df['size'] = df['size'].apply(lambda x: x.replace("Size:", "").strip() if "Size:" in x else x)
    
    # Bersihkan 'gender'
    df['gender'] = df['gender'].apply(lambda x: x.replace("Gender:", "").strip() if "Gender:" in x else x)
    
    return df

# Tambahkan fungsi untuk membersihkan data invalid dan duplikat
def clean_data(df):
    import numpy as np
    
    # Hapus duplikat
    df = df.drop_duplicates()

    # Ganti 'Unknown Product' dan 'Pants' (dengan nilai 0) jadi NaN
    df['product_name'] = df['product_name'].replace(['Unknown Product', 'Pants'], np.nan)
    
    # Ganti nilai 0 di kolom penting menjadi NaN
    df['price'] = df['price'].replace(0, np.nan)
    df['rating'] = df['rating'].replace(0, np.nan)
    df['colors'] = df['colors'].replace(0, np.nan)

    # Hapus baris yang NaN di kolom penting
    df = df.dropna(subset=['product_name', 'price', 'rating', 'colors'])
    
    # Jika ingin validasi rating di 1-5
    df['rating'] = df['rating'].apply(lambda x: x if 1 <= x <= 5 else np.nan)
    df = df.dropna(subset=['rating'])
    
    # Hapus duplikat lagi jika perlu
    df = df.drop_duplicates()
    
    return df
