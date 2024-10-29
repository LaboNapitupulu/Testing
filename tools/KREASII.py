import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import requests
from io import BytesIO

# URL mentah file Excel di GitHub
url = 'https://raw.githubusercontent.com/LaboNapitupulu/File/main/HasilWWC.xlsx'

# Menampilkan pesan status awal
st.title("Analisis Data Magang CEO HMSD 2024")
st.write("Mengunduh file data dari GitHub...")

try:
    # Mengunduh file dari GitHub
    response = requests.get(url)
    response.raise_for_status()
    st.write("File berhasil diunduh!")
except Exception as e:
    st.write("Error saat mengunduh file:", e)

# Membaca data dari file Excel yang diunduh
try:
    data_lembar = pd.read_excel(BytesIO(response.content), sheet_name='Sheeet 1')
    st.write("File berhasil dibaca!")
    st.write("Data Preview:", data_lembar())  # Menampilkan 5 baris pertama sebagai preview
except Exception as e:
    st.write("Error saat membaca file:", e)

# Visualisasi distribusi kategori diterima
def plot_distribusi_diterima(data):
    st.write("Memulai visualisasi distribusi departemen diterima...")  # Pesan status

    jumlah_diterima = data['DITERIMA'].value_counts()
    
    # Plot dengan Matplotlib
    plt.figure(figsize=(10, 6))
    sns.countplot(y='DITERIMA', data=data, order=jumlah_diterima.index)
    plt.title('Distribusi Departemen yang Diterima')
    plt.xlabel('Jumlah Peserta')
    plt.ylabel('Departemen')
    st.pyplot(plt)  # Menampilkan dengan Streamlit

    st.write("Visualisasi menggunakan Plotly...")  # Pesan status

    # Plot interaktif dengan Plotly
    fig = px.bar(jumlah_diterima, x=jumlah_diterima.values, y=jumlah_diterima.index,
                 orientation='h', title='Distribusi Departemen yang Diterima')
    fig.update_layout(xaxis_title='Jumlah Peserta', yaxis_title='Departemen')
    st.plotly_chart(fig)  # Menampilkan dengan Streamlit

# Menampilkan konten di Streamlit
st.write("Menampilkan visualisasi...")
plot_distribusi_diterima(data_lembar)
st.write("Visualisasi selesai!")
