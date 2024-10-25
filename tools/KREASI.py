import streamlit as st
import pandas as pd
import plotly.express as px

# Judul aplikasi
st.title("Pengguna Internet di Dunia")

# Dataset Pengguna Internet di Dunia
data_internet = {
    'Negara': ['United States', 'Indonesia', 'India', 'Brazil', 'China'],
    'Pengguna Internet (%)': [89, 64, 50, 75, 60]
}

# Membuat DataFrame untuk pengguna internet di negara-negara besar
df_internet = pd.DataFrame(data_internet)

# Menampilkan tabel data pengguna internet
st.subheader("Tabel Pengguna Internet di Negara-Negara Besar")
st.dataframe(df_internet)

# Membuat peta interaktif dengan Plotly
st.subheader("Peta Pengguna Internet di Dunia Berdasarkan Negara")

# Choropleth mapbox Plotly
fig = px.choropleth(
    df_internet, 
    locations='Negara', 
    locationmode='country names',
    color='Pengguna Internet (%)', 
    hover_name='Negara',
    title="Pengguna Internet di Dunia Berdasarkan Negara",
    color_continuous_scale="Blues"
)

# Menampilkan peta di Streamlit
st.plotly_chart(fig)

# Penjelasan tambahan
st.write("""
Peta di atas menunjukkan persentase pengguna internet di berbagai negara. 
Amerika Serikat memiliki persentase pengguna internet tertinggi di antara negara-negara yang dibandingkan.
""")
