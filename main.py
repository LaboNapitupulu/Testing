import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/001_Rafi Diva Efangga.py",
    title="001 - Rafi Diva Efangga",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/005_Efi Defiyati.py",
    title="005 - Efi Defiyati",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/033_Tesalonika Hutajulu",
    title="033 - Tesalonika Hutajulu",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/037_Labo Napitupulu.py",
    title="037 - Labo Napitupulu",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/055_Aulia Rizky Syahridafitri.py",
    title="055 - Aulia Rizky Syahridafitri",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/062_Abdillah Fikri Al Pome",
    title="062 - Abdillah Fikri Al Pome",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/074_Lutfia Aisyah Putri",
    title="074 - Lutfia Aisyah Putri",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/075_Aliya Ammara Ananta",
    title="075 - Aliya Ammara Ananta",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/083_Nadya Ratu Anjani.",
    title="083_Nadya Ratu Anjani.",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/084_Aisyah Musfirah.",
    title="084 - Aisyah Musfirah.",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/089_Lia Hana Ichisasmita",
    title="089 - Lia Hana Ichisasmita",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/105_Arielva Simon Siahaan",
    title="105 - Arielva Simon Siahaan",
    icon=":material/person:",
)


#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12,Mahasiswa13],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

