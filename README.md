# 🚲 Bike Sharing Data Analysis & Dashboard

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan **Bike Sharing Dataset** yang mencakup periode tahun 2011–2012. Analisis dilakukan untuk memahami pola penggunaan sepeda berdasarkan waktu, kondisi cuaca, serta aktivitas harian pengguna.

Selain analisis menggunakan notebook, proyek ini juga dilengkapi dengan **dashboard interaktif menggunakan Streamlit** untuk memvisualisasikan hasil analisis secara lebih intuitif.

---

## 📂 Struktur Direktori

```
submission/
├── dashboard/
│   ├── dashboard.py
│   ├── day.csv
│   └── hour.csv
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt
```

---

## ❓ Pertanyaan Bisnis

1. Bagaimana tren jumlah penyewaan sepeda per bulan selama periode 2011-2012, dan pada bulan apa terjadi kenaikan atau penurunan terbesar berdasarkan perubahan jumlah penyewaan?
2. Bagaimana hubungan antara suhu, kelembaban, dan kondisi cuaca terhadap jumlah penyewaan sepeda selama periode 2011-2012?
3. Pada jam berapa terjadi puncak penyewaan sepeda dalam satu hari, dan bagaimana perbedaannya antara hari kerja dan hari libur?

---

## 🔍 Proses Analisis Data

### 1. Import Library

### 2. Data Wrangling

* Gathering data
* Assessing data
* Cleaning data:

  * Mengubah tipe data tanggal
  * Mapping kategori
  * Rename kolom
  * Drop kolom tidak penting
  * Feature engineering (day_category)

### 3. Exploratory Data Analysis (EDA)

* Analisis distribusi data
* Analisis korelasi antar variabel
* Analisis penyewaan berdasarkan kategori (season)

### 4. Visualization & Explanatory Analysis

* Visualisasi tren penyewaan per bulan
* Analisis hubungan antara cuaca dan penyewaan
* Analisis pola penyewaan berdasarkan jam

### 5. Analisis Lanjutan

* Clustering sederhana berbasis kategori suhu dan kelembaban untuk mengidentifikasi pola penyewaan pada berbagai kondisi lingkungan
* Kombinasi suhu hangat dan kelembaban sedang menghasilkan jumlah penyewaan tertinggi

---

## 📊 Insight Utama

* Penyewaan sepeda menunjukkan **pola musiman**, dengan peningkatan pada pertengahan tahun.
* **Suhu memiliki pengaruh positif** terhadap jumlah penyewaan sepeda.
* **Kelembaban dan kecepatan angin** cenderung menurunkan jumlah penyewaan.
* Puncak penyewaan terjadi pada **jam pagi dan sore hari**, terutama pada hari kerja.
* Kombinasi suhu hangat dan kelembaban sedang menghasilkan jumlah penyewaan tertinggi
---

## 🚀 Cara Menjalankan Dashboard

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Jalankan Dashboard

Masuk ke folder dashboard:

```
cd dashboard
streamlit run dashboard.py
```

### 3. Akses Dashboard

Buka browser di:

```
http://localhost:8501
```

---

## 🛠️ Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit

---

## 📁 Dataset

Dataset yang digunakan adalah Bike Sharing Dataset yang berisi data penyewaan sepeda di Washington D.C. tahun 2011–2012, yang mencakup informasi waktu, kondisi cuaca, dan jumlah penyewaan.

Dataset terdiri dari dua file utama:
* day.csv → data agregasi penyewaan sepeda per hari
* hour.csv → data agregasi penyewaan sepeda per jam

---

## 👩‍💻 Author

**Novia Djoend Lestari_CDCC284D6X2740**

---

## 📌 Catatan

Proyek ini dibuat sebagai bagian dari submission analisis data dan bertujuan untuk memberikan insight berdasarkan data historis penyewaan sepeda.
