from utils.utils_extract import fetch_products
from utils.utils_transform import process_data, clean_data
from utils.utils_load import save_to_csv, save_to_google_sheets

def main():
    # Ambil data dari proses extract
    raw_data = fetch_products(pages=50)
    
    # Transform data awal
    df = process_data(raw_data)
    
    # Bersihkan data agar sesuai kriteria
    df_bersih = clean_data(df)
    
    # Debug: lihat data bersih sebelum disimpan
    print("Data bersih:")
    print(df_bersih.head())
    print("Jumlah baris:", len(df_bersih))
    
    # Simpan ke CSV dan Google Sheets
    save_to_csv(df_bersih)
    save_to_google_sheets(df_bersih, json_keyfile='etl-fashion-data-ee489a18d56a.json')

if __name__ == "__main__":
    main()
