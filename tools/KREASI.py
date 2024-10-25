import streamlit as st
import pandas as pd
from PIL import Image

# Bagian 1: Judul Aplikasi
st.title("Pengenalan Data Sains")

# Bagian 2: Penjelasan Interaktif tentang Data Sains
st.header("Apa itu Data Sains?")
st.write("""
Data sains adalah bidang studi yang menggunakan metode ilmiah, proses, algoritma, dan sistem untuk mengekstraksi pengetahuan dan wawasan dari data dalam berbagai bentuk, baik terstruktur maupun tidak terstruktur.
Data sains adalah lanjutan dari beberapa bidang ilmu seperti data mining, machine learning, dan big data.

Berikut adalah beberapa konsep dasar dalam data sains:
- **Machine Learning**: Teknik yang memungkinkan komputer untuk belajar dari data.
- **Data Mining**: Proses mencari pola dari sejumlah besar data.
- **Artificial Intelligence**: Pengembangan sistem yang mampu menjalankan tugas yang biasanya membutuhkan kecerdasan manusia.
- **Data Visualization**: Penyajian data dalam bentuk visual seperti grafik dan diagram.
- **Big Data**: Pengelolaan dan analisis data dalam skala besar.
""")

# Menambahkan gambar ilustrasi tentang Data Sains
image = Image.open("path_to_your_image/data_science.jpg")  # Ganti path dengan gambar relevan
st.image(image, caption="Ilustrasi Data Sains", use_column_width=True)

# Bagian 3: Dataset Interaktif
st.subheader("Tabel Topik Utama dalam Data Sains")

# Contoh dataset interaktif tentang topik data sains
data = {
    'Topik': ['Machine Learning', 'Data Mining', 'Artificial Intelligence', 'Data Visualization', 'Big Data'],
    'Deskripsi': [
        'Teknik yang memungkinkan komputer untuk belajar dari data.',
        'Proses mencari pola dari sejumlah besar data.',
        'Pengembangan sistem yang mampu menjalankan tugas yang biasanya membutuhkan kecerdasan manusia.',
        'Penyajian data dalam bentuk visual seperti grafik dan diagram.',
        'Pengelolaan dan analisis data dalam skala besar.'
    ],
    'Tingkat Kesulitan': ['Menengah', 'Sulit', 'Sulit', 'Mudah', 'Menengah']
}

# Membuat DataFrame menggunakan pandas
df = pd.DataFrame(data)

# Menampilkan tabel interaktif di Streamlit
st.write("Berikut ini adalah beberapa topik utama dalam data sains:")
st.dataframe(df)  # Tabel interaktif yang bisa disortir dan discroll

# Bagian 4: Menyematkan Video YouTube
st.subheader("Video Penjelasan tentang Data Sains")

# Link video YouTube
video_url = "https://youtu.be/wq-O8byTAF0"
st.video(video_url)

# Penjelasan tentang video
st.write("Video ini menjelaskan dasar-dasar tentang data sains. Jika kamu ingin mendownload video ini, klik tombol di bawah.")

# Bagian 5: Tombol Download Video
download_url = "https://www.y2mate.com/youtube/wq-O8byTAF0"

# Tombol untuk download video
if st.button('Download Video'):
    st.markdown(f"[Klik di sini untuk download video](https://www.y2mate.com/youtube/wq-O8byTAF0)")
