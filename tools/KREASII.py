import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur tampilan seaborn
sns.set(style="whitegrid")

# Judul Aplikasi
st.title("Analisis Jam Kerja Peserta Magang CEO HMSD 2024")

# 1. Import Data
data_url = "https://raw.githubusercontent.com/LaboNapitupulu/File/main/Pendataan_Peserta_Magang_CEO_HMSD_2024.csv"
df = pd.read_csv(data_url)

# Tampilkan Data Mentah
st.subheader("Data Mentah")
st.write(df.head())

# 2. Data Cleaning
st.subheader("Data Cleaning")
df['9. Jam Kerja Magang/Minggu (dalam jam)'] = df['9. Jam Kerja Magang/Minggu (dalam jam)'].replace('Belum ada sejauh ini', '0 jam')
df['Jam Kerja per Minggu'] = df['9. Jam Kerja Magang/Minggu (dalam jam)'].str.extract(r'(\d+[,\.]?\d*)')[0].str.replace(',', '.').astype(float)
st.write("Data setelah pembersihan:")
st.write(df[['Nama Lengkap', 'NIM', '2. Divisi Magang', 'Jam Kerja per Minggu']].head())

# 3. Analisis Statistik Deskriptif
st.subheader("Analisis Statistik Deskriptif")
st.write(df['Jam Kerja per Minggu'].describe())

# 4. Visualisasi Data
st.subheader("Visualisasi Data")

# Histogram Jam Kerja per Minggu
st.write("Histogram dari Jam Kerja per Minggu")
plt.figure(figsize=(10, 6))
sns.histplot(df['Jam Kerja per Minggu'], bins=10, kde=True, color="#5600f5", edgecolor='black')
plt.title('Distribusi Jam Kerja per Minggu')
plt.xlabel('Jam Kerja per Minggu')
plt.ylabel('Frekuensi')
st.pyplot(plt)

# Boxplot Jam Kerja per Minggu
st.write("Boxplot dari Jam Kerja per Minggu")
plt.figure(figsize=(8, 5))
sns.boxplot(y=df['Jam Kerja per Minggu'], color="#5600f5")
plt.title('Boxplot Jam Kerja per Minggu')
plt.ylabel('Jam Kerja per Minggu')
st.pyplot(plt)

# Standarisasi nama divisi untuk menghindari duplikasi
df['Divisi Magang Standard'] = df['2. Divisi Magang'].str.lower().str.strip()

# Bar Plot rata-rata jam kerja per minggu berdasarkan divisi
st.write("Rata-rata Jam Kerja per Minggu Berdasarkan Divisi Magang")
avg_hours_per_division = df.groupby('Divisi Magang Standard')['Jam Kerja per Minggu'].mean().reset_index()
plt.figure(figsize=(10, 12))
sns.barplot(data=avg_hours_per_division, x='Jam Kerja per Minggu', y='Divisi Magang Standard', palette="viridis")
plt.title('Rata-rata Jam Kerja per Minggu Berdasarkan Divisi Magang (Unik dan Distandarisasi)')
plt.xlabel('Rata-rata Jam Kerja per Minggu')
plt.ylabel('Divisi Magang')
st.pyplot(plt)

# Density Plot Jam Kerja per Minggu
st.write("Density Plot dari Jam Kerja per Minggu")
valid_data = df['Jam Kerja per Minggu'].dropna()
plt.figure(figsize=(10, 6))
sns.kdeplot(valid_data, shade=True, color="blue")
plt.title('Density Plot of Jam Kerja per Minggu')
plt.xlabel('Jam Kerja per Minggu')
plt.ylabel('Density')
st.pyplot(plt)
