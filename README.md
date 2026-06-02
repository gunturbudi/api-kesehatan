# API Kesehatan (Pedagogical FHIR API Server)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![FHIR](https://img.shields.io/badge/FHIR-HL7-firebrick?style=for-the-badge)](https://hl7.org/fhir/)

Repositori ini berisi implementasi **API Kesehatan Sederhana** berbasis standar **HL7 FHIR (Fast Healthcare Interoperability Resources)**. Proyek ini dikembangkan sebagai bahan ajar (**pedagogis**) untuk membantu mahasiswa memahami konsep dasar pertukaran data klinis dan interoperabilitas sistem informasi kesehatan secara praktis menggunakan Python dan FastAPI.

> [!NOTE]
> **Tujuan Pembelajaran:** 
> Proyek ini dirancang khusus untuk pembelajaran (non-produksi) agar mahasiswa dapat melihat bentuk nyata data terstruktur berstandar FHIR, cara mengakses API menggunakan HTTP Methods (`GET` & `POST`), serta cara mendeploy layanan API ke internet secara gratis.

---

## 🚀 Fitur Utama

- **FHIR-Compliant Resources**: Menyediakan dummy data klinis berstruktur JSON standar FHIR R4:
  - `Patient` (Data Demografi Pasien)
  - `Observation` (Tanda-Tanda Vital: Tekanan Darah, Detak Jantung, Suhu Tubuh)
  - `Bundle` (Kumpulan resource pencarian data klinis)
- **Automatic Interactive Docs**: Dokumentasi API interaktif otomatis menggunakan Swagger UI (`/docs`) dan ReDoc (`/redoc`) sehingga mahasiswa bisa menguji API langsung lewat browser tanpa aplikasi tambahan (seperti Postman).
- **Production Ready for Cloud**: Dikonfigurasi agar siap dideploy secara otomatis ke **Render.com** (atau platform cloud lainnya).

---

## 📂 Struktur Repositori

```bash
api-kesehatan/
├── .gitignore          # Mengabaikan file cache Python lokal
├── README.md           # Panduan dan materi penjelasan pedagogis ini
├── main.py             # Kode program FastAPI & dummy data format FHIR
└── requirements.txt    # Daftar pustaka (library) yang dibutuhkan
```

---

## 🛠️ Cara Menjalankan Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan API ini di laptop/komputermu:

### 1. Prasyarat
Pastikan kamu telah menginstal **Python 3.x** di komputermu dan mencentang opsi **"Add Python to PATH"** saat proses instalasi.

### 2. Instalasi Pustaka
Buka terminal/Command Prompt di dalam direktori `api-kesehatan` lalu jalankan perintah berikut untuk menginstal pustaka yang dibutuhkan:
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Server
Jalankan server pengembangan lokal (Uvicorn) dengan perintah berikut:
```bash
uvicorn main:app --reload
```
Server akan berjalan di alamat: **`http://127.0.0.1:8000`**

### 4. Mengakses Dokumentasi Interaktif
Buka browser favoritmu lalu kunjungi:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Di halaman ini, kamu bisa menguji setiap endpoint secara interaktif dengan mengklik tombol **"Try it out"**, lalu **"Execute"**.

---

## 🔌 Endpoint API yang Tersedia

### 1. Informasi Sistem (Root)
* **Method**: `GET`
* **Path**: `/`
* **Fungsi**: Memeriksa apakah server API berjalan dengan baik.

### 2. Mengambil Data Pasien (FHIR Patient)
* **Method**: `GET`
* **Path**: `/patients/{patient_id}`
* **Fungsi**: Mengambil informasi demografi pasien berdasarkan ID tertentu dalam format resource **FHIR Patient**.
* **Dummy Data**: ID `1` (John Doe) dan ID `2` (Annisa Maulida).

### 3. Mendaftarkan Pasien Baru
* **Method**: `POST`
* **Path**: `/patients`
* **Fungsi**: Mensimulasikan pendaftaran pasien baru dan mengembalikan representasi objek **FHIR Patient** hasil pendaftaran.

### 4. Mengambil Tanda Vital Pasien (FHIR Observation Bundle)
* **Method**: `GET`
* **Path**: `/patients/{patient_id}/observations`
* **Fungsi**: Mengambil semua tanda-tanda vital pasien (seperti tekanan darah, nadi, atau suhu tubuh) dalam bentuk resource **FHIR Bundle** bertipe `searchset` berisi daftar resource **FHIR Observation**.

---

## ☁️ Panduan Deploy ke Render.com

API ini dapat dipublikasikan ke internet menggunakan platform gratis **Render.com**:

1. **Unggah Kode**: Pastikan repositori ini telah diunggah ke akun GitHub pribadimu.
2. **Buat Web Service**: Masuk ke [Render Dashboard](https://dashboard.render.com), buat **Web Service** baru, lalu hubungkan dengan repositori GitHub-mu.
3. **Konfigurasi Parameter**:
   - **Name**: `api-kesehatan`
   - **Region**: `Singapore` (terdekat dengan Indonesia)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: `Free`
4. **Deploy!** Klik tombol **Create Web Service**. Dalam 2-5 menit API akan aktif di internet dengan URL publik gratis (contoh: `https://api-kesehatan.onrender.com`).

---

## 📚 Catatan Akademik & Lisensi

Proyek ini dibuat sebagai media pembelajaran mata kuliah **Pertukaran Informasi Kesehatan / Interoperabilitas Data Medis**. Mahasiswa sangat disarankan untuk melakukan eksplorasi dengan:
1. Menambahkan endpoint diagnosa (**FHIR Condition**).
2. Menghubungkan API dengan database relasional (seperti PostgreSQL) untuk penyimpanan data pasien secara permanen.
3. Menambahkan fitur autentikasi endpoint untuk keamanan data medis.

*Dikembangkan oleh **Dr.techn. Guntur Budi Herwanto, M.Cs.** - Universitas Gadjah Mada.*
