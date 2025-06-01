# Simpan file ini sebagai 03_🚀_Rekomendasi_Strategis_untuk_PCM.py
# di dalam folder `pages`

import streamlit as st
from app import display_footer # Mengimpor fungsi footer dari app.py
import base64 # Ditambahkan untuk fungsi show_logo

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_title(title, subtitle):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_header(title, icon=""):
    if icon:
        st.markdown(f"<h2 class='section-subheader'>{icon} {title}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 class='section-subheader'>{title}</h2>", unsafe_allow_html=True)

def display_minor_subheader(title): # Definisi fungsi yang hilang ditambahkan di sini
     st.markdown(f"<h3 class='section-subheader-minor'>{title}</h3>", unsafe_allow_html=True)

# Fungsi untuk menampilkan logo (diambil dari halaman Beranda, disesuaikan)
def show_logo(image_path, width=100, caption=""):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        # Menggunakan st.image langsung karena lebih mudah untuk alignment di kolom
        st.image(f"data:image/png;base64,{encoded_string}", width=width, caption=caption if caption else None)
    except FileNotFoundError:
        st.markdown(f"<p style='text-align:center; font-style:italic; color:var(--light-text-color); font-size:0.8em;'>[Logo {caption} tidak ada]</p>", unsafe_allow_html=True)
    except Exception: # Menangkap error lain jika base64 gagal
        st.markdown(f"<p style='text-align:center; font-style:italic; color:var(--light-text-color); font-size:0.8em;'>[Gagal memuat logo {caption}]</p>", unsafe_allow_html=True)


# --- KONTEN HALAMAN (BAB 5 - KESIMPULAN DAN SARAN) ---

display_page_title(
    "Merumuskan Langkah Strategis untuk Keunggulan PCM",
    "Kesimpulan Kunci dari Riset dan Rekomendasi Aksi Berbasis Data"
)

# --- 5.1 Kesimpulan (Disajikan sebagai Key Takeaways dalam cards) ---
with st.container(border=True):
    display_section_header("Intisari Temuan Utama Riset Kepuasan Pengunjung", icon="🎯")
    st.markdown(
        """
        <div class='body-text'>
        <p>Analisis komprehensif terhadap data kepuasan pengunjung Pakuwon City Mall Surabaya menghasilkan beberapa wawasan kunci yang krusial bagi pengembangan layanan di masa depan:</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Menggunakan kolom untuk kesimpulan yang lebih menarik
    col_kes1, col_kes2 = st.columns(2)
    with col_kes1:
        st.markdown(
            """
            <div class='content-card-custom' style='background-color: #E9F5FF; height:100%;'>
                <h3 class='section-subheader-minor' style='margin-top:0;'>👤 Profil Pengunjung Khas</h3>
                <p class='body-text'>Pengunjung PCM didominasi oleh <strong>laki-laki</strong> dan segmen <strong>pelajar/mahasiswa</strong>. Mayoritas menggunakan <strong>kendaraan pribadi</strong>. Ini mengimplikasikan pentingnya strategi yang menyasar demografi ini.</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class='content-card-custom' style='background-color: #E9F5FF; margin-top:1rem; height:100%;'>
                <h3 class='section-subheader-minor' style='margin-top:0;'>🎯 Area Prioritas Teridentifikasi</h3>
                <p class='body-text'>Analisis IPA dan PGCV secara konsisten menyoroti beberapa atribut sebagai prioritas utama, seperti <strong>T2 (Ketersediaan tempat duduk)</strong>, <strong>Rp3 (Ketanggapan petugas menyapa)</strong>, dan <strong>E3 (Ketersediaan aduan keluhan)</strong>. Fokus pada area ini akan memberikan dampak terbesar.</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col_kes2:
        st.markdown(
            """
            <div class='content-card-custom' style='background-color: #E9F5FF; height:100%;'>
                <h3 class='section-subheader-minor' style='margin-top:0;'>📉 Kualitas Layanan & Ruang Peningkatan</h3>
                <p class='body-text'>Meskipun banyak aspek layanan dinilai baik (GAP positif), atribut seperti <strong>T1 (Kebersihan area mall)</strong> dan <strong>R3 (Fasilitas mall berfungsi baik)</strong> menunjukkan kinerja di bawah harapan (GAP negatif), menandakan area spesifik yang memerlukan intervensi.</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class='content-card-custom' style='background-color: #E9F5FF; margin-top:1rem; height:100%;'>
                <h3 class='section-subheader-minor' style='margin-top:0;'>⭐ Kepuasan Keseluruhan Sangat Baik</h3>
                <p class='body-text'>Secara keseluruhan, pengunjung PCM menunjukkan tingkat kepuasan yang tinggi, masuk dalam kategori <strong>"Sangat Puas"</strong> dengan nilai CSI <strong>84.540%</strong>. Ini adalah fondasi kuat untuk pengembangan lebih lanjut.</p>
            </div>
            """, unsafe_allow_html=True
        )
    
    st.markdown(
        """
        <div class='body-text' style='margin-top:1rem; padding: 1rem; background-color: #FFF3CD; border-left: 5px solid var(--accent-color); border-radius: 5px;'>
        <p>🔑 <strong>Pesan Kunci:</strong> Meskipun kepuasan umum tinggi, perbaikan terfokus pada area spesifik yang teridentifikasi (terutama kebersihan, fungsi fasilitas, dan beberapa aspek interaksi staf) dapat secara signifikan meningkatkan pengalaman pengunjung dan memperkuat loyalitas.</p>
        </div>
        """, unsafe_allow_html=True)


# --- 5.2 Saran (Disajikan sebagai Rekomendasi Strategis yang Actionable) ---
with st.container(border=True):
    display_section_header("Rekomendasi Strategis untuk Keunggulan Layanan PCM", icon="💡")
    st.markdown(
        """
        <div class='body-text'>
        <p>Berdasarkan temuan riset, berikut adalah rekomendasi strategis yang dapat dipertimbangkan oleh manajemen Pakuwon City Mall untuk meningkatkan kualitas layanan dan memperkuat posisi sebagai destinasi pilihan:</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Kategori Rekomendasi
    cat_ops, cat_sdm, cat_strategis = st.tabs(["🛠️ Operasional & Fasilitas", "🤝 Interaksi & SDM", "📈 Strategi & Inovasi"])

    with cat_ops:
        display_minor_subheader("Peningkatan Aspek Operasional dan Fasilitas Kunci")
        st.markdown(
            """
            <div class='body-text'>
            <ul>
                <li><strong>Prioritaskan Kebersihan Menyeluruh (T1):</strong> Implementasikan standar kebersihan yang lebih tinggi dan frekuensi pembersihan yang lebih intensif, khususnya pada area vital seperti toilet, food court, mushola, dan jalur sirkulasi utama. Pertimbangkan audit kebersihan oleh pihak ketiga.</li>
                <li><strong>Jamin Keandalan Fungsi Fasilitas (R3):</strong> Lakukan program pemeliharaan preventif yang terjadwal dan audit rutin untuk semua fasilitas krusial (eskalator, lift, AC, toilet, sistem penerangan). Pastikan respons perbaikan cepat dan efektif.</li>
                <li><strong>Optimalkan Ketersediaan Tempat Duduk & Area Istirahat (T2 - Prioritas PGCV):</strong> Tingkatkan jumlah dan variasi tempat duduk yang nyaman dan strategis di berbagai area mall. Ciptakan zona istirahat tematik yang menarik.</li>
                <li><strong>Tingkatkan Aksesibilitas dan Manajemen Parkir (T4):</strong> Evaluasi dan optimalkan sistem manajemen parkir untuk kemudahan akses, sirkulasi, dan keamanan. Pertimbangkan teknologi pemandu parkir dan opsi pembayaran digital yang lebih beragam.</li>
                <li><strong>Sempurnakan Papan Penunjuk Arah (T3):</strong> Pastikan sistem navigasi (<i>wayfinding</i>) di dalam mall jelas, informatif, mudah dipahami, dan konsisten di semua area, termasuk penggunaan teknologi digital jika memungkinkan.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with cat_sdm:
        display_minor_subheader("Penguatan Interaksi Pelanggan dan Pengembangan SDM")
        st.markdown(
            """
            <div class='body-text'>
            <ul>
                <li><strong>Tingkatkan Responsivitas dan Keramahan Petugas (Rp3 - Prioritas PGCV):</strong> Latih seluruh staf frontliner (keamanan, informasi, kebersihan) untuk lebih proaktif, ramah, sigap dalam menyapa, dan tulus dalam menawarkan bantuan. Budayakan senyum dan kontak mata positif.</li>
                <li><strong>Optimalkan Sistem Penanganan Keluhan (E3 - Prioritas PGCV):</strong> Sediakan dan sosialisasikan berbagai saluran yang mudah diakses bagi pengunjung untuk menyampaikan keluhan atau masukan (digital dan fisik). Pastikan ada prosedur tindak lanjut yang jelas, cepat, dan transparan.</li>
                <li><strong>Pastikan Kesabaran Petugas dalam Melayani (E2):</strong> Tekankan pentingnya kesabaran dan empati dalam interaksi dengan pengunjung, terutama dalam situasi yang memerlukan penjelasan atau penanganan masalah.</li>
                 <li><strong>Implementasikan Program Pelatihan Layanan Prima (<i>Service Excellence</i>) Berkelanjutan:</strong> Adakan sesi pelatihan reguler untuk semua staf terkait standar layanan, komunikasi efektif, penanganan situasi sulit, dan pengetahuan produk/layanan mall.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with cat_strategis:
        display_minor_subheader("Inovasi Strategis dan Evaluasi Berkelanjutan")
        st.markdown(
            """
            <div class='body-text'>
            <ul>
                <li><strong>Kembangkan Program yang Menyasar Segmen Kunci (Pelajar/Mahasiswa):</strong> Rancang promosi, acara, atau fasilitas khusus yang menarik bagi segmen pelajar/mahasiswa, seperti diskon khusus, area <i>co-working</i>, atau kompetisi kreatif.</li>
                <li><strong>Permudah Akses Informasi Promo dan Acara (R2):</strong> Manfaatkan berbagai platform digital (aplikasi mobile PCM, media sosial, website) dan fisik (direktori digital, papan informasi) untuk menyebarkan informasi acara dan promosi secara efektif dan mudah diakses.</li>
                <li><strong>Pertahankan dan Tingkatkan Aspek Unggulan:</strong> Terus jaga kualitas pada atribut-atribut yang sudah dinilai baik dan penting oleh pengunjung (Kuadran II IPA). Inovasi pada area kekuatan dapat menjadi diferensiasi positif.</li>
                <li><strong>Lakukan Survei Kepuasan Pelanggan Secara Periodik:</strong> Jadwalkan pelaksanaan survei kepuasan secara reguler (misalnya, per semester atau per tahun) untuk memantau efektivitas program perbaikan, mengidentifikasi perubahan ekspektasi pelanggan, dan menjaga layanan tetap relevan.</li>
                <li><strong>Benchmarking dengan Kompetitor:</strong> Lakukan studi banding (<i>benchmarking</i>) secara berkala dengan pusat perbelanjaan sejenis untuk mendapatkan perspektif yang lebih luas dan mengidentifikasi praktik terbaik di industri.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown(
        """
        <div class='body-text' style='margin-top:1.5rem; padding: 1rem; background-color: #D1F2EB; border-left: 5px solid var(--primary-color); border-radius: 5px;'>
        <p>🚀 <strong>Langkah Selanjutnya:</strong> Implementasi rekomendasi ini, disertai dengan komitmen kuat dari seluruh jajaran manajemen dan staf, akan menjadi kunci bagi Pakuwon City Mall untuk tidak hanya mempertahankan tingkat kepuasan yang tinggi, tetapi juga untuk terus berinovasi dan menjadi destinasi gaya hidup terdepan yang selalu relevan dengan kebutuhan pengunjungnya.</p>
        </div>
        """, unsafe_allow_html=True)


# --- Bagian Tim Peneliti dan Ucapan Terima Kasih ---
# Ini akan dipanggil oleh fungsi display_footer() dari app.py
# Jadi tidak perlu didefinisikan ulang di sini jika display_footer() sudah mencakupnya.
# Namun, jika ingin kustomisasi khusus untuk halaman ini, bisa ditambahkan di sini.

# Panggil fungsi footer
display_footer()
