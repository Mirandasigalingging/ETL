import pandas as pd
from utils.utils_extract import extract_page
from utils.utils_transform import transform_data
from utils.utils_load import save_csv, save_to_google_sheets

def main():
    all_products = []
    for page in range(1, 51):
        print(f"Extract halaman {page}")
        products = extract_page(page)
        print(f"Extracted page {page}, produk: {len(products)}")
        all_products.extend(products)

    df = pd.DataFrame(all_products)
    print(f"Total produk: {len(df)}")
    print("Contoh data:\n", df.head())

    # proses transform
    df_clean = transform_data(df)

    # simpan CSV
    save_csv(df_clean, 'products.csv')

    # simpan ke Google Sheets
    creds_path = 'google-sheets-api.json'
    sheet_url = 'https://docs.google.com/spreadsheets/d/ID_SHEET_YANG_DIBAGI/edit?usp=sharing' # ganti sesuai
    save_to_google_sheets(df_clean, creds_path, sheet_url)

if __name__ == "__main__":
    main()
