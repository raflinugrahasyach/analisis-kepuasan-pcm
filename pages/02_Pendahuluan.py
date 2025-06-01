# Simpan file ini sebagai 02_Pendahuluan.py
# di dalam folder `pages` (misalnya, final_project_streamlit/pages/02_Pendahuluan.py)

import streamlit as st

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_header(title, subtitle=""):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='body-text' style='text-align:center; font-size:1.1em; font-style:italic; margin-bottom:1.5rem;'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_subheader(title):
    st.markdown(f"<h2 class='sub-header'>{title}</h2>", unsafe_allow_html=True)

# --- Konten Halaman Pendahuluan ---
# Setiap bagian akan menggunakan st.expander untuk tampilan yang lebih rapi

display_page_header("BAB I: Pendahuluan", "Dasar Pemikiran dan Ruang Lingkup Penelitian")

with st.expander("💡 1.1 Latar Belakang Penelitian", expanded=True):
    st.markdown(
        """
        <div class='body-text'>
        <p>
        Industri ritel modern, termasuk pusat perbelanjaan (mall), memegang peranan krusial dalam dinamika ekonomi nasional, khususnya sebagai motor penggerak pembangunan di kawasan urban. Data Badan Pusat Statistik (BPS) secara konsisten menunjukkan kontribusi signifikan sektor perdagangan besar dan eceran terhadap Produk Domestik Bruto (PDB) Indonesia. Di tingkat regional, Surabaya sebagai kota metropolitan terbesar kedua di Indonesia, mencerminkan tren serupa. Tingginya tingkat okupansi pusat perbelanjaan di Surabaya, sebagaimana dilaporkan oleh Colliers Indonesia (2023) yang mencapai 83,6%, mengindikasikan aktivitas konsumen yang kuat dan peran penting mall dalam kehidupan masyarakat perkotaan.
        </p>
        <p>
        Pakuwon City Mall (PCM), yang beroperasi sejak akhir tahun 2020, merupakan salah satu pemain baru dalam lanskap ritel Surabaya Timur. Dirancang sebagai <i>lifestyle mall</i> premium yang terintegrasi dalam kawasan superblok Pakuwon City, PCM menyasar segmen konsumen kelas menengah ke atas. Sebagai entitas yang relatif baru, PCM menghadapi tantangan untuk secara kontinu menyesuaikan dan meningkatkan kualitas layanannya demi memenuhi ekspektasi konsumen yang beragam dan dinamis. Kualitas layanan, sebagaimana ditunjukkan oleh berbagai studi (misalnya, Japarianto, 2019), merupakan determinan penting yang mempengaruhi persepsi kualitas secara keseluruhan dan minat kunjungan ulang pelanggan.
        </p>
        <p>
        Meskipun model SERVQUAL (yang mencakup dimensi Tangible, Reliability, Responsiveness, Assurance, dan Empathy) telah banyak diterapkan untuk mengukur kualitas layanan (Saripudin, 2021), penelitian yang spesifik dan komprehensif mengevaluasi tingkat kepuasan pengunjung Pakuwon City Mall masih terbatas. Padahal, tinjauan awal melalui platform publik seperti Google Maps mengindikasikan adanya sejumlah ulasan dari pengunjung yang menyoroti aspek fasilitas dan layanan yang dirasa kurang memuaskan. Kesenjangan antara layanan yang diharapkan dan yang dirasakan ini berpotensi mempengaruhi citra dan daya saing mall dalam jangka panjang.
        </p>
        <p>
        Oleh karena itu, penelitian ini diusulkan untuk melakukan analisis mendalam terhadap tingkat kepuasan pengunjung Pakuwon City Mall. Dengan mengintegrasikan beberapa metode analisis, yaitu SERVQUAL untuk mengukur kesenjangan kualitas layanan, Importance Performance Analysis (IPA) untuk memetakan prioritas perbaikan, Potential Gain in Customer Value (PGCV) untuk mengidentifikasi atribut dengan potensi peningkatan nilai tertinggi bagi pelanggan, dan Customer Satisfaction Index (CSI) untuk mengukur tingkat kepuasan secara keseluruhan, penelitian ini bertujuan memberikan rekomendasi strategis yang berbasis data dan <i>actionable</i> bagi manajemen PCM dalam upaya peningkatan kualitas layanan secara berkelanjutan.
        </p>
        </div>
        """, unsafe_allow_html=True
    )

with st.expander("❓ 1.2 Rumusan Masalah", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p>Berdasarkan latar belakang yang telah diuraikan, rumusan masalah yang akan dijawab dalam penelitian ini adalah sebagai berikut:</p>
        <ol>
            <li>Bagaimana karakteristik demografis dan perilaku pengunjung Pakuwon City Mall Surabaya?</li>
            <li>Bagaimana tingkat kesenjangan (GAP) antara harapan (<i>importance</i>) dan persepsi kenyataan (<i>performance</i>) pengunjung terhadap kualitas layanan Pakuwon City Mall berdasarkan lima dimensi SERVQUAL (Tangibles, Reliability, Responsiveness, Assurance, Empathy)?</li>
            <li>Atribut layanan manakah yang menjadi prioritas utama untuk ditingkatkan oleh manajemen Pakuwon City Mall berdasarkan hasil analisis Importance-Performance Analysis (IPA)?</li>
            <li>Bagaimana urutan prioritas perbaikan atribut layanan Pakuwo City Mall berdasarkan analisis Potential Gain in Customer Value (PGCV)?</li>
            <li>Berapakah nilai Customer Satisfaction Index (CSI) yang mencerminkan tingkat kepuasan pengunjung Pakuwon City Mall secara keseluruhan?</li>
        </ol>
        </div>
        """, unsafe_allow_html=True
    )

with st.expander("🎯 1.3 Tujuan Penelitian", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p>Sejalan dengan rumusan masalah yang telah ditetapkan, tujuan dari penelitian ini adalah:</p>
        <ol>
            <li>Mengidentifikasi dan mendeskripsikan karakteristik demografis serta perilaku pengunjung Pakuwon City Mall Surabaya.</li>
            <li>Menganalisis dan mengukur tingkat kesenjangan (GAP) antara harapan dan persepsi kenyataan pengunjung terhadap kualitas layanan Pakuwon City Mall pada setiap atribut dalam lima dimensi SERVQUAL.</li>
            <li>Memetakan atribut-atribut layanan Pakuwon City Mall ke dalam matriks Importance-Performance Analysis (IPA) untuk menentukan prioritas perbaikan dan strategi pengelolaan.</li>
            <li>Menentukan urutan prioritas perbaikan atribut layanan Pakuwon City Mall yang memiliki potensi peningkatan nilai tertinggi bagi pelanggan menggunakan metode PGCV.</li>
            <li>Menghitung dan menginterpretasikan nilai Customer Satisfaction Index (CSI) untuk mengetahui tingkat kepuasan pengunjung Pakuwon City Mall secara komprehensif.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True
    )
    
with st.expander("🌟 1.4 Manfaat Penelitian", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p>Penelitian ini diharapkan dapat memberikan manfaat yang signifikan bagi berbagai pihak, antara lain:</p>
        <ul>
            <li><b>Bagi Manajemen Pakuwon City Mall:</b>
                <ul>
                    <li>Menyediakan data dan analisis empiris yang valid mengenai tingkat kepuasan pengunjung serta persepsi terhadap kualitas layanan yang diberikan.</li>
                    <li>Memberikan rekomendasi konkret dan prioritas perbaikan layanan yang dapat diimplementasikan untuk meningkatkan kepuasan dan loyalitas pengunjung.</li>
                    <li>Menjadi dasar pengambilan keputusan strategis dalam alokasi sumber daya untuk peningkatan kualitas layanan dan fasilitas.</li>
                </ul>
            </li>
            <li><b>Bagi Akademisi dan Peneliti:</b>
                <ul>
                    <li>Menambah khazanah literatur ilmiah dalam bidang manajemen pemasaran, khususnya terkait analisis kepuasan pelanggan dan kualitas layanan di industri ritel (pusat perbelanjaan).</li>
                    <li>Menyajikan contoh aplikasi praktis dari integrasi metode SERVQUAL, IPA, PGCV, dan CSI dalam konteks studi kasus nyata.</li>
                    <li>Dapat menjadi referensi dan dasar untuk penelitian selanjutnya yang lebih mendalam atau dengan cakupan yang lebih luas.</li>
                </ul>
            </li>
            <li><b>Bagi Penulis:</b>
                <ul>
                    <li>Meningkatkan pemahaman teoretis dan kemampuan praktis dalam merancang, melaksanakan, dan menganalisis penelitian kuantitatif di bidang sosial dan bisnis.</li>
                    <li>Mengembangkan keterampilan dalam penggunaan berbagai metode analisis statistik dan interpretasi hasil penelitian.</li>
                </ul>
            </li>
            <li><b>Bagi Konsumen dan Masyarakat Umum:</b>
                <ul>
                    <li>Memberikan gambaran objektif mengenai kualitas layanan yang ditawarkan oleh Pakuwon City Mall, yang dapat menjadi informasi bagi calon pengunjung.</li>
                    <li>Secara tidak langsung, hasil penelitian yang diimplementasikan dapat berkontribusi pada peningkatan pengalaman berbelanja dan rekreasi masyarakat.</li>
                </ul>
            </li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )

with st.expander("🚧 1.5 Batasan Masalah", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p>Untuk menjaga fokus dan kedalaman analisis, serta mempertimbangkan keterbatasan sumber daya dan waktu, penelitian ini memiliki beberapa batasan sebagai berikut:</p>
        <ul>
            <li><b>Objek Penelitian:</b> Penelitian ini difokuskan pada pengunjung Pakuwon City Mall Surabaya yang telah melakukan kunjungan dan menggunakan fasilitas atau layanan mall.</li>
            <li><b>Lokasi dan Waktu Pengambilan Data:</b> Pengambilan data primer (survei kuesioner) dilakukan di area pintu keluar utama Pakuwon City Mall Surabaya pada periode waktu tertentu yang telah ditetapkan (misalnya, selama 7 hari survei yang mencakup hari kerja dan akhir pekan).</li>
            <li><b>Variabel yang Diteliti:</b> Dimensi kualitas layanan yang diukur mengacu pada kerangka SERVQUAL yang telah disesuaikan dengan konteks pusat perbelanjaan. Faktor-faktor lain di luar dimensi SERVQUAL yang mungkin mempengaruhi kepuasan (misalnya, harga produk tenant, promosi spesifik tenant) tidak menjadi fokus utama penelitian ini.</li>
            <li><b>Metode Analisis:</b> Penelitian ini menggunakan metode SERVQUAL, IPA, PGCV, dan CSI. Metode analisis lain yang mungkin relevan tidak diaplikasikan dalam studi ini.</li>
            <li><b>Generalisasi Hasil:</b> Hasil penelitian ini mungkin tidak dapat digeneralisasi secara langsung ke semua pusat perbelanjaan lain, mengingat karakteristik unik dari Pakuwon City Mall dan sampel pengunjungnya.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )
