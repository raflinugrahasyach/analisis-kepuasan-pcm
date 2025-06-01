# Simpan file ini sebagai 04_🚀_Rekomendasi_Strategis_untuk_PCM.py
# di dalam folder `pages`

import streamlit as st

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_title(title, subtitle):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)

def display_content_section_header(title, icon=""): # Hanya header bagian, tanpa card
    if icon:
        st.markdown(f"<h2 class='section-subheader'>{icon} {title}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 class='section-subheader'>{title}</h2>", unsafe_allow_html=True)

# --- KONTEN HALAMAN (BAB 5 - KESIMPULAN DAN SARAN) ---

display_page_title(
    "Langkah Maju untuk Keunggulan Layanan PCM",
    "Rangkuman Temuan Kunci dan Rekomendasi Strategis Berbasis Data"
)

# --- 5.1 Kesimpulan (Diringkas menjadi Key Takeaways) ---
with st.container(border=True):
    display_content_section_header("Rangkuman Wawasan Utama dari Riset", icon="🎯")
    st.markdown(
        """
        <div class='body-text'>
        <p>Berdasarkan analisis komprehensif terhadap data kepuasan pengunjung Pakuwon City Mall Surabaya, berikut adalah poin-poin kesimpulan utama yang dapat ditarik:</p>
        <ol>
            <li>
                <strong>Profil Pengunjung Khas:</strong> Pengunjung PCM didominasi oleh laki-laki dan segmen pelajar/mahasiswa, dengan mayoritas menggunakan kendaraan pribadi. Pemahaman profil ini krusial untuk strategi yang tepat sasaran.
            </li>
            <li>
                <strong>Kualitas Layanan Umumnya Baik, Namun Ada Ruang Peningkatan:</strong> Analisis GAP SERVQUAL menunjukkan bahwa banyak aspek layanan telah memenuhi harapan. Namun, atribut seperti <strong>T1 (Kebersihan area mall)</strong> dan <strong>R3 (Fasilitas mall berfungsi baik)</strong> teridentifikasi memiliki GAP negatif, menandakan kinerja aktual belum sepenuhnya sesuai ekspektasi pada aspek krusial ini. <em>(Catatan: Sesuaikan dengan atribut GAP negatif final dari data Anda).</em>
            </li>
            <li>
                <strong>Prioritas Aksi Teridentifikasi (IPA & PGCV):</strong>
                <ul>
                    <li>Analisis IPA membantu memetakan atribut ke dalam kuadran prioritas. Atribut di Kuadran I (Kepentingan Tinggi, Kinerja Rendah) memerlukan perhatian segera.</li>
                    <li>Analisis PGCV lebih lanjut mengurutkan prioritas perbaikan, menunjukkan bahwa peningkatan pada atribut seperti <strong>T2 (Ketersediaan tempat duduk)</strong>, <strong>Rp3 (Ketanggapan petugas menyapa)</strong>, dan <strong>E3 (Ketersediaan aduan keluhan)</strong> akan memberikan peningkatan nilai terbesar bagi pengunjung. <em>(Sesuaikan dengan 3 PGCV teratas dari data Anda).</em></li>
                </ul>
            </li>
            <li>
                <strong>Tingkat Kepuasan Pengunjung Sangat Memuaskan (CSI):</strong> Secara keseluruhan, pengunjung Pakuwon City Mall menunjukkan tingkat kepuasan yang masuk dalam kategori <strong>"Sangat Puas"</strong> dengan nilai CSI sebesar <strong>84.540%</strong>. Ini adalah pencapaian positif, namun upaya berkelanjutan tetap diperlukan.
            </li>
        </ol>
        <p>Temuan ini menggarisbawahi bahwa meskipun PCM telah berhasil memberikan pengalaman yang memuaskan, fokus pada perbaikan area spesifik dapat lebih meningkatkan kepuasan dan loyalitas pengunjung.</p>
        </div>
        """, unsafe_allow_html=True
    )

# --- 5.2 Saran (Disajikan sebagai Rekomendasi Strategis) ---
with st.container(border=True):
    display_content_section_header("Rekomendasi Strategis untuk Manajemen Pakuwon City Mall", icon="💡")
    st.markdown(
        """
        <div class='body-text'>
        <p>Mengacu pada kesimpulan penelitian, berikut adalah beberapa rekomendasi strategis yang dapat dipertimbangkan oleh manajemen Pakuwon City Mall untuk lebih meningkatkan kualitas layanan dan kepuasan pengunjung:</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Menggunakan kolom untuk layout rekomendasi yang lebih menarik
    rec_col1, rec_col2 = st.columns(2)

    with rec_col1:
        st.markdown(
            """
            <div class='content-card' style='background-color: #EFF6FF;'>
            <h3 class='section-subheader-minor' style='color:#1E6091;'>1. Fokus pada Peningkatan Atribut Kritis</h3>
            <ul class='body-text'>
                <li><strong>Tingkatkan Kebersihan Area Umum (T1):</strong> Perkuat SOP dan frekuensi pembersihan, terutama di toilet, food court, dan area sirkulasi. Pertimbangkan teknologi pembersihan modern.</li>
                <li><strong>Pastikan Fungsi Optimal Fasilitas (R3):</strong> Lakukan audit rutin dan pemeliharaan preventif untuk eskalator, lift, AC, toilet, dll. Sediakan jalur pelaporan kerusakan yang responsif.</li>
                <li><strong>Perbanyak Tempat Duduk & Area Istirahat (T2 - Prioritas PGCV):</strong> Tambah dan variasikan area duduk yang nyaman di berbagai titik strategis mall untuk meningkatkan kenyamanan pengunjung.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(
            """
            <div class='content-card' style='background-color: #E6F7FF;'>
            <h3 class='section-subheader-minor' style='color:#0077B6;'>2. Optimalkan Interaksi dan Responsivitas Staf</h3>
            <ul class='body-text'>
                <li><strong>Tingkatkan Ketanggapan Petugas Menyapa (Rp3 - Prioritas PGCV):</strong> Latih staf (terutama keamanan dan informasi) untuk lebih proaktif, ramah, dan sigap dalam menyapa serta menawarkan bantuan kepada pengunjung.</li>
                <li><strong>Sediakan dan Sosialisasikan Saluran Aduan Efektif (E3 - Prioritas PGCV):</strong> Pastikan saluran untuk menyampaikan keluhan mudah diakses (digital & fisik) dan ada tindak lanjut yang jelas serta transparan.</li>
                 <li><strong>Pelatihan Layanan Prima Berkelanjutan:</strong> Berikan pelatihan reguler kepada seluruh staf frontliner mengenai standar layanan unggul, komunikasi efektif, dan penanganan keluhan.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with rec_col2:
        st.markdown(
            """
            <div class='content-card' style='background-color: #E6F7FF;'>
            <h3 class='section-subheader-minor' style='color:#0077B6;'>3. Strategi Berbasis Profil Pengunjung</h3>
            <ul class='body-text'>
                <li><strong>Sasar Segmen Pelajar/Mahasiswa:</strong> Kembangkan program promosi, diskon pelajar, atau fasilitas yang relevan (area co-working, spot foto, F&B terjangkau).</li>
                <li><strong>Perhatikan Kebutuhan Pengguna Kendaraan Pribadi:</strong> Tingkatkan kenyamanan, keamanan, dan efisiensi manajemen parkir. Pertimbangkan sistem pemandu parkir atau opsi pembayaran nontunai.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            """
            <div class='content-card' style='background-color: #EFF6FF;'>
            <h3 class='section-subheader-minor' style='color:#1E6091;'>4. Evaluasi dan Inovasi Berkelanjutan</h3>
            <ul class='body-text'>
                <li><strong>Pertahankan Kekuatan (Kuadran II IPA):</strong> Terus jaga kualitas pada atribut yang sudah dinilai baik dan penting.</li>
                <li><strong>Optimalisasi Sumber Daya (Kuadran IV IPA):</strong> Evaluasi alokasi sumber daya pada atribut yang kinerjanya tinggi namun kurang dianggap penting oleh pengunjung.</li>
                <li><strong>Survei Kepuasan Periodik:</strong> Lakukan monitoring dan evaluasi kepuasan pengunjung secara berkala untuk mengukur efektivitas program perbaikan dan mengidentifikasi tren baru.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='body-text' style='margin-top:1.5rem;'>
        <p>Implementasi rekomendasi ini diharapkan tidak hanya mempertahankan tingkat kepuasan yang sudah "Sangat Puas", tetapi juga mendorong inovasi layanan yang berkelanjutan, sehingga Pakuwon City Mall dapat terus menjadi destinasi pilihan utama di Surabaya Timur.</p>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("---")
st.markdown(
    """
    <p style='text-align:center; font-size:1em; color:var(--primary-color); font-weight:600;'>
        Terima Kasih atas Perhatian Anda!
    </p>
    <p style='text-align:center; font-size:0.9em; color:var(--light-text-color);'>
        Semoga hasil penelitian ini memberikan kontribusi positif bagi pengembangan Pakuwon City Mall Surabaya.
    </p>
    """, unsafe_allow_html=True
)
