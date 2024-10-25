import streamlit as st
import pandas as pd
import plotly.express as px

# Judul aplikasi
st.title("Pengenalan Sains Data")

# Deskripsi Singkat
st.write("""
Sains data adalah bidang interdisipliner yang menggunakan metode, algoritma, dan sistem ilmiah untuk mengekstrak wawasan dari data dalam berbagai bentuk, baik terstruktur maupun tidak terstruktur. 
Ini adalah bidang yang berkembang pesat dan sangat penting dalam pengambilan keputusan berbasis data di banyak sektor industri.
""")

# Menyertakan Video Pengenalan Sains Data
st.subheader("Video Pengenalan Sains Data")
video_url = "https://www.youtube.com/watch?v=wq-O8byTAF0"  # Ganti dengan URL video yang relevan
st.video(video_url)

# Tabel Interaktif
st.subheader("Tabel Statistik Sains Data")

# Contoh dataset statistik sains data
data_statistik = {
    'Aspek': ['Jumlah Pengguna Internet (juta)', 'Volume Data Global (Zettabytes)', 'Data yang Diproses Per Tahun (Exabytes)'],
    'Nilai': [5000, 59, 44]  # Ganti dengan data yang relevan
}

# Membuat DataFrame
df_statistik = pd.DataFrame(data_statistik)

# Menampilkan tabel interaktif
st.dataframe(df_statistik)

# Visualisasi Data
st.subheader("Visualisasi Pertumbuhan Pengguna Internet di Dunia")

# Contoh data pengguna internet
data_internet = {
    'Tahun': [2015, 2016, 2017, 2018, 2019, 2020],
    'Pengguna (juta)': [3200, 3600, 3900, 4200, 4600, 5000]
}

# Membuat DataFrame
df_internet = pd.DataFrame(data_internet)

# Membuat grafik garis
fig = px.line(df_internet, x='Tahun', y='Pengguna (juta)', title='Pertumbuhan Pengguna Internet di Dunia')

# Menampilkan grafik di Streamlit
st.plotly_chart(fig)

# Penjelasan tambahan
st.write("""
Grafik di atas menunjukkan pertumbuhan jumlah pengguna internet di seluruh dunia dari tahun 2015 hingga 2020.
Penggunaan internet terus meningkat seiring dengan perkembangan teknologi dan aksesibilitas data.
""")
