import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

def save_csv(df, filename="products.csv"):
    try:
        if df.empty:
            print("Tidak ada data untuk disimpan ke CSV.")
            return
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke file: {filename}")
    except Exception as e:
        print(f"❌ Gagal menyimpan CSV: {e}")

def save_to_gsheet(df, spreadsheet_id, sheet_name="Sheet1", credentials_path="etl-fashion-data-e7a102c009e2.json"):
    try:
        if df.empty:
            print("Tidak ada data untuk disimpan ke Google Sheets.")
            return

        creds = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )

        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        # Convert DataFrame to list of lists
        values = [df.columns.tolist()] + df.values.tolist()
        body = {"values": values}

        result = sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body=body
        ).execute()

        updated = result.get("updatedCells", 0)
        print(f"Berhasil menyimpan ke Google Sheets: {updated} sel diperbarui.")
    except Exception as e:
        print(f"Gagal menyimpan ke Google Sheets: {e}")
