from utils.extract import fetch_products
from utils.transform import process_data
from utils.load import save_to_csv, save_to_google_sheets

def main():
    # 1. Extract data dari website
    raw_data = fetch_products(pages=50)
    # 2. Transform dan bersihkan data
    df = process_data(raw_data)
    # 3. Save ke CSV
    save_to_csv(df, output_path='products.csv')
    # 4. Save ke Google Sheets
    save_to_google_sheets(df, json_keyfile='google-sheets-api.json',
                          sheet_url='https://docs.google.com/spreadsheets/d/1hTQoQgDOx0By5-C6G8hK3qofpUK1qfCYU__F1BW1DQc')

if __name__ == "__main__":
    main()
