import streamlit as st
import pandas as pd
import plotly.express as px

# Bagian 1: Judul Aplikasi
st.title("Penerapan Data Sains: Visualisasi dan Statistik")

# Bagian 2: Penjelasan Data Sains
st.header("Apa itu Data Sains?")
st.write("""
Data sains adalah bidang multidisiplin yang bertujuan untuk mengekstraksi wawasan dari data. 
Berikut ini adalah contoh visualisasi dari data terkait topik utama dalam data sains, seperti Machine Learning, 
Data Mining, dan lainnya. Grafik di bawah ini menggambarkan distribusi artikel ilmiah berdasarkan topik dalam bidang data sains.
""")

# Bagian 3: Tabel Dataset dan Statistik
st.subheader("Tabel Distribusi Artikel Data Sains")

# Dataset distribusi artikel per topik
data = {
    'Topik': ['Machine Learning', 'Data Mining', 'Artificial Intelligence', 'Data Visualization', 'Big Data'],
    'Jumlah Artikel': [120, 80, 100, 50, 90]
}

# Membuat DataFrame menggunakan pandas
df = pd.DataFrame(data)

# Menampilkan tabel distribusi artikel
st.write("Berikut adalah jumlah artikel ilmiah terkait setiap topik data sains:")
st.dataframe(df)

# Bagian 4: Grafik Interaktif dengan Plotly
st.subheader("Grafik Distribusi Artikel Ilmiah Berdasarkan Topik")

# Membuat grafik bar chart interaktif
fig = px.bar(df, x='Topik', y='Jumlah Artikel', 
             title="Distribusi Artikel Ilmiah Berdasarkan Topik Data Sains",
             labels={'Jumlah Artikel': 'Jumlah Artikel (Unit)', 'Topik': 'Topik Data Sains'})

# Menampilkan grafik interaktif di Streamlit
st.plotly_chart(fig)

# Bagian 5: Penjelasan Grafik
st.write("""
Grafik di atas menunjukkan distribusi artikel ilmiah berdasarkan topik utama dalam data sains. 
Ini adalah salah satu cara visualisasi yang dapat membantu kita memahami data dengan lebih baik. 
Contoh visualisasi ini menggunakan **Plotly**, sebuah library populer untuk visualisasi data interaktif.
""")

# Bagian 6: Menyematkan Video YouTube (Tambahan)
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
