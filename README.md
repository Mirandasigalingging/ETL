# Proyek ETL: Extract, Transform, Load Data ke Google Sheets

Proyek ini merupakan implementasi pipeline ETL (Extract, Transform, Load) yang menggunakan Python. Data diekstrak dari sumber tertentu, diproses/transformasi sesuai kebutuhan, lalu hasil akhirnya diunggah ke Google Sheets.

    ETL/
    ├── tests
    │   ├── test_extract.py
    │   ├── test_transform.py
    │   ├── test_load.py
    ├── utils
    │   ├── extract.py
    │   ├── transform.py
    │   ├── load.py
    ├── main.py
    ├── requirements.txt
    ├── google-sheets-api.json

- **tests/** : Berisi script pengujian otomatis untuk tiap bagian ETL.
- **utils/** : Berisi fungsi-fungsi untuk extract, transform, load.
- **main.py** : Script utama yang menjalankan proses ETL secara keseluruhan.
- **requirements.txt** : Daftar dependencies yang diperlukan.
- **google-sheets-api.json** : Credential JSON untuk akses Google Sheets API.

---

## Langkah-langkah Pengerjaan

### 1. Membuat Struktur Folder dan Berkas
Buat folder dan file sesuai struktur di atas.

### 2. Membuat Repository GitHub
- Buat repository baru di GitHub, misalnya: `ETL`.
- Upload semua berkas ke repo tersebut.
- Commit dan push perubahan.

### 3. Mengkloning Repository di Google Colab
Setelah repo tersedia, jalankan di Google Colab:

```python
!git clone https://github.com/Mirandasigalingging/ETL.git /content/ETL
%cd /content/ETL
```
### 4. Menginstall Dependencies
```python
!pip install -r requirements.txt
```

### 5. Menjalankan Skrip Utama (main.py)
```python
!python main.py
```
### 6. Menjalankan Test Coverage
Untuk memastikan semua bagian berjalan dengan baik dan mendapatkan laporan coverage:
```python
!coverage run -m pytest tests
!coverage report
```
### Hasil Output
Data yang telah diproses akan diunggah ke Google Sheets yang dapat diakses melalui link berikut:
[Google Sheets Data](https://docs.google.com/spreadsheets/d/1hTQoQgDOx0By5-C6G8hK3qofpUK1qfCYU__F1BW1DQc/edit?usp=sharing)

Catatan
Pastikan file google-sheets-api.json sudah diisi dengan credentials Google API yang benar.
Pastikan dependencies di requirements.txt sudah lengkap dan kompatibel.
