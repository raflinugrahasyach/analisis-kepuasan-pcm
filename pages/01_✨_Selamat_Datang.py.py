# Simpan file ini sebagai 01_✨_Selamat_Datang.py
# di dalam folder `pages` (misalnya, final_project_streamlit_pcm/pages/)

import streamlit as st

# --- FUNGSI BANTUAN SPESIFIK HALAMAN (jika perlu) atau gunakan global ---
# Mengasumsikan CSS global dari app.py sudah diterapkan.

def display_page_title(title, subtitle):
    """Menampilkan judul utama halaman dan subjudulnya."""
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)

def display_content_section(title, content_html, icon=""):
    """Menampilkan bagian konten dengan subheader dan isi."""
    if icon:
        st.markdown(f"<h2 class='section-subheader'>{icon} {title}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 class='section-subheader'>{title}</h2>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='content-card'><div class='body-text'>{content_html}</div></div>", unsafe_allow_html=True)

# --- KONTEN HALAMAN SELAMAT DATANG ---

# Atur judul utama halaman ini (akan muncul di tab browser jika ini halaman pertama yang di-load)
# st.set_page_config(page_title="Selamat Datang - Analisis PCM", page_icon="✨") # Tidak perlu jika sudah di app.py

display_page_title(
    "Selamat Datang di Dasbor Analisis Kepuasan Pengunjung",
    "Menjelajahi Wawasan untuk Peningkatan Layanan di Pakuwon City Mall Surabaya"
)

# --- Sekilas Tentang Pakuwon City Mall Surabaya ---
pcm_info_html = """
    <p>Pakuwon City Mall (PCM) Surabaya, yang secara resmi dibuka pada akhir tahun 2020, telah dengan cepat memposisikan diri sebagai salah satu destinasi gaya hidup premium di kawasan Surabaya Timur. Terintegrasi dalam superblok Pakuwon City, mall ini dirancang untuk melayani segmen pasar menengah ke atas, menawarkan pengalaman berbelanja, kuliner, dan hiburan yang komprehensif.</p>
    <p>Dengan luas area lebih dari 60.000 m² dan menampung lebih dari 200 gerai ternama, PCM tidak hanya berfungsi sebagai pusat perbelanjaan, tetapi juga sebagai episentrum kegiatan sosial dan rekreasi bagi masyarakat urban. Lokasinya yang strategis, termasuk kedekatannya dengan berbagai institusi pendidikan tinggi, turut membentuk profil pengunjung yang dinamis dan beragam.</p>
    <p>Sebagai pemain yang relatif baru di tengah lanskap ritel Surabaya yang kompetitif, pemahaman mendalam terhadap ekspektasi dan kepuasan pengunjung menjadi kunci bagi PCM untuk terus berinovasi, meningkatkan kualitas layanan, dan memperkuat posisinya di pasar.</p>
"""
display_content_section(
    "Sekilas Tentang Pakuwon City Mall Surabaya",
    pcm_info_html,
    icon="🛍️"
)

# --- Konteks dan Tujuan Riset (Ringkasan dari Bab 1 Pendahuluan) ---
konteks_riset_html = """
    <p>Industri ritel modern, khususnya pusat perbelanjaan, memegang peran vital dalam perekonomian urban. Di Surabaya, persaingan antar mall semakin ketat, menuntut setiap pemain untuk terus meningkatkan kualitas layanannya demi menarik dan mempertahankan pengunjung.</p>
    <p>Meskipun Pakuwon City Mall (PCM) telah menunjukkan perkembangan yang pesat, evaluasi berkelanjutan terhadap kepuasan pengunjung sangat diperlukan. Penelitian ini dilakukan untuk:</p>
    <ul>
        <li>Mengidentifikasi secara komprehensif <strong>karakteristik pengunjung</strong> PCM.</li>
        <li>Menganalisis <strong>tingkat kesenjangan (GAP)</strong> antara harapan dan persepsi kenyataan pengunjung terhadap berbagai aspek layanan menggunakan kerangka SERVQUAL.</li>
        <li>Memetakan <strong>prioritas perbaikan layanan</strong> melalui Importance-Performance Analysis (IPA).</li>
        <li>Mengidentifikasi atribut dengan <strong>potensi peningkatan nilai terbesar</strong> bagi pelanggan melalui Potential Gain in Customer Value (PGCV).</li>
        <li>Mengukur <strong>tingkat kepuasan pengunjung secara keseluruhan</strong> menggunakan Customer Satisfaction Index (CSI).</li>
    </ul>
    <p>Temuan dari riset ini diharapkan dapat memberikan <strong>wawasan strategis dan rekomendasi actionable</strong> bagi manajemen Pakuwon City Mall untuk meningkatkan kualitas layanan, memperkuat loyalitas pelanggan, dan mencapai keunggulan kompetitif.</p>
"""
display_content_section(
    "Konteks dan Tujuan Riset Kepuasan Pengunjung",
    konteks_riset_html,
    icon="🎯"
)

# --- Navigasi ke Halaman Berikutnya ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='content-card' style='text-align:center;'>
        <h3 class='section-subheader-minor'>Jelajahi Lebih Lanjut</h3>
        <p class='body-text'>Silakan gunakan menu navigasi di sebelah kiri untuk melihat detail <strong>Temuan Kunci dari Pengunjung</strong> dan <strong>Rekomendasi Strategis</strong> yang kami susun untuk Pakuwon City Mall.</p>
    </div>
    """, unsafe_allow_html=True
)

# --- Footer atau Informasi Tambahan ---
st.markdown("---")
st.markdown(
    """
    <p style='text-align:center; font-size:0.9em; color:var(--light-text-color);'>
        Aplikasi Dasbor Interaktif oleh Tim Peneliti Statistika Bisnis ITS (2025)
    </p>
    """, unsafe_allow_html=True
)
