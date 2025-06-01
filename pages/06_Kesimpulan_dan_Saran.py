# Simpan file ini sebagai 06_Kesimpulan_dan_Saran.py
# di dalam folder `pages` (misalnya, final_project_streamlit/pages/06_Kesimpulan_dan_Saran.py)

import streamlit as st

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_header(title, subtitle=""):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='body-text' style='text-align:center; font-size:1.1em; font-style:italic; margin-bottom:1.5rem;'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_subheader(title):
    st.markdown(f"<h2 class='sub-header'>{title}</h2>", unsafe_allow_html=True)

# --- Konten Halaman Kesimpulan dan Saran ---
display_page_header("BAB V: Kesimpulan dan Saran", "Ringkasan Temuan Utama dan Rekomendasi Strategis")

with st.container(border=True):
    display_section_subheader("📌 5.1 Kesimpulan Penelitian")
    st.markdown(
        """
        <div class='body-text'>
        <p>Berdasarkan analisis data yang telah dilakukan secara komprehensif terhadap tingkat kepuasan pengunjung Pakuwon City Mall Surabaya menggunakan metode SERVQUAL, Importance-Performance Analysis (IPA), dan Customer Satisfaction Index (CSI), dapat ditarik beberapa kesimpulan penting sebagai berikut:</p>
        <ol>
            <li>
                <b>Profil Karakteristik Pengunjung:</b> Pengunjung Pakuwon City Mall didominasi oleh jenis kelamin <b>laki-laki (58,65%)</b> dan kelompok pekerjaan <b>Pelajar/Mahasiswa (40,2%)</b>. Usia rata-rata pengunjung adalah sekitar <b>23 tahun</b>, dan mayoritas menggunakan <b>kendaraan pribadi (sepeda motor dan mobil masing-masing 43,7%)</b>. Pemahaman terhadap profil ini menjadi dasar penting untuk penyesuaian strategi layanan dan pemasaran.
            </li>
            <li>
                <b>Evaluasi Kualitas Layanan (Analisis GAP SERVQUAL):</b> Secara umum, kualitas layanan Pakuwon City Mall menunjukkan kinerja yang cukup baik, di mana sebagian besar atribut layanan mendapatkan skor persepsi (kenyataan) yang telah memenuhi atau bahkan melebihi skor harapan pengunjung (ditandai dengan GAP positif). Meskipun demikian, teridentifikasi beberapa atribut layanan yang menunjukkan adanya kesenjangan negatif (GAP negatif), yaitu <b>T1 (Kebersihan area umum)</b> dengan GAP -0.07 dan <b>R3 (Fasilitas mall berfungsi baik)</b> dengan GAP -0.02. Hal ini mengindikasikan bahwa pada aspek-aspek tersebut, kinerja aktual Pakuwon City Mall belum sepenuhnya memenuhi ekspektasi pengunjung.
            </li>
            <li>
                <b>Prioritas Peningkatan Layanan (Analisis IPA):</b> Pemetaan atribut-atribut layanan ke dalam matriks Importance-Performance Analysis (IPA) membantu mengidentifikasi area-area strategis untuk peningkatan. Atribut yang berada dalam <b>Kuadran I (Prioritas Utama)</b>—yaitu atribut yang dianggap sangat penting oleh pengunjung namun kinerjanya masih dinilai rendah—harus menjadi fokus utama upaya perbaikan oleh manajemen PCM. <i>(Identifikasi atribut spesifik di Kuadran I akan bergantung pada hasil olah data primer penelitian Anda).</i>
            </li>
            <li>
                <b>Tingkat Kepuasan Pengunjung Secara Keseluruhan (Analisis CSI):</b> Berdasarkan perhitungan Customer Satisfaction Index (CSI) dengan menggunakan data olahan yang tersedia, tingkat kepuasan pengunjung Pakuwon City Mall secara keseluruhan berada pada angka sekitar <b>[Nilai CSI Aktual dari Penelitian Anda, contoh: 78.52%]</b>. Nilai ini mengklasifikasikan tingkat kepuasan pengunjung dalam kategori <b>[Kategori CSI Aktual, contoh: Puas]</b>. Meskipun hasil ini menunjukkan tingkat kepuasan yang positif, tetap terdapat ruang untuk peningkatan lebih lanjut guna mencapai kategori 'Sangat Puas' dan memperkuat posisi kompetitif PCM.
            </li>
            <li>
                <b>Potensi Peningkatan Nilai bagi Pelanggan (Analisis PGCV - jika dilakukan):</b> Jika analisis Potential Gain in Customer Value (PGCV) dilakukan, maka akan dapat diidentifikasi urutan prioritas atribut layanan yang, jika ditingkatkan kinerjanya, akan memberikan dampak peningkatan nilai dan kepuasan terbesar bagi pelanggan.
            </li>
        </ol>
        <p>Kesimpulan ini menggarisbawahi bahwa meskipun Pakuwon City Mall telah berhasil memberikan layanan yang cukup memuaskan pada banyak aspek, upaya perbaikan yang terfokus, terukur, dan berkelanjutan pada area-area kunci yang teridentifikasi sangat diperlukan untuk meningkatkan pengalaman pengunjung secara menyeluruh, memperkuat loyalitas pelanggan, dan mempertahankan daya saing di industri ritel yang semakin kompetitif.</p>
        </div>
        """, unsafe_allow_html=True
    )

with st.container(border=True):
    display_section_subheader("💡 5.2 Saran dan Rekomendasi")
    st.markdown(
        """
        <div class='body-text'>
        <p>Mengacu pada kesimpulan hasil penelitian, berikut adalah beberapa saran dan rekomendasi strategis yang dapat dipertimbangkan oleh manajemen Pakuwon City Mall Surabaya untuk meningkatkan kualitas layanan dan kepuasan pengunjung:</p>
        <ol>
            <li>
                <b>Fokus pada Perbaikan Atribut Kritis (Prioritas Utama dari IPA dan GAP Negatif):</b>
                <ul>
                    <li><b>Peningkatan Kebersihan Area Umum (T1):</b> Mengintensifkan jadwal dan standar prosedur operasional (SOP) kebersihan di seluruh area mall, terutama pada fasilitas vital seperti toilet, area food court, mushola, dan jalur sirkulasi utama. Mempertimbangkan penambahan personel kebersihan pada jam-jam puncak kunjungan dan penggunaan teknologi pembersihan yang lebih efektif.</li>
                    <li><b>Optimalisasi Fungsi dan Keandalan Fasilitas Mall (R3):</b> Melakukan audit rutin dan program pemeliharaan preventif secara berkala terhadap semua fasilitas penting (eskalator, lift, sistem pendingin udara, penerangan, fasilitas toilet, dll.) untuk memastikan semuanya berfungsi optimal, aman, dan nyaman digunakan. Menyediakan jalur pelaporan kerusakan fasilitas yang mudah diakses oleh pengunjung dan memastikan respons perbaikan yang cepat.</li>
                    <li><i>(Tambahkan atribut lain yang masuk Kuadran I IPA dari hasil penelitian Anda).</i></li>
                </ul>
            </li>
            <li>
                <b>Strategi Pemasaran dan Layanan yang Disesuaikan dengan Profil Pengunjung:</b>
                <ul>
                    <li>Mengingat dominasi pelajar/mahasiswa, pertimbangkan untuk mengembangkan program promosi, diskon khusus pelajar, atau acara yang menarik bagi segmen usia muda. Menyediakan fasilitas pendukung seperti area co-working/belajar dengan Wi-Fi gratis, spot foto yang <i>instagramable</i>, dan pilihan F&B yang variatif dan terjangkau.</li>
                    <li>Memperhatikan kebutuhan pengunjung laki-laki dengan menyediakan tenant atau layanan yang relevan dengan minat mereka.</li>
                    <li>Meningkatkan kenyamanan, keamanan, dan efisiensi sistem manajemen parkir, mengingat tingginya penggunaan kendaraan pribadi. Pertimbangkan implementasi sistem pemandu parkir (<i>parking guidance system</i>), opsi pembayaran nontunai yang beragam, atau penambahan kapasitas area parkir jika memungkinkan.</li>
                </ul>
            </li>
            <li>
                <b>Penguatan dan Inovasi pada Atribut Unggulan (Kuadran II IPA):</b>
                <ul>
                    <li>Terus mempertahankan dan bahkan meningkatkan kualitas pada atribut-atribut layanan yang telah dinilai sangat baik dan penting oleh pengunjung. Inovasi berkelanjutan pada area-area yang sudah menjadi kekuatan PCM dapat menjadi diferensiasi positif dan meningkatkan daya tarik mall.</li>
                </ul>
            </li>
            <li>
                <b>Optimalisasi Alokasi Sumber Daya (Evaluasi Kuadran IV IPA):</b>
                <ul>
                    <li>Mengevaluasi kembali alokasi sumber daya (tenaga kerja, biaya, waktu) yang digunakan untuk atribut-atribut yang dinilai kurang penting oleh pengunjung namun kinerjanya sudah sangat tinggi. Pertimbangkan kemungkinan realokasi sebagian sumber daya tersebut untuk mendukung perbaikan pada atribut-atribut di Kuadran I yang lebih krusial.</li>
                </ul>
            </li>
            <li>
                <b>Peningkatan Kualitas Sumber Daya Manusia (Staf Layanan):</b>
                <ul>
                    <li>Melakukan program pelatihan dan pengembangan secara reguler bagi seluruh staf yang berinteraksi langsung dengan pengunjung (<i>frontliners</i>), termasuk petugas keamanan, petugas kebersihan, staf informasi, dan lainnya. Fokus pelatihan pada standar layanan prima (<i>service excellence</i>), kemampuan komunikasi efektif, empati, penanganan keluhan secara profesional, dan pengetahuan produk/layanan mall.</li>
                </ul>
            </li>
            <li>
                <b>Pengembangan Mekanisme Umpan Balik dan Sistem Evaluasi Berkelanjutan:</b>
                <ul>
                    <li>Menyediakan dan mempromosikan berbagai saluran yang mudah diakses bagi pengunjung untuk memberikan umpan balik, kritik, dan saran (misalnya, melalui aplikasi mobile PCM, kios digital interaktif, formulir online, atau kotak saran fisik yang strategis).</li>
                    <li>Melakukan survei kepuasan pelanggan secara periodik (misalnya, setiap enam bulan atau satu tahun sekali) untuk memantau efektivitas implementasi program perbaikan dan mengidentifikasi perubahan tren dalam ekspektasi dan persepsi pelanggan.</li>
                </ul>
            </li>
            <li>
                <b>Saran untuk Penelitian Selanjutnya:</b>
                <ul>
                    <li>Penelitian mendatang dapat mengeksplorasi lebih dalam faktor-faktor lain di luar dimensi SERVQUAL yang signifikan mempengaruhi loyalitas dan niat kunjungan ulang pengunjung PCM, seperti pengalaman emosional (<i>emotional experience</i>), pengaruh media sosial, atau citra merek (<i>brand image</i>).</li>
                    <li>Melakukan analisis komparatif (<i>benchmarking</i>) dengan pusat perbelanjaan sejenis lainnya di Surabaya untuk mendapatkan perspektif yang lebih luas mengenai posisi kompetitif PCM.</li>
                    <li>Mengkaji dampak jangka panjang dari implementasi rekomendasi yang diberikan dalam penelitian ini terhadap perubahan tingkat kepuasan dan kinerja bisnis Pakuwon City Mall.</li>
                </ul>
            </li>
        </ol>
        </div>
        """, unsafe_allow_html=True
    )
