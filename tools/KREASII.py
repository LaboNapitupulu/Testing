import pandas as pd
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio

# Konfigurasi plotly untuk tampilan interaktif
pio.renderers.default = 'notebook'

# URL mentah file Excel di GitHub
url = 'https://raw.githubusercontent.com/LaboNapitupulu/File/main/HasilWWC.xlsx'

# Mengunduh file dari GitHub
response = requests.get(url)
response.raise_for_status()  # Memastikan unduhan berhasil

# Membaca data dari file Excel yang diunduh
data_lembar = pd.read_excel(BytesIO(response.content), sheet_name='Sheeet 1')

# 1. Analisis Deskriptif
# Menampilkan statistik deskriptif untuk data kategori
def tampilkan_statistik_deskriptif(data):
    print("Statistik Deskriptif:\n")
    statistik_deskriptif = data.describe(include='all')
    print(statistik_deskriptif)
    return statistik_deskriptif

# 2. Visualisasi distribusi kategori diterima
def plot_distribusi_diterima(data):
    jumlah_diterima = data['DITERIMA'].value_counts()
    
    plt.figure(figsize=(10, 6))
    sns.countplot(y='DITERIMA', data=data, order=jumlah_diterima.index)
    plt.title('Distribusi Departemen yang Diterima')
    plt.xlabel('Jumlah Peserta')
    plt.ylabel('Departemen')
    plt.show()

    # Plot interaktif dengan Plotly
    fig = px.bar(jumlah_diterima, x=jumlah_diterima.values, y=jumlah_diterima.index,
                 orientation='h', title='Distribusi Departemen yang Diterima')
    fig.update_layout(xaxis_title='Jumlah Peserta', yaxis_title='Departemen')
    fig.show()

# 3. Visualisasi distribusi pilihan pertama
def plot_distribusi_pilihan_pertama(data):
    jumlah_pilihan1 = data['pilihan 1'].value_counts()
    
    plt.figure(figsize=(10, 6))
    sns.countplot(y='pilihan 1', data=data, order=jumlah_pilihan1.index)
    plt.title('Distribusi Pilihan Pertama')
    plt.xlabel('Jumlah Peserta')
    plt.ylabel('Departemen')
    plt.show()

    # Plot interaktif dengan Plotly
    fig = px.bar(jumlah_pilihan1, x=jumlah_pilihan1.values, y=jumlah_pilihan1.index,
                 orientation='h', title='Distribusi Pilihan Pertama')
    fig.update_layout(xaxis_title='Jumlah Peserta', yaxis_title='Departemen')
    fig.show()

# 4. Visualisasi distribusi pilihan kedua
def plot_distribusi_pilihan_kedua(data):
    jumlah_pilihan2 = data['pilihan 2'].value_counts()
    
    plt.figure(figsize=(10, 6))
    sns.countplot(y='pilihan 2', data=data, order=jumlah_pilihan2.index)
    plt.title('Distribusi Pilihan Kedua')
    plt.xlabel('Jumlah Peserta')
    plt.ylabel('Departemen')
    plt.show()

    # Plot interaktif dengan Plotly
    fig = px.bar(jumlah_pilihan2, x=jumlah_pilihan2.values, y=jumlah_pilihan2.index,
                 orientation='h', title='Distribusi Pilihan Kedua')
    fig.update_layout(xaxis_title='Jumlah Peserta', yaxis_title='Departemen')
    fig.show()

# Menjalankan semua fungsi analisis dan visualisasi
def main():
    # Menampilkan statistik deskriptif
    print("Memulai analisis deskriptif...")
    tampilkan_statistik_deskriptif(data_lembar)

    # Plot distribusi diterima
    print("\nVisualisasi distribusi diterima...")
    plot_distribusi_diterima(data_lembar)

    # Plot distribusi pilihan pertama
    print("\nVisualisasi distribusi pilihan pertama...")
    plot_distribusi_pilihan_pertama(data_lembar)

    # Plot distribusi pilihan kedua
    print("\nVisualisasi distribusi pilihan kedua...")
    plot_distribusi_pilihan_kedua(data_lembar)

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
