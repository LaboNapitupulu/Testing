import streamlit as st
import pandas as pd
import plotly.express as px

# Bagian 1: Judul Aplikasi
st.title("Penerapan Data Sains: Visualisasi dan Statistik")

# Bagian 2: Penjelasan Data Sains
st.header("Apa itu Data Sains?")
st.write("""
Data sains adalah bidang multidisiplin yang bertujuan untuk mengekstraksi wawasan dari data. 
Beberapa topik penting dalam data sains meliputi Machine Learning, Data Mining, Artificial Intelligence, 
Data Visualization, dan Big Data. Berikut ini adalah contoh visualisasi dari data terkait pengguna internet di berbagai negara.
""")

# Bagian 3: Tabel dan Grafik Distribusi Artikel Ilmiah Berdasarkan Topik Data Sains
st.subheader("Tabel dan Grafik Distribusi Artikel Ilmiah Berdasarkan Topik Data Sains")

# Dataset distribusi artikel per topik
data_artikel = {
    'Topik': ['Machine Learning', 'Data Mining', 'Artificial Intelligence', 'Data Visualization', 'Big Data'],
    'Jumlah Artikel': [120, 80, 100, 50, 90]
}

# Membuat DataFrame untuk artikel ilmiah
df_artikel = pd.DataFrame(data_artikel)

# Menampilkan tabel distribusi artikel
st.write("Berikut adalah jumlah artikel ilmiah terkait setiap topik data sains:")
st.dataframe(df_artikel)

# Menggunakan Streamlit's built-in bar chart untuk distribusi artikel
st.bar_chart(df_artikel.set_index('Topik'))

# Penjelasan grafik
st.write("""
Grafik di atas menunjukkan distribusi artikel ilmiah berdasarkan topik utama dalam data sains.
Machine Learning dan Artificial Intelligence merupakan topik yang paling banyak diteliti dalam beberapa tahun terakhir.
""")

# Bagian 4: Menyematkan Video YouTube
st.subheader("Video Penjelasan tentang Data Sains")
video_url = "https://youtu.be/wq-O8byTAF0"
st.video(video_url)

# Penjelasan tentang video
st.write("Video ini menjelaskan dasar-dasar tentang data sains. Jika kamu ingin mendownload video ini, klik tombol di bawah.")

# Tombol untuk download video
download_url = "https://drive.google.com/file/d/12JhS_ct2DTdhYZ3ENl-3JYdbfNpn1dlD/view?usp=sharing
if st.button('Download Video'):
    st.markdown(f"[Klik di sini untuk download video](https://drive.google.com/file/d/12JhS_ct2DTdhYZ3ENl-3JYdbfNpn1dlD/view?usp=sharing)")

# Bagian 5: Contoh Visualisasi Data
st.header("Contoh Visualisasi Data")

# Bagian 6: Visualisasi Data Pengguna Internet di Dunia
st.subheader("Pengguna Internet di Dunia")

# Dataset Pengguna Internet di 25 negara
data_internet = {
    'Negara': [
        'United States', 'Indonesia', 'India', 'Brazil', 'China', 
        'Germany', 'United Kingdom', 'France', 'Japan', 'Russia',
        'South Africa', 'Australia', 'Canada', 'Mexico', 'Italy', 
        'South Korea', 'Spain', 'Turkey', 'Argentina', 'Nigeria', 
        'Netherlands', 'Saudi Arabia', 'Taiwan', 'Sweden', 'Norway'
    ],
    'Pengguna Internet (%)': [
        89, 64, 50, 75, 60, 
        91, 94, 93, 92, 78, 
        62, 89, 88, 70, 82, 
        85, 83, 79, 76, 71, 
        67, 64, 66, 90, 88
    ]
}

# Membuat DataFrame
df_internet = pd.DataFrame(data_internet)

# Menampilkan tabel data pengguna internet
st.write("Berikut adalah persentase pengguna internet di berbagai negara:")
st.dataframe(df_internet)

# Membuat peta interaktif dengan Plotly
fig = px.choropleth(
    df_internet, 
    locations='Negara', 
    locationmode='country names',
    color='Pengguna Internet (%)', 
    hover_name='Negara',
    title="Pengguna Internet di Dunia Berdasarkan Negara",
    color_continuous_scale="Blues"
)

# Menampilkan peta di Streamlit
st.plotly_chart(fig)

# Penjelasan tambahan
st.write("""
Peta di atas menunjukkan persentase pengguna internet di berbagai negara. 
Negara dengan pengguna internet terbanyak adalah Amerika Serikat, diikuti oleh Indonesia dan India.
""")

# Bagian 7: Analisis Data COVID-19
st.subheader("Analisis Kasus COVID-19")

# Dataset kasus COVID-19 (contoh)
data_covid = {
    'Tanggal': pd.date_range(start='2020-01-01', periods=10, freq='M'),
    'Kasus Harian': [100, 150, 200, 180, 160, 120, 130, 140, 170, 190]
}

# Membuat DataFrame untuk kasus COVID-19
df_covid = pd.DataFrame(data_covid)

# Menampilkan tabel kasus harian
st.write("Berikut adalah data kasus harian COVID-19:")
st.dataframe(df_covid)

# Membuat grafik garis untuk kasus COVID-19
fig_covid = px.line(df_covid, x='Tanggal', y='Kasus Harian', title='Tren Kasus COVID-19 Harian')

# Menampilkan grafik di Streamlit
st.plotly_chart(fig_covid)

# Penjelasan tambahan
st.write("""
Grafik di atas menunjukkan tren kenaikan dan penurunan kasus COVID-19 selama periode waktu tertentu.
""")

# Sumber Data
st.write("""
Sumber Data:
1. **Topik Data Sains (Jumlah Artikel)**: Data diambil dari [Google Scholar](https://scholar.google.com/) atau [arXiv](https://arxiv.org/).
2. **Pengguna Internet di Dunia**: Data diambil dari [Internet World Stats](https://www.internetworldstats.com/) atau [Statista](https://www.statista.com/).
3. **Analisis Kasus COVID-19**: Data diambil dari [World Health Organization (WHO)](https://www.who.int/) atau [Our World in Data](https://ourworldindata.org/coronavirus).
""")
