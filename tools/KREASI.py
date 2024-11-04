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
Aplikasi ini menganalisis data jam kerja peserta magang untuk memberikan wawasan mengenai pola kerja mereka di berbagai divisi.
Analisis ini dapat membantu manajemen dalam memahami alokasi waktu kerja peserta di setiap divisi.
""")

# 1. Import Data
st.subheader("1. Import Data")
st.write("Data diambil langsung dari file CSV yang berisi informasi mengenai peserta magang, termasuk divisi dan jam kerja mingguan.")
data_url = "https://raw.githubusercontent.com/LaboNapitupulu/File/main/Pendataan_Peserta_Magang_CEO_HMSD_2024.csv"
df = pd.read_csv(data_url)

# Menampilkan semua data yang diambil dari file CSV
st.write(df)

# Penjelasan Dataset
st.subheader("Penjelasan Dataset")
st.write(f"""
Dataset ini terdiri dari {df.shape[0]} baris (objek) dan {df.shape[1]} kolom (atribut). Berikut adalah deskripsi dari masing-masing kolom dalam dataset ini:
- **Nama Lengkap**: Nama lengkap dari peserta magang.
- **NIM**: Nomor Induk Mahasiswa, dikonversi menjadi string untuk menghindari tampilan koma.
- **Divisi Magang**: Divisi tempat peserta magang bekerja.
- **Jam Kerja Magang/Minggu (dalam jam)**: Kolom yang mencatat jumlah jam kerja mingguan dari setiap peserta. Data ini memerlukan pembersihan sebelum dianalisis.
""")

# 2. Data Cleaning (Pembersihan Data)
st.subheader("2. Pembersihan Data")
st.write("""
Pada kolom "Jam Kerja Magang/Minggu (dalam jam)", beberapa entri memiliki teks "Belum ada sejauh ini".
Langkah ini mengganti teks tersebut dengan "0 jam" agar dapat diproses.
Kami kemudian mengekstrak angka dari kolom tersebut dan mengonversinya menjadi format numerik untuk keperluan analisis lebih lanjut.
Selain itu, kolom NIM dikonversi menjadi string untuk menghindari tampilan dengan koma.
""")
# Konversi NIM menjadi string untuk menghindari tampilan dengan koma
df['NIM'] = df['NIM'].astype(str)

# Pembersihan data jam kerja
df['9. Jam Kerja Magang/Minggu (dalam jam)'] = df['9. Jam Kerja Magang/Minggu (dalam jam)'].replace('Belum ada sejauh ini', '0 jam')
df['Jam Kerja per Minggu'] = df['9. Jam Kerja Magang/Minggu (dalam jam)'].str.extract(r'(\d+[,\.]?\d*)')[0].str.replace(',', '.').astype(float)
st.write(df[['Nama Lengkap', 'NIM', '2. Divisi Magang', 'Jam Kerja per Minggu']])

# 3. Analisis Statistik Deskriptif
st.subheader("3. Analisis Statistik Deskriptif")
st.write("""
Analisis statistik deskriptif memberikan gambaran mengenai distribusi jam kerja, termasuk rata-rata, standar deviasi, 
nilai minimum dan maksimum, serta kuartil. Ini membantu kita memahami rentang jam kerja serta variasi antar peserta.
""")
st.write(df['Jam Kerja per Minggu'].describe())

# 4. Visualisasi Data
st.subheader("4. Visualisasi Data")

# Histogram untuk kolom "Jam Kerja per Minggu"
st.write("""
**Histogram Jam Kerja per Minggu**: Histogram ini menunjukkan distribusi frekuensi dari jam kerja peserta magang. 
Setiap batang menunjukkan jumlah peserta yang memiliki jam kerja dalam kisaran tertentu, dengan garis distribusi kepadatan untuk memperjelas pola distribusi secara umum.
""")
plt.figure(figsize=(10, 6))
sns.histplot(df['Jam Kerja per Minggu'], bins=10, kde=True, color="#5600f5", edgecolor='black')
plt.title('Distribusi Jam Kerja per Minggu')
plt.xlabel('Jam Kerja per Minggu')
plt.ylabel('Frekuensi')
st.pyplot(plt)

# Boxplot untuk kolom "Jam Kerja per Minggu"
st.write("""
**Boxplot Jam Kerja per Minggu**: Boxplot ini menunjukkan distribusi rentang jam kerja, termasuk nilai ekstrem (outlier).
Rentang utama data ditunjukkan dengan box, sementara titik di luar box adalah outlier.
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
**Rata-rata Jam Kerja per Minggu Berdasarkan Divisi**: Setelah standarisasi nama divisi, 
rata-rata jam kerja dihitung untuk setiap divisi. Grafik ini memudahkan kita membandingkan beban kerja antara divisi-divisi yang berbeda.
Divisi dengan rata-rata lebih tinggi mungkin menunjukkan beban kerja yang lebih besar.
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
**Density Plot Jam Kerja per Minggu**: Density plot ini menunjukkan kepadatan data pada berbagai rentang nilai jam kerja.
Bagian puncak menunjukkan kisaran jam kerja yang paling banyak ditempati oleh peserta, memberi gambaran umum pola distribusi data.
""")
valid_data = df['Jam Kerja per Minggu'].dropna()
plt.figure(figsize=(10, 6))
sns.kdeplot(valid_data, shade=True, color="blue")
plt.title('Density Plot of Jam Kerja per Minggu')
plt.xlabel('Jam Kerja per Minggu')
plt.ylabel('Density')
st.pyplot(plt)
