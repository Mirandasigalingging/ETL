import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
import logging

def save_to_csv(df, output_path='products.csv'):
    try:
        df.to_csv(output_path, index=False)
        print(f"Data berhasil disimpan ke {output_path}")
    except Exception as e:
        print(f"Gagal menyimpan CSV: {e}")

def save_to_google_sheets(df, json_keyfile='google-sheets-api.json', sheet_url='https://docs.google.com/spreadsheets/d/1hTQoQgDOx0By5-C6G8hK3qofpUK1qfCYU__F1BW1DQc/edit'):
    try:
        gc = gspread.service_account(filename=json_keyfile)
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.sheet1
        worksheet.clear()
        set_with_dataframe(worksheet, df)
        print("Data berhasil disimpan ke Google Sheets")
    except Exception as e:
        print(f"Error saat menyimpan ke Google Sheets: {e}")
