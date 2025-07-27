# Social Media Scraper Web App

Sebuah aplikasi web untuk melakukan scraping data dari Twitter, Instagram, dan Facebook berdasarkan kata kunci pencarian.

## Fitur

- Pencarian berdasarkan kata kunci
- Support untuk tiga platform media sosial:
  - Twitter
  - Instagram
  - Facebook
- Menampilkan hasil dalam bentuk tabel
- Ekspor data ke format JSON
- Responsive design (dapat digunakan di mobile dan desktop)

## Persyaratan Sistem

- Python 3.7+
- pip (Python package manager)

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/social-media-scraper.git
   cd social-media-scraper
   ```

2. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate     # Untuk Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Konfigurasi

Untuk scraping Instagram, Anda mungkin perlu login. Buat file `config.ini` di folder utama dengan konten berikut:

```ini
[instagram]
username = your_username
password = your_password
```

**Catatan**: Simpan file ini di .gitignore untuk menghindari kompromi akun Anda.

## Penggunaan

1. Jalankan aplikasi:
   ```bash
   python app.py
   ```

2. Buka browser dan akses:
   ```
   http://localhost:5000
   ```

3. Masukkan:
   - Kata kunci pencarian
   - Pilih platform media sosial
   - Jumlah post yang ingin di-scrape (max 100)

4. Klik "Scrape Data" untuk memulai proses

5. Hasil akan ditampilkan dalam tabel dan bisa di-export ke JSON

## Struktur Proyek

```
social-media-scraper/
│
├── app.py                # File utama Flask
├── config.ini            # File konfigurasi (opsional)
├── requirements.txt      # Dependensi Python
├── README.md             # Dokumentasi ini
│
├── scraper/              # Modul scraper
│   ├── twitter_scraper.py
│   ├── instagram_scraper.py
│   └── facebook_scraper.py
│
├── static/               # Aset statis
│   └── style.css
│
└── templates/            # Template HTML
    └── index.html
```

## Batasan dan Catatan Penting

1. **Legalitas**:
   - Scraping mungkin melanggar Terms of Service beberapa platform
   - Gunakan hanya untuk tujuan pembelajaran/pribadi
   - Pertimbangkan untuk menggunakan API resmi jika tersedia

2. **Autentikasi**:
   - Instagram memerlukan login untuk scraping
   - Facebook mungkin memblokir akses jika terlalu banyak request

3. **Rate Limiting**:
   - Aplikasi sudah memiliki delay antar request untuk menghindari pemblokiran
   - Jangan melakukan terlalu banyak request dalam waktu singkat

## Kontribusi

Kontribusi dipersilakan! Silakan buka issue atau pull request untuk:
- Perbaikan bug
- Fitur baru
- Peningkatan dokumentasi

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).