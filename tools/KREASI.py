import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Bagian 1: Judul Aplikasi
st.title("Persebaran Pengguna Internet di Indonesia Berdasarkan Pulau")

# Bagian 2: Dataset Pengguna Internet per Pulau
st.subheader("Tabel Pengguna Internet di Indonesia Berdasarkan Pulau")

# Dataset pengguna internet di Indonesia berdasarkan pulau
data_persebaran = {
    'Pulau': ['Jawa', 'Sumatera', 'Kalimantan', 'Sulawesi', 'Papua'],
    'Jumlah Pengguna (juta)': [120, 50, 20, 15, 5]
}

# Membuat DataFrame untuk pengguna internet per pulau
df_persebaran = pd.DataFrame(data_persebaran)

# Menampilkan tabel interaktif
st.dataframe(df_persebaran)

# Bagian 3: Membuat Peta Persebaran Pengguna Internet
st.subheader("Peta Persebaran Pengguna Internet Berdasarkan Pulau")

# Load GeoJSON file atau shapefile untuk peta Indonesia
# Pastikan file ini sudah kamu unduh dan berada di folder yang sama dengan aplikasi
# atau gunakan path relatif sesuai lokasi file GeoJSON atau shapefile.
gdf = gpd.read_file("path/to/indonesia-pulau.geojson")

# Gabungkan dataset pengguna internet dengan GeoDataFrame berdasarkan kolom 'Pulau'
gdf = gdf.merge(df_persebaran, left_on="NAME_1", right_on="Pulau")

# Membuat peta dengan Matplotlib
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
gdf.plot(column='Jumlah Pengguna (juta)', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title("Persebaran Pengguna Internet di Indonesia Berdasarkan Pulau", fontsize=15)
ax.axis('off')

# Menampilkan peta di Streamlit
st.pyplot(fig)

# Bagian 4: Penjelasan
st.write("""
Peta di atas menunjukkan persebaran pengguna internet di Indonesia berdasarkan pulau besar.
Jawa merupakan pulau dengan jumlah pengguna internet terbesar, diikuti oleh Sumatera, Kalimantan, Sulawesi, dan Papua.
Visualisasi ini menggunakan **GeoPandas** dan **Matplotlib** untuk menunjukkan distribusi data berdasarkan wilayah.
""")
