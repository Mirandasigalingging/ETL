from utils.utils_extract import scrape_all_pages
from utils.utils_transform import transform_data
from utils.utils_load import save_csv, save_to_gsheet

def main():
    print("Memulai proses ETL...")

    # Tahap Extract
    products, timestamps = scrape_all_pages()
    if not products:
        print("Gagal: Tidak ada produk yang berhasil diambil dari website.")
        return
    print(f"Berhasil mengekstrak {len(products)} produk dari web.")

    # Tahap Transform
    df = transform_data(products, timestamps)
    if df.empty:
        print("Data hasil transformasi kosong. Tidak menyimpan ke CSV atau Google Sheets.")
        return
    print(f"Transformasi selesai. Total baris bersih: {len(df)}")

    # Tahap Load
    print("Menyimpan ke products.csv...")
    save_csv(df)

    print("Menyimpan ke Google Sheets...")
    spreadsheet_id = "https://docs.google.com/spreadsheets/d/1hTQoQgDOx0By5-C6G8hK3qofpUK1qfCYU__F1BW1DQc/edit?gid=0#gid=0"
    save_to_gsheet(df, spreadsheet_id)

    print("Proses ETL selesai tanpa error.")

if __name__ == "__main__":
    main()
