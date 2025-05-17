import gspread
from gspread_dataframe import set_with_dataframe

def save_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"Data disimpan ke file CSV: {filename}")
    except Exception as e:
        print(f"Error menyimpan CSV: {e}")

def save_to_google_sheets(df, creds_json, sheet_url):
    try:
        gc = gspread.service_account(filename=creds_json)
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.get_worksheet(0)
        worksheet.clear()
        set_with_dataframe(worksheet, df)
        print("Data berhasil disimpan ke Google Sheets")
    except Exception as e:
        print(f"Error saat menyimpan ke Google Sheets: {e}")