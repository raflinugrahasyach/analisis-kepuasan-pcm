# Simpan file ini sebagai app.py
# di root folder proyek Anda (misalnya, final_project_streamlit_pcm/)

import streamlit as st

# --- KONFIGURASI HALAMAN UTAMA ---
st.set_page_config(
    page_title="Analisis Kepuasan Pengunjung PCM",
    page_icon="assets/pcm_favicon.png",  # Ganti dengan path ke favicon Anda jika ada, atau emoji 🛍️ / 📊
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:tim.peneliti.pcm@example.com', # Ganti dengan email kontak Anda
        'Report a bug': "mailto:tim.peneliti.pcm@example.com?subject=Bug Report Aplikasi PCM",
        'About': """
        ## Aplikasi Analisis Kepuasan Pengunjung Pakuwon City Mall Surabaya

        Aplikasi ini menyajikan hasil penelitian mengenai tingkat kepuasan pengunjung Pakuwon City Mall (PCM) Surabaya, 
        dilakukan oleh tim mahasiswa Sarjana Terapan Statistika Bisnis, Fakultas Vokasi, 
        Institut Teknologi Sepuluh Nopember (ITS) Surabaya, tahun 2025.

        **Tim Peneliti:**
        - Azzam Pahlawan Ramadhan (2043221006)
        - Muhammad Rafli Nugrahasyach (2043221085)
        - Edbert Fernando (2043221106)

        **Dosen Pengampu:**
        - Drs. Destri Susilaningrum, M.Si.
        - Moch. Abdillah Nafis, S. Stat., M.MT

        **Asisten Dosen:**
        - Albertus Eka Putra Haryanto, S.Tr. Stat., M.Stat.
        """
    }
)

# --- CSS KUSTOM UNTUK TAMPILAN PROFESIONAL ---
def load_custom_css():
    st.markdown("""
    <style>
        /* Import Font dari Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Roboto:wght@400;500;700&display=swap');

        /* Variabel Warna Utama (Contoh: Biru ITS dan aksen modern) */
        :root {
            --primary-color: #003366; /* Biru Tua ITS */
            --secondary-color: #00A3E0; /* Biru Muda ITS / Aksen */
            --accent-color: #FFC107; /* Kuning sebagai aksen (opsional) */
            --text-color: #333333;
            --light-text-color: #555555;
            --bg-color: #F8F9FA; /* Latar belakang sedikit abu-abu */
            --card-bg-color: #FFFFFF;
            --border-color: #DEE2E6;
        }

        /* Gaya Umum Aplikasi */
        .stApp {
            background-color: var(--bg-color);
            font-family: 'Roboto', sans-serif;
            color: var(--text-color);
        }

        /* Sidebar Styling */
        .st-emotion-cache-16txtl3 { /* Target sidebar Streamlit (cek kelas CSS jika versi berubah) */
            background-color: var(--primary-color); 
            padding-top: 1.5rem;
        }
        .st-emotion-cache-16txtl3 .st-emotion-cache-1gulkj5 { /* Link navigasi di sidebar */
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: #FFFFFF; /* Warna teks link navigasi */
        }
        .st-emotion-cache-16txtl3 .st-emotion-cache-1gulkj5:hover,
        .st-emotion-cache-16txtl3 .st-emotion-cache-1gulkj5.st-emotion-cache-134448f { /* Link aktif dan hover */
            background-color: var(--secondary-color);
            color: #FFFFFF;
        }
        .st-emotion-cache-16txtl3 .st-emotion-cache-6qob1r { /* Header di sidebar (jika ada) */
             color: #FFFFFF;
             font-family: 'Montserrat', sans-serif;
        }
         .st-emotion-cache-16txtl3 .stAlert { /* Info box di sidebar */
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #FFFFFF;
        }
        .st-emotion-cache-16txtl3 .stAlert p {
             color: #FFFFFF !important;
        }


        /* Header Utama Halaman */
        .main-header {
            font-family: 'Montserrat', sans-serif;
            font-size: 2.2rem; /* Ukuran font judul utama */
            font-weight: 700;
            color: var(--primary-color);
            padding: 1.5rem 0;
            margin-bottom: 1.5rem;
            text-align: center;
            border-bottom: 3px solid var(--secondary-color);
        }
        .page-subtitle {
            font-family: 'Roboto', sans-serif;
            font-size: 1.1rem;
            color: var(--light-text-color);
            text-align: center;
            margin-top: -1rem;
            margin-bottom: 2rem;
            font-style: italic;
        }

        /* Sub-Header Bagian */
        .section-subheader {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.6rem; /* Ukuran yang pas untuk sub-judul */
            font-weight: 600;
            color: var(--primary-color);
            margin-top: 2.5rem;
            margin-bottom: 1.2rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border-color);
        }
        .section-subheader-minor { /* Untuk sub-sub judul jika perlu */
            font-family: 'Montserrat', sans-serif;
            font-size: 1.3rem;
            font-weight: 600;
            color: var(--secondary-color);
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }

        /* Kontainer Konten (Card) */
        .content-card {
            background-color: var(--card-bg-color);
            padding: 1.5rem 2rem; /* Padding lebih besar */
            border-radius: 12px; /* Sudut lebih melengkung */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08); /* Bayangan lebih halus */
            margin-bottom: 2rem;
            border: 1px solid var(--border-color);
        }
        
        /* Teks Biasa */
        .body-text {
            font-size: 1rem; /* Ukuran font standar untuk teks */
            line-height: 1.7; /* Jarak antar baris yang nyaman */
            color: var(--text-color);
            text-align: justify; 
        }
        .body-text p, .body-text li {
            margin-bottom: 0.8rem; 
        }
        .body-text ul, .body-text ol {
            padding-left: 1.5rem; 
        }
        .body-text strong { /* Teks tebal */
            color: var(--primary-color);
            font-weight: 600;
        }
        .body-text h5 { /* Sub-judul kecil dalam teks, seperti untuk interpretasi grafik */
             font-family: 'Montserrat', sans-serif;
             color: var(--secondary-color);
             font-size: 1.1rem;
             font-weight: 600;
             margin-top: 1rem;
             margin-bottom: 0.5rem;
        }


        /* Styling untuk Expander */
        .stExpander {
            border: 1px solid var(--border-color) !important;
            border-radius: 8px !important;
            box-shadow: 0 3px 6px rgba(0,0,0,0.05) !important;
            margin-bottom: 1.2rem;
        }
        .stExpander header { 
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            color: var(--primary-color);
            font-size: 1.1rem; 
            background-color: #F8F9FA; /* Latar header expander sedikit beda */
            border-bottom: 1px solid var(--border-color);
        }
        .stExpander header:hover {
            background-color: #EFF6FF; 
        }

        /* Styling untuk Tabs */
        .stTabs [data-baseweb="tab-list"] {
        	gap: 12px; /* Jarak antar tab */
        }
        .stTabs [data-baseweb="tab"] {
        	height: 44px; /* Tinggi tab */
        	white-space: pre-wrap;
        	background-color: var(--card-bg-color);
        	border-radius: 8px 8px 0 0; /* Sudut atas melengkung */
            border-bottom: 2px solid transparent;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            color: var(--light-text-color);
        }
        .stTabs [data-baseweb="tab"]:hover {
        	background-color: #E9ECEF; /* Warna hover tab */
            color: var(--primary-color);
        }
        .stTabs [aria-selected="true"] { /* Tab aktif */
        	background-color: var(--card-bg-color);
            border-bottom: 3px solid var(--secondary-color);
            color: var(--primary-color);
            font-weight: 700;
        }
        
        /* Styling untuk Tabel (DataFrame) */
        .stDataFrame {
            border-radius: 8px;
            overflow: hidden; /* Agar border-radius terlihat */
        }
        /* Anda mungkin perlu menargetkan kelas CSS yang lebih spesifik jika ingin mengubah header tabel, dll. */

        /* Tombol (jika digunakan) */
        .stButton>button {
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            font-family: 'Montserrat', sans-serif;
            border: 2px solid var(--secondary-color);
            color: var(--secondary-color);
            background-color: transparent;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            color: white;
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
        }
        .stButton>button:focus {
            box-shadow: 0 0 0 0.2rem rgba(0, 163, 224, 0.5) !important; /* Aksen fokus */
        }

    </style>
    """, unsafe_allow_html=True)

# Panggil fungsi untuk memuat CSS saat aplikasi dimulai
load_custom_css()

# --- KONTEN SIDEBAR (Muncul di semua halaman) ---
with st.sidebar:
    # Logo ITS bisa diletakkan di sini jika diinginkan
    try:
        # Pastikan file logo_its_putih.png ada di folder assets
        # atau ganti dengan path yang benar atau URL
        st.image("assets/logo_its_putih.png", width=100) 
    except Exception: # Menangkap semua jenis error jika gambar tidak ada
        st.markdown("<h3 style='color:white; text-align:center; font-family: Montserrat, sans-serif;'>ITS</h3>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: white; margin-bottom:1rem; font-family: Montserrat, sans-serif;'>Navigasi Riset</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 1px solid rgba(255,255,255,0.3); margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    
    # Deskripsi singkat aplikasi di sidebar
    st.markdown(
        """
        <div style='color: #E0E0E0; font-size: 0.9rem; text-align: justify; padding: 0 0.5rem;'>
        Selamat datang di dasbor interaktif hasil penelitian kepuasan pengunjung 
        <b>Pakuwon City Mall Surabaya</b>. 
        Gunakan menu di atas untuk menjelajahi berbagai temuan dan rekomendasi.
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("<hr style='border-top: 1px solid rgba(255,255,255,0.3); margin-top:1.5rem; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    
    # Informasi tambahan atau kredit
    st.markdown(
        """
        <div style='font-size: 0.8em; text-align: center; color: #B0B0B0;'>
            <p><strong>Tim Peneliti:</strong><br>
            Azzam P. R. (006) | M. Rafli N. (085) | Edbert F. (106)</p>
            <p><strong>Pembimbing Utama:</strong><br>
            Drs. Destri Susilaningrum, M.Si.</p>
            <p><i>Statistika Bisnis - FV ITS (2025)</i></p>
        </div>
        """, unsafe_allow_html=True
    )

# Catatan: Streamlit akan secara otomatis membuat navigasi dari file-file di folder `pages`.
# Tidak perlu menambahkan logika navigasi manual di sini jika menggunakan struktur folder `pages`.
