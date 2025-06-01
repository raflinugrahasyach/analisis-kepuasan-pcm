# Simpan file ini sebagai 01_Beranda.py
# di dalam folder `pages` (misalnya, final_project_streamlit/pages/01_Beranda.py)

import streamlit as st
import base64 # Untuk encode gambar logo jika ada

# --- Fungsi Bantuan (Jika ada fungsi global, idealnya diimpor dari app.py atau utils.py) ---
# Untuk halaman ini, kita akan menggunakan gaya global yang sudah di-set di app.py.
# Fungsi spesifik untuk halaman ini bisa didefinisikan di sini.

def display_page_header(title, subtitle=""):
    """Menampilkan header utama halaman (menggunakan kelas CSS dari app.py)."""
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='body-text' style='text-align:center; font-size:1.1em; font-style:italic; margin-bottom:1.5rem;'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_subheader(title):
    """Menampilkan sub-header untuk setiap bagian konten (menggunakan kelas CSS dari app.py)."""
    st.markdown(f"<h2 class='sub-header'>{title}</h2>", unsafe_allow_html=True)

def create_content_box(content_function, *args, **kwargs):
    """Membuat container bergaya 'card' untuk konten (menggunakan kelas CSS dari app.py)."""
    # st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    # content_function(*args, **kwargs)
    # st.markdown("</div>", unsafe_allow_html=True)
    # Di Streamlit versi baru, st.container() sendiri sudah cukup untuk pengelompokan.
    # Kelas .content-box akan diterapkan pada elemen di dalamnya jika diperlukan.
    with st.container(border=True): # Menggunakan border bawaan Streamlit jika versi mendukung
        # st.markdown("<div class='content-box'>", unsafe_allow_html=True) # Jika ingin styling CSS kustom
        content_function(*args, **kwargs)
        # st.markdown("</div>", unsafe_allow_html=True)


# Fungsi untuk memuat dan menampilkan logo ITS
def show_its_logo():
    logo_path = "assets/its_logo.png"  # Pastikan path ini benar dan file logo ada
    try:
        with open(logo_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 15px; margin-top: -10px;">
                <img src="data:image/png;base64,{encoded_string}" alt="Logo ITS" width="100">
            </div>
            """,
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        # st.warning("Logo ITS (assets/its_logo.png) tidak ditemukan.") # Bisa di-uncomment jika perlu notifikasi
        st.markdown( # Fallback jika logo tidak ada
            """
            <div style="display: flex; justify-content: center; margin-bottom: 15px; margin-top: -10px; font-size: 16px; font-weight: bold; color: #1E3A8A; padding: 8px; border: 1px dashed #D1D5DB; border-radius: 8px;">
                [Logo Institut Teknologi Sepuluh Nopember]
            </div>
            """, unsafe_allow_html=True)

# --- Konten Halaman Beranda ---
def display_main_title_section():
    """Menampilkan judul utama penelitian dan informasi dasar."""
    show_its_logo() # Tampilkan logo di atas judul
    st.markdown(
        """
        <div style='text-align: center; margin-bottom: 25px;'>
            <h1 style='color: #1E3A8A; font-size: 28px; font-weight: bold; line-height: 1.25; margin-bottom: 8px;'>
                ANALISIS TINGKAT KEPUASAN PENGUNJUNG<br>PAKUWON CITY MALL SURABAYA
            </h1>
            <h2 style='color: #2563EB; font-size: 20px; font-weight: normal;  line-height: 1.25; margin-bottom: 12px;'>
                BERDASARKAN DIMENSI SERVQUAL MENGGUNAKAN METODE IPA DAN CSI
            </h2>
            <p style='font-size: 15px; color: #4B5563; margin-top: 10px;'>
                Final Project Mata Kuliah Metode Riset Sosial dan Bisnis (VS191505)
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_team_info_section():
    """Menampilkan informasi tim peneliti dan pembimbing."""
    st.markdown("<h3 style='text-align:center; color: #1E3A8A; font-size:18px; margin-bottom:15px;'>Disusun Oleh Tim Peneliti:</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='content-box' style='text-align: center; height:100%;'>
                <h4 style='color: #1E3A8A; margin-bottom:8px; font-size:16px;'>Anggota Tim:</h4>
                <p style='font-size: 14px; color: #374151; margin-bottom:4px;'>Azzam Pahlawan Ramadhan (2043221006)</p>
                <p style='font-size: 14px; color: #374151; margin-bottom:4px;'>Muhammad Rafli Nugrahasyach (2043221085)</p>
                <p style='font-size: 14px; color: #374151;'>Edbert Fernando (2043221106)</p>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div class='content-box' style='text-align: center; height:100%;'>
                <h4 style='color: #1E3A8A; margin-bottom:8px; font-size:16px;'>Dosen Pengampu:</h4>
                <p style='font-size: 14px; color: #374151; margin-bottom:4px;'>Drs. Destri Susilaningrum, M.Si.</p>
                <p style='font-size: 14px; color: #374151;'>Moch. Abdillah Nafis, S. Stat., M.MT</p>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown(
            """
            <div class='content-box' style='text-align: center; height:100%;'>
                <h4 style='color: #1E3A8A; margin-bottom:8px; font-size:16px;'>Asisten Dosen:</h4>
                <p style='font-size: 14px; color: #374151;'>Albertus Eka Putra Haryanto, S.Tr. Stat., M.Stat.</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True) # Spacer

def display_institution_info_section():
    """Menampilkan informasi institusi."""
    display_section_subheader("🏢 Informasi Institusi")
    st.markdown(
        """
        <div class='body-text' style='text-align: center;'>
            <p>Program Studi Sarjana Terapan Statistika Bisnis</p>
            <p>Departemen Statistika Bisnis</p>
            <p>Fakultas Vokasi</p>
            <p><b>Institut Teknologi Sepuluh Nopember</b></p>
            <p>Surabaya, 2025</p>
        </div>
        """, unsafe_allow_html=True)

def display_abstract_section():
    """Menampilkan abstrak penelitian."""
    display_section_subheader("📜 Abstrak Penelitian")
    st.markdown(
        """
        <div class='body-text' style='padding: 15px; border-left: 4px solid #2563EB; background-color: #EFF6FF; border-radius: 6px;'>
        <p>
        Industri ritel modern dan pusat perbelanjaan memainkan peran strategis dalam mendukung pertumbuhan ekonomi, khususnya di kawasan perkotaan seperti Surabaya. Pakuwon City Mall (PCM) Surabaya, sebagai salah satu pusat perbelanjaan yang relatif baru, memerlukan evaluasi berkelanjutan terhadap kualitas layanannya untuk memenuhi dan melampaui ekspektasi konsumen. Penelitian ini bertujuan untuk menganalisis secara komprehensif tingkat kepuasan pengunjung PCM. Analisis didasarkan pada dimensi SERVQUAL untuk mengidentifikasi kesenjangan kualitas layanan, metode Importance Performance Analysis (IPA) untuk menentukan prioritas perbaikan, dan Customer Satisfaction Index (CSI) untuk mengukur indeks kepuasan secara keseluruhan.
        </p>
        <p>
        Pendekatan kuantitatif digunakan dalam penelitian ini, dengan data primer yang dikumpulkan melalui survei kuesioner kepada pengunjung PCM. Teknik pengambilan sampel yang diterapkan adalah sampling acak sistematis untuk memastikan representativitas sampel. Analisis data akan melibatkan perhitungan GAP antara harapan dan persepsi kualitas layanan, pemetaan atribut layanan ke dalam matriks IPA, serta perhitungan nilai CSI.
        </p>
        <p>
        Hasil penelitian ini diharapkan dapat memberikan wawasan mendalam mengenai karakteristik kepuasan pengunjung, mengidentifikasi area-area layanan yang memerlukan perhatian dan peningkatan khusus, serta menyajikan ukuran kuantitatif tingkat kepuasan secara keseluruhan. Temuan ini diharapkan dapat menjadi landasan bagi manajemen PCM dalam merumuskan strategi peningkatan kualitas layanan yang efektif, sehingga dapat meningkatkan pengalaman dan loyalitas pengunjung.
        </p>
        </div>
        """, unsafe_allow_html=True
    )

# --- Struktur Halaman Beranda ---
# Mengatur judul utama halaman (ini akan menggunakan gaya dari app.py jika halaman ini di-load)
display_page_header("Selamat Datang di Aplikasi Analisis Kepuasan Pengunjung PCM", "Visualisasi Interaktif Hasil Penelitian Final Project")

create_content_box(display_main_title_section)
create_content_box(display_team_info_section)
create_content_box(display_institution_info_section)
create_content_box(display_abstract_section)
