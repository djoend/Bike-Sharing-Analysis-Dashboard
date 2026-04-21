import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# ======================
# 🎨 PASTEL UI STYLE
# ======================
st.markdown("""
    <style>
    /* Background utama */
    .stApp {
        background-color: #FFF7F0;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #FDE2E4;
    }

    /* Card metric */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    /* Judul */
    h1, h2, h3 {
        color: #6D6875;
    }

    /* Text */
    p {
        color: #4A4A4A;
    }

    /* Button (kalau nanti dipakai) */
    button {
        background-color: #B5EAD7 !important;
        color: black !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

sns.set(style='whitegrid')

sns.set_palette([
    "#A0CED9",  # biru pastel
    "#FFB5A7",  # peach
    "#B5EAD7",  # mint
    "#CDB4DB",  # ungu pastel
    "#FFC8DD"   # pink pastel
])

# ======================
# LOAD DATA
# ======================
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# ======================
# DATA CLEANING
# ======================
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

day_df.rename(columns={
    'dteday': 'date',
    'yr': 'year',
    'mnth': 'month',
    'cnt': 'total_rentals'
}, inplace=True)

hour_df.rename(columns={
    'dteday': 'date',
    'yr': 'year',
    'mnth': 'month',
    'hr': 'hour',
    'cnt': 'total_rentals'
}, inplace=True)

day_df['year'] = day_df['year'].map({0: 2011, 1: 2012})
hour_df['year'] = hour_df['year'].map({0: 2011, 1: 2012})

hour_df['day_category'] = hour_df['workingday'].map({
    0: 'Weekend/Holiday',
    1: 'Working Day'
})

# ======================
# SIDEBAR MENU
# ======================
st.sidebar.title("📌 Menu")

page = st.sidebar.selectbox(
    "Pilih Halaman",
    ["Penjelasan Proyek", "Dashboard"]
)

# ======================
# 📄 HALAMAN 1
# ======================
if page == "Penjelasan Proyek":

    st.title("📄 Penjelasan Proyek")

    st.markdown("""
    ### 📊 Latar Belakang
    Bike sharing merupakan salah satu bentuk transportasi modern yang memungkinkan pengguna menyewa sepeda secara praktis tanpa proses yang rumit. Sistem ini banyak digunakan di berbagai kota karena dinilai lebih ramah lingkungan, fleksibel, dan efisien untuk mobilitas jarak pendek.
    Seiring dengan berkembangnya penggunaan bike sharing, data yang dihasilkan juga semakin besar dan beragam, seperti waktu penyewaan, kondisi cuaca, musim, hingga pola aktivitas pengguna. Data tersebut dapat dimanfaatkan untuk memahami perilaku pengguna serta faktor-faktor yang memengaruhi jumlah penyewaan sepeda.
    Melalui analisis data ini, diharapkan dapat diperoleh insight yang berguna untuk membantu pengelola sistem dalam meningkatkan layanan, mengoptimalkan ketersediaan sepeda, serta mendukung pengambilan keputusan berbasis data.
    Dalam proyek ini, digunakan Bike Sharing Dataset yang berisi data historis penyewaan sepeda di Washington D.C., Amerika Serikat selama tahun 2011-2012. Dataset ini telah diperkaya dengan informasi cuaca dan musim, sehingga memungkinkan analisis yang lebih mendalam terkait faktor-faktor yang memengaruhi jumlah penyewaan sepeda.
    
    ### 🎯 Tujuan
    Proyek ini bertujuan untuk menganalisis data penyewaan sepeda guna mendapatkan insight yang dapat membantu pengambilan keputusan. Adapun tujuan utamanya adalah:
                
    - Menganalisis tren penyewaan sepeda dari waktu ke waktu, khususnya per bulan selama periode 2011-2012
    - Mengetahui pengaruh faktor cuaca seperti suhu, kelembaban, dan kondisi cuaca terhadap jumlah penyewaan sepeda
    - Mengidentifikasi pola penggunaan sepeda berdasarkan jam dalam sehari, termasuk perbedaan antara hari kerja dan hari libur
    - Menyajikan hasil analisis dalam bentuk visualisasi yang mudah dipahami melalui dashboard interaktif menggunakan Streamlit
 
    ### 📁 Dataset
    Dataset yang digunakan adalah Bike Sharing Dataset yang terdiri dari dua file utama:
                
    - day.csv → data penyewaan sepeda per hari (731 data)
    - hour.csv → data penyewaan sepeda per jam (17.379 data)
                
    Dataset ini mencakup berbagai variabel penting, antara lain:
    - Informasi waktu: tanggal, bulan, tahun, jam
    - Kondisi lingkungan: suhu, kelembaban, kecepatan angin, kondisi cuaca
    - Kategori hari: hari kerja atau hari libur
    - Jumlah penyewaan: total, pengguna kasual, dan pengguna terdaftar
                
    Dengan kombinasi variabel tersebut, dataset ini memungkinkan analisis yang komprehensif terhadap pola penyewaan sepeda berdasarkan waktu dan kondisi lingkungan.

    ### ❓ Pertanyaan
    1. Bagaimana tren jumlah penyewaan sepeda per bulan selama periode 2011-2012, dan pada bulan apa terjadi kenaikan atau penurunan terbesar berdasarkan perubahan jumlah penyewaan?
    2. Bagaimana hubungan antara suhu, kelembaban, dan kondisi cuaca terhadap jumlah penyewaan sepeda selama periode 2011-2012?
    3. Pada jam berapa terjadi puncak penyewaan sepeda dalam satu hari, dan bagaimana perbedaannya antara hari kerja dan hari libur?

    """)

# ======================
# 📊 HALAMAN 2
# ======================
elif page == "Dashboard":

    st.title("🚲 Bike Sharing Dashboard")
    st.write("Analisis Penyewaan Sepeda Tahun 2011-2012")

    # ======================
    # FILTER
    # ======================
    st.sidebar.header("Filter")

    selected_year = st.sidebar.selectbox(
        "Pilih Tahun",
        options=sorted(day_df['year'].unique())
    )

    month_dict = {i: calendar.month_name[i] for i in range(1, 13)}

    selected_month = st.sidebar.selectbox(
        "Pilih Bulan",
        options=list(month_dict.keys()),
        format_func=lambda x: month_dict[x]
    )

    # ======================
    # FILTER DATA
    # ======================
    filtered_day = day_df[
        (day_df['year'] == selected_year) &
        (day_df['month'] == selected_month)
    ]

    filtered_hour = hour_df[
        (hour_df['year'] == selected_year) &
        (hour_df['month'] == selected_month)
    ]

    # ======================
    # METRICS
    # ======================
    st.subheader("📌 Ringkasan Data")

    col1, col2, col3 = st.columns(3)

    if not filtered_day.empty:
        col1.metric("Total Penyewaan", int(filtered_day['total_rentals'].sum()))
        col2.metric("Rata-rata Harian", int(filtered_day['total_rentals'].mean()))
        col3.metric("Maksimum Harian", int(filtered_day['total_rentals'].max()))
    else:
        st.warning("Data tidak tersedia untuk filter ini")

    # ======================
    # TREND 
    # ======================
    st.header("📈 Tren Penyewaan Sepeda per Bulan")

    monthly = day_df.groupby(['year','month'])['total_rentals'].sum().reset_index()
    monthly['month_name'] = monthly['month'].apply(lambda x: calendar.month_abbr[x])

    fig1, ax1 = plt.subplots(figsize=(10,5))
    sns.lineplot(
    data=monthly,
    x='month_name',
    y='total_rentals',
    hue='year',
    marker='o',
    linewidth=3,
    ax=ax1
)
    
    st.pyplot(fig1)

    # INSIGHT 
    st.write("""
    Insight:
    Terjadi peningkatan penyewaan pada pertengahan tahun dan penurunan pada awal serta akhir tahun.
    Tahun 2012 memiliki jumlah penyewaan yang lebih tinggi dibandingkan 2011.
    """)

    # ======================
    # 🌦️ CUACA 
    # ======================
    st.header("🌦️ Pengaruh Cuaca terhadap Penyewaan")

    if not filtered_day.empty:
        fig2, ax2 = plt.subplots()
        sns.scatterplot(
    data=filtered_day,
    x='temp',
    y='total_rentals',
    s=80,
    alpha=0.7,
    ax=ax2
)
        
        st.pyplot(fig2)

        fig3, ax3 = plt.subplots()
        sns.heatmap(filtered_day[['temp','hum','windspeed','total_rentals']].corr(),
                    annot=True, cmap='coolwarm', ax=ax3)
        st.pyplot(fig3)

        # INSIGHT 
        st.write("""
        Insight:
        Suhu memiliki hubungan positif terhadap jumlah penyewaan, sedangkan kelembaban dan angin cenderung negatif.
        """)

    # ======================
    # ⏰ JAM 
    # ======================
    st.header("⏰ Pola Penyewaan Berdasarkan Jam")

    if not filtered_hour.empty:
        hourly = filtered_hour.groupby(['hour','day_category'])['total_rentals'].mean().reset_index()

        fig4, ax4 = plt.subplots()
        sns.lineplot(
    data=hourly,
    x='hour',
    y='total_rentals',
    hue='day_category',
    marker='o',
    linewidth=3,
    ax=ax4
)
        
        st.pyplot(fig4)

        peak = hourly.loc[hourly['total_rentals'].idxmax()]
        st.success(f"🔥 Jam puncak: {int(peak['hour'])}:00 ({peak['day_category']})")

        # INSIGHT 
        st.write("""
        Insight:
        Hari kerja memiliki dua puncak (pagi & sore), sedangkan akhir pekan lebih merata di siang hari.
        """)

    # ======================
    # FOOTER
    # ======================
    st.caption("© 2026 Bike Sharing Analysis by Novia Djoend Lestari_CDCC284D6X2740")