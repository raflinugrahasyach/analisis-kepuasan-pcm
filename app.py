# Simpan file ini sebagai app.py
# di root folder proyek Anda (misalnya, streamlit_pcm_presentation/)

import streamlit as st
import base64 # Untuk encode gambar logo jika ada

# --- KONFIGURASI HALAMAN UTAMA ---
st.set_page_config(
    page_title="Dasbor Kepuasan Pengunjung PCM",
    page_icon="assets/its_logo_fav.png",  # Ganti dengan path ke favicon ITS atau PCM Anda
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None, # Hapus atau ganti dengan link bantuan Anda
        'Report a bug': None, # Hapus atau ganti
        'About': """
        ## Dasbor Analisis Kepuasan Pengunjung Pakuwon City Mall Surabaya

        Aplikasi interaktif ini menyajikan temuan kunci dan rekomendasi strategis dari penelitian 
        mengenai tingkat kepuasan pengunjung Pakuwon City Mall (PCM) Surabaya.

        Penelitian dilakukan oleh tim mahasiswa Program Studi Sarjana Terapan Statistika Bisnis, 
        Departemen Statistika Bisnis, Fakultas Vokasi, Institut Teknologi Sepuluh Nopember (ITS) Surabaya, tahun 2025.
        """
    }
)

# --- CSS KUSTOM UNTUK TAMPILAN PROFESIONAL ---
def load_custom_css():
    st.markdown("""
    <style>
        /* Import Font dari Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Roboto:wght@400;500&display=swap');

        /* Variabel Warna Utama (Contoh: Biru ITS dan aksen modern) */
        :root {
            --primary-color: #003B6E; /* Biru Tua ITS yang lebih gelap sedikit */
            --secondary-color: #00AEEF; /* Biru Muda ITS / Aksen Cerah */
            --accent-color: #FFD700; /* Emas sebagai aksen */
            --text-color: #212529; /* Warna teks utama (gelap) */
            --light-text-color: #495057; /* Warna teks sekunder (abu-abu) */
            --bg-color: #F4F7F9; /* Latar belakang sangat terang, hampir putih */
            --card-bg-color: #FFFFFF; /* Warna latar kartu/kontainer */
            --border-color: #E0E0E0; /* Warna border halus */
            --header-font: 'Montserrat', sans-serif;
            --body-font: 'Roboto', sans-serif;
        }

        /* Gaya Umum Aplikasi */
        .stApp {
            background-color: var(--bg-color);
            font-family: var(--body-font);
            color: var(--text-color);
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: var(--primary-color); 
            padding-top: 1rem;
        }
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p, 
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] li,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] strong {
            color: #FFFFFF; /* Warna teks di sidebar */
        }
        [data-testid="stSidebar"] .st-emotion-cache-1gulkj5 { /* Link navigasi */
            padding: 0.7rem 1rem;
            border-radius: 0.4rem;
            margin-bottom: 0.3rem;
            font-weight: 500;
            color: #E0E0E0; 
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        [data-testid="stSidebar"] .st-emotion-cache-1gulkj5:hover,
        [data-testid="stSidebar"] .st-emotion-cache-1gulkj5.st-emotion-cache-134448f { /* Link aktif dan hover */
            background-color: var(--secondary-color);
            color: #FFFFFF;
            font-weight: 600;
        }
        [data-testid="stSidebar"] [data-testid="stImage"] img { /* Logo di sidebar */
            margin-bottom: 1rem;
        }
         [data-testid="stSidebar"] hr {
            border-top: 1px solid rgba(255,255,255,0.2);
            margin: 1rem 0;
        }

        /* Header Utama Halaman */
        .main-header {
            font-family: var(--header-font);
            font-size: 2rem; 
            font-weight: 700;
            color: var(--primary-color);
            padding: 1.2rem 0 1rem 0;
            margin-bottom: 0.5rem;
            text-align: center;
            border-bottom: 3px solid var(--secondary-color);
        }
        .page-subtitle {
            font-family: var(--body-font);
            font-size: 1.05rem;
            color: var(--light-text-color);
            text-align: center;
            margin-top: -0.5rem; /* Lebih dekat ke header */
            margin-bottom: 2rem;
            font-style: italic;
        }

        /* Sub-Header Bagian */
        .section-subheader {
            font-family: var(--header-font);
            font-size: 1.5rem; 
            font-weight: 600;
            color: var(--primary-color);
            margin-top: 2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.4rem;
            border-bottom: 2px solid var(--border-color);
        }
        .section-subheader-minor { 
            font-family: var(--header-font);
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--secondary-color);
            margin-top: 1.2rem;
            margin-bottom: 0.7rem;
        }

        /* Kontainer Konten (Card) - Menggunakan st.container(border=True) lebih disarankan */
        /* Jika ingin styling kustom: */
        .content-card-custom { 
            background-color: var(--card-bg-color);
            padding: 1.2rem 1.5rem; 
            border-radius: 10px; 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.07); 
            margin-bottom: 1.5rem;
            border: 1px solid var(--border-color);
        }
        
        /* Teks Biasa */
        .body-text {
            font-size: 0.95rem; 
            line-height: 1.65; 
            color: var(--text-color);
            text-align: justify; 
        }
        .body-text p, .body-text li {
            margin-bottom: 0.7rem; 
        }
        .body-text ul, .body-text ol {
            padding-left: 1.2rem; 
        }
        .body-text strong { 
            color: var(--primary-color);
            font-weight: 500; /* Sedikit lebih ringan dari 600 */
        }
        .body-text h5 { 
             font-family: var(--header-font);
             color: var(--secondary-color);
             font-size: 1.05rem;
             font-weight: 600;
             margin-top: 0.8rem;
             margin-bottom: 0.4rem;
        }

        /* Styling untuk Expander */
        .stExpander {
            border: 1px solid var(--border-color) !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.04) !important;
            margin-bottom: 1rem;
        }
        .stExpander header { 
            font-family: var(--header-font);
            font-weight: 600;
            color: var(--primary-color);
            font-size: 1.05rem; 
            background-color: #F0F4F7; /* Latar header expander sedikit beda */
            border-bottom: 1px solid var(--border-color);
            border-radius: 8px 8px 0 0; /* Cocokkan dengan border expander */
        }
         .stExpander header:hover {
            background-color: #E1EAF2; 
        }

        /* Styling untuk Tabs */
        .stTabs [data-baseweb="tab-list"] {
        	gap: 10px; 
            border-bottom: 2px solid var(--border-color);
        }
        .stTabs [data-baseweb="tab"] {
        	height: 40px; 
        	background-color: transparent; /* Transparan agar menyatu */
            border-radius: 6px 6px 0 0; 
            border-bottom: 3px solid transparent; /* Awalnya transparan */
            font-family: var(--header-font);
            font-weight: 500;
            color: var(--light-text-color);
            padding: 0.5rem 1rem;
            transition: color 0.3s ease, border-color 0.3s ease;
        }
        .stTabs [data-baseweb="tab"]:hover {
        	background-color: #E9ECEF; 
            color: var(--primary-color);
        }
        .stTabs [aria-selected="true"] { 
            border-bottom: 3px solid var(--secondary-color);
            color: var(--primary-color);
            font-weight: 600;
        }
        
        /* Footer Styling */
        .footer {
            padding: 1.5rem 0;
            margin-top: 3rem;
            text-align: center;
            font-size: 0.85em;
            color: var(--light-text-color);
            border-top: 1px solid var(--border-color);
            background-color: var(--card-bg-color); /* Footer dengan latar putih */
        }
        .footer img {
            margin: 0 10px; /* Jarak antar logo di footer */
            vertical-align: middle;
        }

    </style>
    """, unsafe_allow_html=True)

# Panggil fungsi untuk memuat CSS saat aplikasi dimulai
load_custom_css()

# --- FUNGSI UNTUK FOOTER YANG KONSISTEN ---
def display_footer():
    st.markdown("---", unsafe_allow_html=True) # Garis pemisah sebelum footer
    
    # Kolom untuk logo dan teks
    # Anda mungkin perlu menyesuaikan path ke logo Anda dan menyimpannya di folder `assets`
    logo_its_path = "assets/logo_its_biru.png"  # Ganti dengan path logo ITS Anda
    logo_statbis_path = "assets/logo_departemen_statbis.png" # Ganti dengan path logo Statbis Anda
    
    footer_html = f"""
    <div class="footer">
        <table style="width:100%; border:none; margin-bottom:10px;">
            <tr>
                <td style="width:20%; text-align:right; border:none; padding-right:15px;">
                    <img src="data:image/png;base64,{image_to_base64(logo_its_path)}" alt="Logo ITS" height="50">
                </td>
                <td style="width:60%; text-align:center; border:none;">
                    <strong>Tim Peneliti:</strong><br>
                    Azzam Pahlawan Ramadhan (2043221006) | Muhammad Rafli Nugrahasyach (2043221085) | Edbert Fernando (2043221106)<br><br>
                    <strong>Dosen Pengampu:</strong> Drs. Destri Susilaningrum, M.Si. | Moch. Abdillah Nafis, S. Stat., M.MT<br>
                    <strong>Asisten Dosen:</strong> Albertus Eka Putra Haryanto, S.Tr. Stat., M.Stat.<br><br>
                    <strong>Departemen Statistika Bisnis, Fakultas Vokasi</strong><br>
                    Institut Teknologi Sepuluh Nopember (ITS), Surabaya - 2025
                </td>
                <td style="width:20%; text-align:left; border:none; padding-left:15px;">
                    <img src="data:image/png;base64,{image_to_base64(logo_statbis_path)}" alt="Logo Statistika Bisnis" height="50">
                </td>
            </tr>
        </table>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

def image_to_base64(image_path):
    """Mengubah file gambar menjadi string base64 untuk disematkan di HTML."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return "" # Kembalikan string kosong jika file tidak ditemukan

# --- KONTEN SIDEBAR (Muncul di semua halaman) ---
with st.sidebar:
    try:
        # Ganti dengan path logo ITS yang cocok untuk sidebar (misalnya versi putih)
        st.image("assets/logo_its_putih.png", width=120) 
    except Exception:
        st.markdown("<h1 style='color:white; text-align:center; font-family: var(--header-font);'>ITS</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: white; margin-bottom:0.5rem; font-family: var(--header-font); font-size:1.5rem;'>Navigasi Dasbor</h2>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style='color: #E8F0F4; font-size: 0.9rem; text-align: justify; padding: 0 0.5rem;'>
        Selamat datang di dasbor interaktif hasil penelitian kepuasan pengunjung 
        <b>Pakuwon City Mall Surabaya</b>. 
        Gunakan menu di atas untuk menjelajahi berbagai temuan dan rekomendasi.
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style='font-size: 0.8em; text-align: center; color: #C0D0D8;'>
            <p><strong>Riset Kepuasan Pengunjung PCM</strong><br>
            Tim Statistika Bisnis ITS</p>
            <p><i>Fakultas Vokasi - 2025</i></p>
        </div>
        """, unsafe_allow_html=True
    )

# Catatan: Streamlit secara otomatis membuat navigasi dari file-file di folder `pages`.
# Tidak perlu menambahkan logika navigasi manual di sini.
