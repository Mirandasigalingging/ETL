import pandas as pd
import re

def process_data(data):
    df = pd.DataFrame(data)
    # Bersihkan kolom price
    df['price'] = df['price'].apply(lambda x: int(float(re.sub(r'[$,]', '', x)) * 16000) if x else 0)
    # Bersihkan rating
    df['rating'] = df['rating'].apply(lambda x: float(re.search(r"([\d.]+)", x).group(1)) if re.search(r"([\d.]+)", x) else 0)
    # Bersihkan colors
    df['colors'] = df['colors'].apply(lambda x: int(re.search(r"(\d+)", x).group(1)) if re.search(r"(\d+)", x) else 0)
    # Bersihkan size dan gender
    df['size'] = df['size'].apply(lambda x: x.replace("Size:", "").strip() if "Size:" in x else x)
    df['gender'] = df['gender'].apply(lambda x: x.replace("Gender:", "").strip() if "Gender:" in x else x)
    return df
