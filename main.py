from utils.utils_extract import fetch_products
from utils.utils_transform import process_data, clean_data
from utils.utils_load import save_to_csv, save_to_google_sheets

def main():
    raw_data = fetch_products(pages=50)
    df = process_data(raw_data)

    print("Kolom data:", df.columns.tolist())  # Pastikan kolomnya benar

    df_bersih = clean_data(df)

    print("Data bersih:")
    print(df_bersih.head())

    save_to_csv(df_bersih)
    save_to_google_sheets(df_bersih, json_keyfile='etl-fashion-data-ee489a18d56a.json')

if __name__ == "__main__":
    main()
