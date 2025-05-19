from utils.extract import extract_all
from utils.transform import transform, clean_data
from utils.load import load_to_csv

def main():
    # Extract
    raw = extract_all(pages=50)

    # Transform
    df = transform(raw)

    # Debug: cek kolom
    print("Kolom data setelah transform:", df.columns.tolist())

    # Bersihkan data
    df_bersih = clean_data(df)

    # Cek hasil bersih
    print("Data bersih contoh:")
    print(df_bersih.head())

    # Save
    load_to_csv(df_bersih, output_path="products.csv")

if __name__ == "__main__":
    main()
