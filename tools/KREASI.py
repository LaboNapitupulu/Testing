import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur tampilan grafik dengan tema 'whitegrid' dari seaborn
sns.set(style="whitegrid")

# Judul Aplikasi
st.title("Analisis Jam Kerja Peserta Magang CEO HMSD 2024")
st.write("""
Selamat datang di aplikasi analisis data jam kerja peserta magang CEO HMSD 2024.
Aplikasi ini memberikan wawasan mengenai pola jam kerja para peserta magang di berbagai divisi.
Melalui beberapa visualisasi interaktif, Anda dapat melihat distribusi jam kerja, perbandingan antar divisi, dan pola kerja peserta magang dengan lebih mudah.
""")

# 1. Import Data
st.subheader("1. Import Data")
st.write("Data diambil langsung dari file CSV yang berisi informasi mengenai peserta magang, termasuk divisi dan jam kerja mingguan.")
data_url = "https://raw.githubusercontent.com/LaboNapitupulu/File/main/Pendataan_Peserta_Magang_CEO_HMSD_2024.csv"
df = pd.read_csv(data_url)

# Menampilkan semua data yang diambil dari file CSV
st.write("### Data Lengkap")
st.write("Berikut adalah data lengkap peserta magang yang kami gunakan untuk analisis:")
st.write(df)

# 2. Pembersihan Data
st.subheader("2. Pembersihan Data")
st.write("""
Pada tahap ini, kami melakukan pembersihan data agar informasi lebih akurat.
Beberapa data di kolom "Jam Kerja Magang/Minggu (dalam jam)" berisi teks "Belum ada sejauh ini". 
Kami mengganti teks tersebut dengan nilai "0 jam" sehingga data lebih mudah dianalisis.
Selain itu, kami mengonversi kolom NIM ke bentuk teks untuk menghindari tampilan dengan koma yang dapat menyebabkan kebingungan.
""")
df['NIM'] = df['NIM'].astype(str)
df['9. Jam Kerja Magang/Minggu (dalam jam)'] = df['9. Jam Kerja Magang/Minggu (dalam jam)'].replace('Belum ada sejauh ini', '0 jam')
df['Jam Kerja per Minggu'] = df['9. Jam Kerja Magang/Minggu (dalam jam)'].str.extract(r'(\d+[,\.]?\d*)')[0].str.replace(',', '.').astype(float)
st.write(df[['Nama Lengkap', 'NIM', '2. Divisi Magang', 'Jam Kerja per Minggu']])

# 3. Analisis Statistik Deskriptif
st.subheader("3. Analisis Statistik Deskriptif")
st.write("""
Analisis statistik ini memberikan gambaran umum mengenai distribusi jam kerja peserta magang. 
Berikut ini beberapa hal yang ditunjukkan:
- **Rata-rata (Mean)**: Nilai rata-rata jam kerja per minggu di seluruh peserta.
- **Standar Deviasi**: Mengukur seberapa besar variasi jam kerja antar peserta; semakin besar nilainya, semakin bervariasi jam kerja peserta.
- **Nilai Minimum dan Maksimum**: Menunjukkan peserta dengan jam kerja terendah dan tertinggi.
- **Kuartil**: Kuartil pertama (Q1) menunjukkan batas bawah 25% jam kerja terendah, median (Q2) menunjukkan titik tengah, dan kuartil ketiga (Q3) menunjukkan batas atas 25% jam kerja tertinggi.
""")
st.write(df['Jam Kerja per Minggu'].describe())

# 4. Visualisasi Data
st.subheader("4. Visualisasi Data")

# Histogram untuk kolom "Jam Kerja per Minggu"
st.write("""
**Distribusi Frekuensi Jam Kerja per Minggu**
- Histogram di bawah ini menunjukkan berapa banyak peserta yang bekerja dalam kisaran jam kerja tertentu setiap minggu.
- Sumbu horizontal (x-axis) menampilkan rentang jam kerja per minggu, sedangkan sumbu vertikal (y-axis) menunjukkan jumlah peserta dalam setiap rentang tersebut.
- Garis distribusi (kde) menambahkan visualisasi yang lebih halus mengenai pola distribusi, menunjukkan puncak dan pola umum.
- Contoh interpretasi: jika grafik menunjukkan satu puncak besar, artinya sebagian besar peserta bekerja dalam kisaran jam tersebut.
""")
plt.figure(figsize=(10, 6))
sns.histplot(df['Jam Kerja per Minggu'], bins=10, kde=True, color="#5600f5", edgecolor='black')
plt.title('Distribusi Jam Kerja per Minggu')
plt.xlabel('Jam Kerja per Minggu')
plt.ylabel('Frekuensi')
st.pyplot(plt)

# Boxplot untuk kolom "Jam Kerja per Minggu"
st.write("""
**Boxplot Distribusi Jam Kerja per Minggu**
- Boxplot di bawah ini memberikan informasi mengenai rentang jam kerja peserta dan menunjukkan nilai ekstrem (outliers).
- Bagian dalam box menampilkan 50% data di antara kuartil pertama (Q1) dan kuartil ketiga (Q3), sementara garis tengah adalah median atau nilai tengah.
- Titik-titik di luar box adalah outliers, yang mengindikasikan peserta dengan jam kerja yang jauh lebih tinggi atau lebih rendah dari peserta lainnya.
- Boxplot membantu mengidentifikasi variasi dan apakah ada peserta yang jam kerjanya sangat berbeda dari yang lain.
""")
plt.figure(figsize=(8, 5))
sns.boxplot(y=df['Jam Kerja per Minggu'], color="#5600f5")
plt.title('Boxplot Jam Kerja per Minggu')
plt.ylabel('Jam Kerja per Minggu')
st.pyplot(plt)

# Standarisasi nama divisi untuk menghindari duplikasi
df['Divisi Magang Standard'] = df['2. Divisi Magang'].str.lower().str.strip()

# Bar Plot rata-rata jam kerja per minggu berdasarkan divisi
st.write("""
**Rata-rata Jam Kerja per Minggu Berdasarkan Divisi**
- Grafik batang di bawah ini menunjukkan rata-rata jam kerja per minggu di setiap divisi magang setelah standarisasi nama divisi.
- Setiap batang menunjukkan jam kerja rata-rata pada divisi tersebut, sehingga kita dapat melihat divisi mana yang memiliki beban kerja lebih tinggi atau lebih rendah.
- Interpretasi: Divisi dengan rata-rata lebih tinggi mungkin memiliki tugas lebih banyak atau kompleks, sedangkan divisi dengan rata-rata lebih rendah mungkin memiliki jadwal yang lebih fleksibel atau tugas lebih sedikit.
""")
avg_hours_per_division = df.groupby('Divisi Magang Standard')['Jam Kerja per Minggu'].mean().reset_index()
plt.figure(figsize=(10, 12))
sns.barplot(data=avg_hours_per_division, x='Jam Kerja per Minggu', y='Divisi Magang Standard', palette="viridis")
plt.title('Rata-rata Jam Kerja per Minggu Berdasarkan Divisi Magang (Unik dan Distandarisasi)')
plt.xlabel('Rata-rata Jam Kerja per Minggu')
plt.ylabel('Divisi Magang')
st.pyplot(plt)

# Density Plot untuk kolom "Jam Kerja per Minggu"
st.write("""
**Kepadatan Distribusi Jam Kerja per Minggu**
- Density plot di bawah ini memberikan tampilan yang lebih halus dari distribusi data, menampilkan kepadatan jam kerja per minggu.
- Puncak (peak) dalam density plot menunjukkan rentang jam kerja yang paling sering ditempati oleh peserta magang.
- Density plot ini bermanfaat untuk melihat pola distribusi jam kerja, apakah cenderung berkumpul pada satu nilai atau tersebar dalam beberapa rentang yang berbeda.
""")
valid_data = df['Jam Kerja per Minggu'].dropna()
plt.figure(figsize=(10, 6))
sns.kdeplot(valid_data, shade=True, color="blue")
plt.title('Density Plot of Jam Kerja per Minggu')
plt.xlabel('Jam Kerja per Minggu')
plt.ylabel('Density')
st.pyplot(plt)
