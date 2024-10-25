import streamlit as st
import pandas as pd
from PIL import Image

# Bagian 1: Judul Aplikasi
st.title("Penerapan Data Sains: Visualisasi dan Statistik")

# Bagian 2: Penjelasan Data Sains
st.header("Apa itu Data Sains?")
st.write("""
Data sains adalah bidang multidisiplin yang bertujuan untuk mengekstraksi wawasan dari data. 
Beberapa topik penting dalam data sains meliputi Machine Learning, Data Mining, Artificial Intelligence, 
Data Visualization, dan Big Data. Berikut ini adalah contoh visualisasi dari data terkait pengguna internet di Indonesia.
""")

# Bagian 6: Tabel Dataset dan Grafik Distribusi Artikel Data Sains
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

# Bagian 7: Menyematkan Video YouTube
st.subheader("Video Penjelasan tentang Data Sains")

# Link video YouTube
video_url = "https://youtu.be/wq-O8byTAF0"
st.video(video_url)

# Penjelasan tentang video
st.write("Video ini menjelaskan dasar-dasar tentang data sains. Jika kamu ingin mendownload video ini, klik tombol di bawah.")

# Tombol untuk download video
download_url = "https://www.y2mate.com/youtube/wq-O8byTAF0"
if st.button('Download Video'):
    st.markdown(f"[Klik di sini untuk download video](https://www.y2mate.com/youtube/wq-O8byTAF0)")
