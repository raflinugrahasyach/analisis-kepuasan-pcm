# Simpan file ini sebagai 01_✨_Selamat_Datang.py
# di dalam folder `pages`

import streamlit as st
from app import display_footer # Mengimpor fungsi footer dari app.py

# --- Fungsi Bantuan Spesifik Halaman (jika perlu) atau gunakan global ---
# Mengasumsikan CSS global dari app.py sudah diterapkan.

def display_page_title(title, subtitle):
    """Menampilkan judul utama halaman dan subjudulnya."""
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_header(title, icon=""):
    """Menampilkan header bagian konten."""
    if icon:
        st.markdown(f"<h2 class='section-subheader'>{icon} {title}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 class='section-subheader'>{title}</h2>", unsafe_allow_html=True)

# --- KONTEN HALAMAN SELAMAT DATANG ---

display_page_title(
    "Dasbor Analisis Kepuasan Pengunjung Pakuwon City Mall",
    "Mengungkap Wawasan untuk Peningkatan Layanan Berkelanjutan"
)

# --- Sekilas Tentang Pakuwon City Mall Surabaya ---
with st.container(border=True):
    display_section_header("Mengenal Pakuwon City Mall Surabaya", icon="🛍️")
    
    col1_pcm, col2_pcm = st.columns([1, 2])
    with col1_pcm:
        # Anda bisa mengganti ini dengan gambar PCM yang menarik jika ada
        # st.image("assets/pcm_image.jpg", caption="Pakuwon City Mall Surabaya")
        st.markdown("<div style='display: flex; align-items: center; justify-content: center; height: 100%; font-size: 5rem; background-color: #e9ecef; border-radius: 10px;'>🏬</div>", unsafe_allow_html=True)


    with col2_pcm:
        st.markdown(
            """
            <div class='body-text'>
            Pakuwon City Mall (PCM) Surabaya, yang secara resmi beroperasi sejak akhir tahun 2020, dengan cepat memantapkan dirinya sebagai salah satu destinasi gaya hidup (<i>lifestyle mall</i>) premium di kawasan strategis Surabaya Timur. Sebagai bagian integral dari pengembangan superblok Pakuwon City, mall ini dirancang untuk memenuhi kebutuhan dan aspirasi segmen pasar menengah ke atas.
            <br><br>
            Dengan arsitektur modern, luas area yang representatif (lebih dari 60.000 m²), dan koleksi lebih dari 200 gerai yang mencakup merek-merek ternama baik lokal maupun internasional, PCM menawarkan pengalaman berbelanja, kuliner, dan hiburan yang komprehensif. Lebih dari sekadar pusat perbelanjaan, PCM juga berfungsi sebagai episentrum kegiatan sosial dan rekreasi bagi masyarakat urban, didukung oleh lokasinya yang dekat dengan berbagai fasilitas publik dan institusi pendidikan tinggi.
            <br><br>
            Dalam lanskap industri ritel Surabaya yang dinamis dan kompetitif, pemahaman mendalam terhadap ekspektasi dan tingkat kepuasan pengunjung menjadi faktor krusial bagi PCM untuk terus berinovasi, meningkatkan kualitas layanan, dan memperkuat posisinya sebagai pilihan utama masyarakat.
            </div>
            """, unsafe_allow_html=True)

# --- Konteks dan Tujuan Riset (Ringkasan dari Bab 1 Pendahuluan) ---
with st.container(border=True):
    display_section_header("Mengapa Riset Ini Penting bagi PCM? (Konteks & Tujuan)", icon="🎯")
    st.markdown(
        """
        <div class='body-text'>
        Industri ritel modern menghadapi tantangan konstan untuk memenuhi ekspektasi pelanggan yang terus berkembang. Di tengah persaingan yang ketat, kualitas layanan menjadi pembeda utama dan kunci untuk membangun loyalitas pengunjung. Pakuwon City Mall, sebagai pemain penting di Surabaya Timur, memerlukan data dan wawasan akurat untuk terus meningkatkan daya tariknya.
        <br><br>
        Penelitian ini dilakukan dengan tujuan utama untuk:
        <ul>
            <li><strong>Memahami Profil Pengunjung:</strong> Mengidentifikasi secara detail siapa saja yang mengunjungi PCM, meliputi karakteristik demografis dan perilaku mereka.</li>
            <li><strong>Mengevaluasi Kualitas Layanan:</strong> Menganalisis persepsi pengunjung terhadap berbagai aspek layanan yang ditawarkan PCM dibandingkan dengan harapan mereka (menggunakan kerangka SERVQUAL).</li>
            <li><strong>Mengidentifikasi Area Prioritas:</strong> Menentukan aspek layanan mana yang paling krusial untuk ditingkatkan berdasarkan tingkat kepentingan bagi pengunjung dan kinerja aktual PCM (melalui Importance-Performance Analysis).</li>
            <li><strong>Mengukur Kepuasan Global:</strong> Menyediakan ukuran kuantitatif mengenai tingkat kepuasan pengunjung secara keseluruhan (menggunakan Customer Satisfaction Index).</li>
        </ul>
        Temuan dari riset ini dirancang untuk memberikan <strong>rekomendasi strategis yang konkret dan berbasis data</strong> kepada manajemen Pakuwon City Mall, guna mendukung upaya peningkatan kualitas layanan secara berkelanjutan dan memperkuat posisi kompetitif di pasar.
        </div>
        """, unsafe_allow_html=True
    )

# --- Navigasi ke Halaman Berikutnya ---
st.markdown("<br>", unsafe_allow_html=True)
with st.container(border=True):
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        st.markdown(
        """
        <div class='body-text' style='padding:1rem; text-align:center;'>
            <h3 class='section-subheader-minor'>Apa Kata Pengunjung?</h3>
            <p>Selami lebih dalam temuan-temuan kunci dari analisis data survei kepuasan pengunjung PCM.</p>
        </div>
        """, unsafe_allow_html=True)
        # st.page_link("pages/02_📊_Temuan_Kunci_Kepuasan_Pengunjung.py", label="Lihat Temuan Kunci", icon="📊")
        # Tombol manual jika page_link tidak berfungsi sesuai harapan di semua environment
        if st.button("📊 Lihat Temuan Kunci", use_container_width=True):
            st.switch_page("pages/02_📊_Temuan_Kunci_Kepuasan_Pengunjung.py")


    with col_nav2:
        st.markdown(
        """
        <div class='body-text' style='padding:1rem; text-align:center;'>
            <h3 class='section-subheader-minor'>Langkah Strategis Berikutnya</h3>
            <p>Temukan rekomendasi konkret dan langkah aksi yang dapat diambil PCM untuk meningkatkan layanan.</p>
        </div>
        """, unsafe_allow_html=True)
        # st.page_link("pages/03_🚀_Rekomendasi_Strategis_untuk_PCM.py", label="Lihat Rekomendasi Strategis", icon="🚀")
        if st.button("🚀 Lihat Rekomendasi Strategis", use_container_width=True):
            st.switch_page("pages/03_🚀_Rekomendasi_Strategis_untuk_PCM.py")


# Panggil fungsi footer
display_footer()
