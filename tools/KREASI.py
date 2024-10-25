import streamlit as st
import pandas as pd
import plotly.express as px

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

# Bagian 3: Peta Interaktif Persebaran Pengguna Internet
st.subheader("Peta Persebaran Pengguna Internet Berdasarkan Pulau")

# Data koordinat dan geojson untuk pulau-pulau besar di Indonesia
# Untuk membuat visualisasi peta, kita menggunakan Plotly dengan peta choropleth

# URL GeoJSON untuk peta Indonesia
geojson_url = "https://raw.githubusercontent.com/superpikar/indonesia-geojson/master/indonesia-geojson/indonesia-provinces.geojson"

# Membuat grafik peta dengan Plotly
fig = px.choropleth_mapbox(
    df_persebaran, 
    geojson=geojson_url, 
    locations='Pulau', 
    featureidkey="properties.state",
    color='Jumlah Pengguna (juta)',
    hover_name='Pulau',
    title="Persebaran Pengguna Internet di Indonesia Berdasarkan Pulau",
    mapbox_style="carto-positron",
    center={"lat": -1.5, "lon": 117.5},  # Pusat geografis Indonesia
    zoom=3,
    color_continuous_scale="Blues"
)

# Menampilkan grafik peta di Streamlit
st.plotly_chart(fig)

# Bagian 4: Penjelasan
st.write("""
Peta di atas menunjukkan persebaran pengguna internet di Indonesia berdasarkan pulau besar. 
Jawa merupakan pulau dengan jumlah pengguna internet terbesar, diikuti oleh Sumatera, Kalimantan, Sulawesi, dan Papua. 
Visualisasi ini menggunakan **Choropleth Map** yang menampilkan distribusi data dengan warna.
""")
