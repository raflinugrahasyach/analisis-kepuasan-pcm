# Simpan file ini sebagai app.py
# di root folder proyek Anda (misalnya, final_project_streamlit/app.py)

import streamlit as st
# from streamlit_option_menu import option_menu # Opsional, jika ingin menu sidebar kustom
# import plotly.express as px # Tidak digunakan langsung di app.py, tapi mungkin di pages
# import pandas as pd # Tidak digunakan langsung di app.py, tapi mungkin di pages

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Analisis Kepuasan PCM",
    page_icon="📊",  # Anda bisa menggunakan emoji atau path ke file .ico
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/library/api-reference',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': """
        ## Aplikasi Analisis Kepuasan Pengunjung Pakuwon City Mall
        Dibuat untuk Final Project Mata Kuliah Metode Riset Sosial dan Bisnis.
        
        Institut Teknologi Sepuluh Nopember, Surabaya - 2025.
        """
    }
)

# --- CSS KUSTOM ---
# Fungsi untuk memuat CSS dari file atau menggunakan inline CSS
def load_custom_css():
    # Prioritaskan memuat dari file styles.css jika ada
    # Untuk saat ini, kita akan menggunakan inline CSS untuk kemudahan.
    # Jika Anda ingin menggunakan file styles.css, buat file tersebut dan uncomment bagian di bawah.
    # try:
    #     with open("styles.css") as f:
    #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    # except FileNotFoundError:
    # Fallback ke inline CSS jika styles.css tidak ditemukan atau tidak digunakan
    st.markdown("""
    <style>
        /* Gaya umum untuk aplikasi */
        .stApp {
            /* background-color: #f0f2f6; */ /* Contoh warna latar belakang netral */
            font-family: 'Arial', sans-serif; /* Font dasar yang bersih */
        }

        /* Gaya untuk judul utama di setiap halaman (digunakan oleh fungsi display_page_header) */
        .main-header {
            font-size: 30px; /* Ukuran font judul utama */
            font-weight: bold;
            color: #1E3A8A; /* Biru tua, sesuai dengan tema ITS atau korporat */
            padding-top: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 3px solid #D1D5DB; /* Garis bawah yang lebih tegas */
            margin-bottom: 1.5rem;
            text-align: center; /* Judul utama di tengah */
        }

        /* Gaya untuk sub-judul (digunakan oleh fungsi display_section_subheader) */
        .sub-header {
            font-size: 22px; /* Ukuran yang pas untuk sub-judul */
            font-weight: bold;
            color: #2563EB; /* Biru yang lebih cerah dari header utama */
            margin-top: 1.8rem;
            margin-bottom: 0.9rem;
            border-left: 4px solid #2563EB; /* Aksen garis kiri */
            padding-left: 10px;
        }

        /* Gaya untuk container/card yang membungkus konten (digunakan oleh fungsi create_content_box) */
        .content-box {
            background-color: #FFFFFF; /* Putih bersih */
            padding: 20px 25px; /* Padding atas-bawah dan kiri-kanan */
            border-radius: 10px; /* Sudut yang lebih melengkung */
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.08); /* Bayangan yang lebih halus */
            margin-bottom: 20px;
            border: 1px solid #E5E7EB; /* Border tipis untuk definisi */
        }
        
        /* Gaya untuk expander Streamlit */
        .stExpander {
            border: 1px solid #DDE2E9 !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04) !important;
            margin-bottom: 1rem; /* Jarak antar expander */
        }
        .stExpander header { /* Styling untuk header expander */
            font-weight: bold;
            color: #1E3A8A; /* Warna teks header expander */
            font-size: 18px; /* Ukuran font header expander */
        }
        .stExpander header:hover {
            background-color: #f0f2f6; /* Warna latar saat hover di header expander */
        }


        /* Gaya untuk teks biasa di dalam konten */
        .body-text {
            font-size: 16px; /* Ukuran font standar untuk teks */
            line-height: 1.65; /* Jarak antar baris yang nyaman */
            color: #374151; /* Abu-abu tua untuk kontras yang baik */
            text-align: justify; /* Rata kiri-kanan untuk tampilan formal */
        }
        .body-text p, .body-text li {
            margin-bottom: 0.7rem; /* Jarak antar paragraf/list item */
        }
        .body-text ul, .body-text ol {
            padding-left: 20px; /* Indentasi untuk list */
        }

        /* Gaya untuk sidebar */
        /* Anda bisa menargetkan kelas CSS spesifik dari Streamlit jika ingin kustomisasi lebih lanjut */
        /* .css-1d391kg { background-color: #F9FAFB; } */
        
        /* Gaya untuk tombol Streamlit (jika diperlukan) */
        .stButton>button {
            border-radius: 8px;
            padding: 8px 18px;
            font-weight: bold;
            border: 1px solid #2563EB; /* Border tombol */
            color: #2563EB; /* Warna teks tombol */
            background-color: #FFFFFF; /* Latar belakang tombol */
        }
        .stButton>button:hover {
            color: white;
            background-color: #1D4ED8; /* Warna tombol saat hover */
            border: 1px solid #1D4ED8;
        }
    </style>
    """, unsafe_allow_html=True)

# Panggil fungsi untuk memuat CSS saat aplikasi dimulai
load_custom_css()

# --- Konten Sidebar ---
# Konten ini akan muncul di sidebar di semua halaman
with st.sidebar:
    # Anda bisa menambahkan logo di sini jika mau
    # try:
    #     st.image("assets/its_logo.png", width=100, caption="Institut Teknologi Sepuluh Nopember")
    # except FileNotFoundError:
    #     st.markdown("<p style='text-align:center; font-weight:bold; color:#1E3A8A;'>[Logo ITS]</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #1E3A8A; margin-top:0px; margin-bottom:10px;'>Menu Navigasi</h2>", unsafe_allow_html=True)
    st.markdown("---") # Garis pemisah
    
    # Deskripsi singkat aplikasi di sidebar
    st.info(
        """
        **Selamat Datang!**
        
        Aplikasi ini adalah visualisasi interaktif dari hasil penelitian mengenai **Analisis Tingkat Kepuasan Pengunjung Pakuwon City Mall Surabaya**.
        
        Gunakan menu navigasi di atas untuk menjelajahi setiap bab penelitian.
        """
    )
    st.markdown("---") # Garis pemisah
    
    # Informasi tambahan atau kredit
    st.markdown(
        """
        <div style='font-size: 0.85em; text-align: center; color: #4B5563;'>
            <p><strong>Tim Peneliti:</strong><br>
            Azzam Pahlawan Ramadhan<br>
            Muhammad Rafli Nugrahasyach<br>
            Edbert Fernando</p>
            <p><strong>Dosen Pengampu:</strong><br>
            Drs. Destri Susilaningrum, M.Si.<br>
            Moch. Abdillah Nafis, S. Stat., M.MT</p>
            <p><strong>Asisten Dosen:</strong><br>
            Albertus Eka Putra H., S.Tr. Stat., M.Stat.</p>
            <hr style='border-top: 1px solid #E5E7EB; margin: 8px 0;'>
            <p>Statistika Bisnis - Fakultas Vokasi<br>
            Institut Teknologi Sepuluh Nopember<br>
            Surabaya, 2025</p>
        </div>
        """, unsafe_allow_html=True
    )

# Pesan default jika tidak ada halaman yang dipilih atau app.py dijalankan langsung
# Streamlit akan secara otomatis mencari file di folder `pages` untuk membuat navigasi.
# File ini (app.py) lebih berfungsi sebagai konfigurasi global dan penampung sidebar.
# Jika Anda ingin halaman utama ada di app.py (bukan di `pages/01_Beranda.py`),
# Anda bisa menambahkan konten di sini dan menghapus/mengubah nama `01_Beranda.py`.
# Contoh:
# if __name__ == "__main__":
#     st.title("Selamat Datang di Aplikasi Utama")
#     st.write("Ini adalah konten yang muncul jika app.py dijalankan sebagai skrip utama.")
#     st.write("Namun, untuk aplikasi multi-halaman, konten biasanya ada di folder `pages`.")
