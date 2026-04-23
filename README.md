# 🚲 Bike Sharing Data Analysis & Dashboard

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan Bike Sharing Dataset periode tahun 2011–2012. Analisis dilakukan untuk memahami pola penggunaan sepeda berdasarkan waktu, kondisi cuaca, serta aktivitas pengguna.

Hasil analisis kemudian disajikan dalam bentuk dashboard interaktif menggunakan Streamlit, sehingga pengguna dapat mengeksplorasi data secara dinamis melalui filter tahun dan bulan.

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

Dashboard interaktif menampilkan:
- Filter berdasarkan tahun dan bulan
- Ringkasan metrik:
  - Total penyewaan
  - Rata-rata harian
  - Maksimum harian
- Visualisasi:
  - Tren penyewaan per bulan
  - Scatter plot suhu vs penyewaan
  - Heatmap korelasi
  - Pola penyewaan per jam (working day vs weekend)

### 5. Analisis Lanjutan

Dilakukan clustering sederhana berbasis kategori:
- Kategori suhu: Low, Medium, High
- Kategori kelembaban: Low, Medium, High
Kemudian dianalisis rata-rata penyewaan untuk setiap kombinasi kategori menggunakan barplot.

---

## 📊 Insight Utama

* Penyewaan sepeda menunjukkan pola musiman, meningkat pada pertengahan tahun.
* Tahun 2012 memiliki jumlah penyewaan lebih tinggi dibandingkan 2011.
* Suhu berpengaruh positif terhadap jumlah penyewaan.
* Kelembaban dan kecepatan angin cenderung berpengaruh negatif.
* Pada hari kerja, puncak terjadi di pagi dan sore hari (jam berangkat & pulang kerja).
* Pada akhir pekan, penyewaan lebih merata dan cenderung tinggi di siang hari.
* Kombinasi optimal:
  Suhu tinggi + kelembaban rendah/medium → penyewaan tertinggi
---

## 🚀 Cara Menjalankan Dashboard

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Masuk ke Folder Dashboard

cd dashboard

### 3. Masuk ke Folder Dashboard

streamlit run dashboard.py

### 4. Akses Browser


http://localhost:8501

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
