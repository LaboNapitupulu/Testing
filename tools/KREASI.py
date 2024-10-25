import streamlit as st
import pandas as pd

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

# Bagian 4: Grafik Bar Sederhana dengan Streamlit
st.subheader("Grafik Distribusi Artikel Ilmiah Berdasarkan Topik")

# Menggunakan bar chart bawaan dari Streamlit
st.bar_chart(df.set_index('Topik'))
