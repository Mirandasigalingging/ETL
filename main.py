from utils.utils_extract import fetch_products
from utils.utils_transform import process_data, clean_data
from utils.utils_load import save_to_csv, save_to_google_sheets

def main():
    raw_data = fetch_products(pages=50)
    df = process_data(raw_data)

    # Cek nama-nama kolom
    print("Kolom data:", df.columns.tolist())

    # Pastikan kolom yang benar sudah sesuai
    df_bersih = clean_data(df)

    # Cek data bersih
    print("Data bersih:")
    print(df_bersih.head())
    print("Jumlah baris:", len(df_bersih))
    
    # Simpan hasil bersih
    save_to_csv(df_bersih)
    save_to_google_sheets(df_bersih, json_keyfile='etl-fashion-data-ee489a18d56a.json')

if __name__ == "__main__":
    main()
