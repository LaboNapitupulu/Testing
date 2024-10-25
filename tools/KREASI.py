import streamlit as st
import pandas as pd
import plotly.express as px

# Judul aplikasi
st.title("Persebaran Pengguna Internet di Indonesia Berdasarkan Pulau")

# Dataset Pengguna Internet per Pulau
data_persebaran = {
    'Pulau': ['Jawa', 'Sumatera', 'Kalimantan', 'Sulawesi', 'Papua'],
    'Jumlah Pengguna (juta)': [120, 50, 20, 15, 5]
}

# Membuat DataFrame untuk pengguna internet per pulau
df_persebaran = pd.DataFrame(data_persebaran)

# Menampilkan tabel data pengguna internet
st.subheader("Tabel Pengguna Internet Berdasarkan Pulau")
st.dataframe(df_persebaran)

# URL GeoJSON (pastikan URL ini benar dan dapat diakses)
geojson_url = "https://raw.githubusercontent.com/superpikar/indonesia-geojson/master/indonesia-geojson/indonesia-provinces.geojson"

# Membuat peta interaktif dengan Plotly
st.subheader("Peta Persebaran Pengguna Internet Berdasarkan Pulau")

# Choropleth mapbox Plotly
fig = px.choropleth_mapbox(
    df_persebaran, 
    geojson=geojson_url, 
    locations='Pulau',  # Kolom di DataFrame yang berisi nama pulau
    featureidkey="properties.NAME_1",  # Field di GeoJSON yang mencocokkan nama wilayah
    color='Jumlah Pengguna (juta)',  # Data yang digunakan untuk mewarnai
    hover_name='Pulau',  # Nama pulau yang ditampilkan saat hover
    title="Persebaran Pengguna Internet di Indonesia Berdasarkan Pulau",
    mapbox_style="carto-positron",
    center={"lat": -1.5, "lon": 117.5},  # Pusat peta di Indonesia
    zoom=3,  # Tingkat zoom
    color_continuous_scale="Blues"  # Skala warna untuk visualisasi
)

# Menampilkan peta di Streamlit
st.plotly_chart(fig)

# Penjelasan tambahan
st.write("""
Peta di atas menunjukkan persebaran pengguna internet di Indonesia berdasarkan pulau besar. 
Pulau Jawa memiliki jumlah pengguna internet terbesar, diikuti oleh Sumatera, Kalimantan, Sulawesi, dan Papua.
""")
