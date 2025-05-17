from utils.utils_extract import extract_page
from utils.utils_transform import transform_data
from utils.utils_load import save_csv, save_to_google_sheets

# kode main seperti biasa

def main():
    all_products = []
    total_pages = 50
    for page in range(1, total_pages + 1):
        products = extract_page(page)
        all_products.extend(products)
        print(f"Extracted page {page}, produk: {len(products)}")
    
    df = pd.DataFrame(all_products)
    print("Kolom DataFrame:", df.columns)
    print("Contoh data:\n", df.head())

    if df.empty:
        print("DataFrame kosong, cek fungsi extract_page()")
        return

    df_clean = transform_data(df)
    save_csv(df_clean, 'products.csv')
    print("Data disimpan ke CSV.")

    creds_json = 'tough-anagram-460012-t4-e5a2928ac1b3.json'  # Sesuaikan path file creds
    sheet_url = 'https://docs.google.com/spreadsheets/d/1hTQoQgDOx0By5-C6G8hK3qofpUK1qfCYU__F1BW1DQc/edit?usp=sharing'
    save_to_google_sheets(df_clean, creds_json, sheet_url)
    print("Data berhasil disimpan ke Google Sheets.")

if __name__ == "__main__":
    main()
