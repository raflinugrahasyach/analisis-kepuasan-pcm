# Simpan file ini sebagai 03_Tinjauan_Pustaka.py
# di dalam folder `pages` (misalnya, final_project_streamlit/pages/03_Tinjauan_Pustaka.py)

import streamlit as st

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_header(title, subtitle=""):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='body-text' style='text-align:center; font-size:1.1em; font-style:italic; margin-bottom:1.5rem;'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_subheader(title): # Didefinisikan ulang agar bisa dipanggil
    st.markdown(f"<h2 class='sub-header'>{title}</h2>", unsafe_allow_html=True)

# --- Konten Halaman Tinjauan Pustaka ---
# Menggunakan st.tabs untuk memisahkan setiap konsep utama

display_page_header("BAB II: Tinjauan Pustaka", "Landasan Teori dan Konsep-Konsep Kunci Penelitian")

tab_titles = [
    "📚 Penelitian Terdahulu",
    "📊 SERVQUAL", 
    "🗺️ IPA", 
    "📈 CSI", 
    "💰 PGCV", 
    "🛍️ Pakuwon City Mall"
]
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tab_titles)

with tab1:
    display_section_subheader("2.1 Penelitian Terdahulu")
    st.markdown(
        """
        <div class='body-text'>
        <p>Penelitian mengenai kualitas layanan dan kepuasan pelanggan di pusat perbelanjaan telah banyak dilakukan. Beberapa studi relevan yang menjadi acuan dan perbandingan dalam penelitian ini antara lain:</p>
        <ul>
            <li>
                <b>Wibowo & Muflihah (2022)</b> menganalisis kualitas pelayanan terhadap kepuasan pelanggan di Sanjaya Fitness menggunakan metode Servqual dan IPA. Hasilnya menunjukkan dimensi tangible memiliki GAP paling negatif, dan IPA mengidentifikasi prioritas perbaikan seperti ketersediaan alat dan respons terhadap kritik.
            </li>
            <li>
                <b>Septiardy (2014)</b> melakukan studi peningkatan kualitas pelayanan di Kebun Binatang Surabaya menggunakan model ServQual, Kano, HoQ, dan incremental analysis. Ditemukan bahwa mayoritas atribut masih dalam kategori <i>basic needs</i> dan memiliki GAP negatif.
            </li>
            <li>
                <b>Ardianti & Waluyo (2021)</b> menganalisis kepuasan pelanggan terhadap kualitas pelayanan di Toko XYZ Surabaya menggunakan metode CSI dan PGCV. CSI menunjukkan pelanggan merasa puas, dan PGCV mengidentifikasi atribut prioritas perbaikan seperti ketersediaan meja kursi.
            </li>
            <li>
                <b>Ridho Muhammad Havidh Nst (2022)</b> menerapkan CSI dan analisis GAP pada kualitas pelayanan Bus Listrik Feeder Trans Koetaradja. Hasil CSI menunjukkan kriteria sangat puas, dan analisis GAP mengidentifikasi indikator dengan GAP tertinggi dan terendah.
            </li>
             <li>
                <b>Taraoktavia & Indarwati (2021)</b> meneliti pengaruh <i>experiential marketing</i> dan <i>zoo image</i> terhadap <i>revisit intention</i> dengan <i>experiential satisfaction</i> sebagai variabel intervening, menggunakan path analysis.
            </li>
        </ul>
        <p>Penelitian ini berupaya mengintegrasikan beberapa metode (SERVQUAL, IPA, PGCV, CSI) untuk memberikan analisis yang lebih komprehensif dan spesifik pada konteks Pakuwon City Mall Surabaya, yang merupakan kontribusi pembeda dari studi-studi sebelumnya.</p>
        </div>
        """, unsafe_allow_html=True
    )

with tab2:
    display_section_subheader("2.2 SERVQUAL (Service Quality)")
    st.markdown(
        """
        <div class='body-text'>
        <p>
        SERVQUAL adalah model konseptual yang dikembangkan oleh Parasuraman, Zeithaml, dan Berry (1985, 1988) untuk mengukur kualitas layanan yang dirasakan oleh pelanggan. Model ini didasarkan pada premis bahwa kualitas layanan dapat diukur dengan mengidentifikasi dan menganalisis kesenjangan (GAP) antara harapan pelanggan (<i>expectations</i>) terhadap suatu layanan dan persepsi mereka terhadap kinerja aktual layanan yang diterima (<i>perceptions</i>).
        </p>
        <p>SERVQUAL mengidentifikasi lima dimensi generik yang digunakan pelanggan dalam mengevaluasi kualitas layanan:</p>
        <ol>
            <li><b>Tangibles (Bukti Fisik/Berwujud):</b> Berkaitan dengan penampilan fisik fasilitas, peralatan, personel, dan materi komunikasi perusahaan. Dalam konteks mall, ini mencakup kebersihan, desain interior, kenyamanan fasilitas, dan penampilan staf.</li>
            <li><b>Reliability (Keandalan):</b> Kemampuan perusahaan untuk memberikan layanan yang dijanjikan secara akurat, konsisten, dan dapat diandalkan. Ini berarti melakukan layanan dengan benar pada kesempatan pertama. Contoh: eskalator yang selalu berfungsi, informasi yang akurat dari petugas.</li>
            <li><b>Responsiveness (Daya Tanggap):</b> Kemauan dan kesigapan para karyawan untuk membantu pelanggan dan memberikan layanan dengan cepat dan tepat waktu. Ini juga mencakup kemampuan untuk merespons permintaan atau keluhan pelanggan.</li>
            <li><b>Assurance (Jaminan):</b> Mencakup pengetahuan, kompetensi, kesopanan, dan sifat dapat dipercaya dari karyawan, serta kemampuan mereka untuk menumbuhkan rasa percaya dan keyakinan pelanggan terhadap perusahaan. Ini juga terkait dengan keamanan dan bebas dari risiko.</li>
            <li><b>Empathy (Empati):</b> Kemudahan dalam menjalin hubungan, komunikasi yang baik, perhatian pribadi, dan pemahaman terhadap kebutuhan individual pelanggan. Ini berarti memperlakukan pelanggan sebagai individu yang unik.</li>
        </ol>
        <p>Pengukuran kualitas layanan menggunakan SERVQUAL melibatkan kuesioner yang terdiri dari pasangan pernyataan untuk setiap atribut: satu untuk mengukur tingkat harapan pelanggan dan satu lagi untuk mengukur persepsi mereka terhadap kinerja aktual. Skor GAP dihitung sebagai $GAP = \text{Skor Persepsi} - \text{Skor Harapan}$. Nilai GAP negatif menunjukkan bahwa kinerja tidak memenuhi harapan, nilai positif berarti kinerja melebihi harapan, dan nilai nol berarti kinerja sesuai harapan.</p>
        </div>
        """, unsafe_allow_html=True
    )

with tab3:
    display_section_subheader("2.3 Importance-Performance Analysis (IPA)")
    st.markdown(
        """
        <div class='body-text'>
        <p>
        Importance-Performance Analysis (IPA), pertama kali diperkenalkan oleh Martilla dan James (1977), adalah sebuah teknik diagnostik yang digunakan secara luas untuk membantu manajer mengidentifikasi kekuatan dan kelemahan suatu produk atau layanan, serta menentukan prioritas untuk upaya perbaikan. IPA membandingkan persepsi pelanggan mengenai seberapa penting (<i>importance</i>) berbagai atribut layanan dengan persepsi mereka mengenai seberapa baik (<i>performance</i>) perusahaan dalam menyediakan atribut-atribut tersebut.
        </p>
        <p>Hasil analisis IPA biasanya divisualisasikan dalam sebuah diagram kartesius dua dimensi, yang dikenal sebagai matriks IPA. Sumbu horizontal (X) mewakili skor kinerja (<i>performance</i>), dan sumbu vertikal (Y) mewakili skor kepentingan (<i>importance</i>). Titik potong kedua sumbu biasanya adalah rata-rata keseluruhan skor kinerja dan kepentingan. Matriks ini terbagi menjadi empat kuadran:</p>
        <ul>
            <li><b>Kuadran I (Prioritas Utama / <i>Concentrate Here</i>):</b> Atribut-atribut yang berada di kuadran ini memiliki tingkat kepentingan tinggi bagi pelanggan, namun kinerjanya dinilai rendah oleh mereka. Ini adalah area kritis yang memerlukan perhatian dan tindakan perbaikan segera dari manajemen.</li>
            <li><b>Kuadran II (Pertahankan Prestasi / <i>Keep Up the Good Work</i>):</b> Atribut-atribut di sini dianggap sangat penting oleh pelanggan, dan kinerjanya juga dinilai tinggi. Perusahaan telah berhasil pada aspek ini dan harus terus mempertahankan level kinerjanya.</li>
            <li><b>Kuadran III (Prioritas Rendah / <i>Low Priority</i>):</b> Atribut-atribut ini memiliki tingkat kepentingan rendah bagi pelanggan dan kinerjanya juga dinilai rendah. Perbaikan di area ini tidak menjadi prioritas utama dan mungkin tidak memberikan dampak signifikan terhadap kepuasan keseluruhan.</li>
            <li><b>Kuadran IV (Mungkin Berlebihan / <i>Possible Overkill</i>):</b> Atribut-atribut di kuadran ini memiliki tingkat kepentingan rendah bagi pelanggan, namun kinerjanya sangat tinggi. Ini menunjukkan bahwa perusahaan mungkin mengalokasikan sumber daya secara berlebihan pada aspek-aspek yang kurang dihargai pelanggan. Sumber daya ini mungkin lebih baik dialihkan ke atribut di Kuadran I.</li>
        </ul>
        <p>IPA memberikan panduan visual yang jelas bagi pengambilan keputusan strategis terkait alokasi sumber daya dan fokus upaya peningkatan kualitas.</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.image("https://i.imgur.com/9yZ4G2s.png", caption="Contoh Matriks Analisis Importance-Performance Analysis (IPA)", use_column_width=True)


with tab4:
    display_section_subheader("2.4 Customer Satisfaction Index (CSI)")
    st.markdown(
        """
        <div class='body-text'>
        <p>
        Customer Satisfaction Index (CSI) adalah sebuah ukuran kuantitatif yang digunakan untuk menilai tingkat kepuasan pelanggan secara keseluruhan terhadap suatu produk, layanan, atau perusahaan. CSI merupakan indeks komposit yang dihitung berdasarkan evaluasi pelanggan terhadap berbagai atribut atau dimensi yang dianggap penting, serta bobot kepentingan relatif dari masing-masing atribut tersebut.
        </p>
        <p>Metode perhitungan CSI umumnya melibatkan langkah-langkah berikut (Fornell et al., 1996; Sutopo & Widodo, 2018):</p>
        <ol>
            <li><b>Identifikasi Atribut Kunci:</b> Menentukan atribut-atribut layanan atau produk yang relevan dan penting bagi pelanggan.</li>
            <li><b>Pengukuran Kepentingan dan Kinerja:</b> Mengumpulkan data dari pelanggan mengenai tingkat kepentingan (<i>importance</i>) setiap atribut dan persepsi mereka terhadap kinerja aktual (<i>performance/satisfaction</i>) perusahaan pada setiap atribut tersebut, biasanya menggunakan skala Likert.</li>
            <li><b>Menghitung Skor Rata-rata:</b> Menghitung skor rata-rata untuk kepentingan (Mean Importance Score - MIS) dan kinerja (Mean Satisfaction Score - MSS) untuk setiap atribut.</li>
            <li><b>Menghitung Bobot (Weight Factor - WF):</b> Bobot setiap atribut dihitung berdasarkan kontribusi relatifnya terhadap kepuasan keseluruhan. Salah satu cara umum adalah: $WF_i = MIS_i / \sum_{j=1}^{k} MIS_j$, di mana $k$ adalah jumlah atribut.</li>
            <li><b>Menghitung Skor Tertimbang (Weighted Score - WS):</b> Skor kinerja setiap atribut dikalikan dengan bobotnya: $WS_i = WF_i \times MSS_i$.</li>
            <li><b>Menghitung Total Skor Tertimbang (Total Weighted Score - TWS):</b> Jumlah dari semua skor tertimbang: $TWS = \sum_{i=1}^{k} WS_i$.</li>
            <li><b>Menghitung CSI:</b> CSI dihitung dengan membandingkan TWS dengan nilai maksimum yang mungkin dicapai (jika semua atribut dinilai sempurna pada skala kinerja, dikalikan dengan bobotnya, yang setara dengan skala maksimum jika bobot dinormalisasi). Rumus sederhana: $CSI = (TWS / \text{Skala Maksimum Kinerja}) \times 100\%$.</li>
        </ol>
        <p>Nilai CSI biasanya disajikan dalam rentang 0% hingga 100%. Kriteria interpretasi tingkat kepuasan (misalnya, Sangat Puas, Puas, Cukup Puas, Kurang Puas, Tidak Puas) kemudian digunakan untuk memberikan makna pada nilai CSI yang diperoleh. Contoh kriteria (Tabel 2.3 dari PDF): 81-100% (Sangat Puas), 66-80.99% (Puas), dst.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
with tab5:
    display_section_subheader("2.5 Potential Gain in Customer Value (PGCV)")
    st.markdown(
        """
        <div class='body-text'>
        <p>
        Analisis Potential Gain in Customer Value (PGCV) adalah sebuah metode yang digunakan untuk menyempurnakan atau melengkapi hasil analisis dari metode Importance-Performance Analysis (IPA). Sementara IPA membantu mengidentifikasi kuadran prioritas, PGCV bertujuan untuk memberikan urutan perbaikan yang lebih spesifik di antara atribut-atribut yang dianggap penting, khususnya yang berada di Kuadran I (Prioritas Utama) IPA. Metode ini membantu menganalisis atribut mana yang, jika kinerjanya ditingkatkan, akan memberikan "keuntungan nilai" atau peningkatan kepuasan terbesar bagi pelanggan (Hom, 2003; Ardianti & Waluyo, 2021).
        </p>
        <p>PGCV mengukur seberapa besar potensi peningkatan kepuasan pelanggan jika kinerja suatu atribut yang dianggap penting ditingkatkan dari level saat ini ke level maksimal atau yang ideal menurut persepsi pelanggan.</p>
        <p>Langkah-langkah umum dalam menghitung indeks PGCV (LR & Sulistyawati, 2021 dari PDF):</p>
        <ol>
            <li>
                <b>Menghitung Achieved Customer Value (ACV) per atribut:</b>
                ACV mencerminkan nilai yang saat ini dirasakan pelanggan dari kinerja aktual suatu atribut, dengan mempertimbangkan kepentingannya.
                $$ ACV_i = \overline{X}_i \times \overline{Y}_i $$
                Dimana: $\overline{X}_i$ = Skor rata-rata tingkat kepuasan/kenyataan (Performance) untuk atribut ke-i, dan $\overline{Y}_i$ = Skor rata-rata tingkat kepentingan (Importance) untuk atribut ke-i.
            </li>
            <li>
                <b>Menghitung Ultimately Desired Customer Value (UDCV) per atribut:</b>
                UDCV mencerminkan nilai ideal yang diinginkan pelanggan jika kinerja atribut tersebut maksimal, dengan tetap mempertimbangkan kepentingannya.
                $$ UDCV_i = \overline{Y}_i \times P_{max} $$
                Dimana: $P_{max}$ = Nilai maksimal pada skala Likert yang digunakan untuk mengukur kinerja (misalnya, 6 jika skala 1-6).
            </li>
            <li>
                <b>Menghitung Indeks Potential Gain in Customer Value (PGCV) Terbobot per atribut:</b>
                Indeks PGCV menunjukkan potensi peningkatan nilai. Pembobotan dilakukan untuk menormalkan kontribusi kepentingan setiap atribut.
                $$ \text{Indeks PGCV}_i = (UDCV_i - ACV_i) \times Bobot_i $$
                Dimana: $Bobot_i = \overline{Y}_i / \sum_{j=1}^{k} \overline{Y}_j $ (Bobot kepentingan relatif atribut ke-i).
            </li>
        </ol>
        <p>Atribut layanan dengan nilai Indeks PGCV terbesar menjadi prioritas pertama dalam perbaikan, diikuti oleh atribut dengan nilai PGCV terbesar kedua, dan seterusnya. Ini memberikan panduan yang lebih terperinci untuk alokasi sumber daya perbaikan.</p>
        </div>
        """, unsafe_allow_html=True
    )

with tab6:
    display_section_subheader("2.6 Pakuwon City Mall Surabaya")
    st.markdown(
        """
        <div class='body-text'>
        <p>
        Pakuwon City Mall (PCM) merupakan salah satu pusat perbelanjaan modern yang berlokasi strategis di kawasan pengembangan kota mandiri Pakuwon City, Surabaya Timur. Mall ini secara resmi mulai beroperasi pada akhir tahun 2020 dan dirancang sebagai sebuah <i>lifestyle mall</i> yang menyasar segmen konsumen kelas menengah hingga atas. PCM adalah bagian dari portofolio Pakuwon Group, salah satu pengembang properti terkemuka di Indonesia yang dikenal dengan proyek-proyek superblok terintegrasi.
        </p>
        <p>
        Dengan luas area yang substansial (lebih dari 60.000 m²) dan menampung lebih dari 200 gerai (<i>tenant</i>), Pakuwon City Mall menawarkan beragam pilihan produk dan layanan, mulai dari fesyen, kuliner, hiburan keluarga, hingga kebutuhan sehari-hari. Kehadiran tenant-tenant premium dan fasilitas pendukung lainnya bertujuan untuk menciptakan pengalaman berbelanja dan rekreasi yang komprehensif dan nyaman bagi pengunjung.
        </p>
        <p>
        Selain berfungsi sebagai destinasi belanja, PCM juga diposisikan sebagai episentrum kegiatan sosial dan rekreasi bagi masyarakat urban, khususnya yang berdomisili di wilayah timur Surabaya dan sekitarnya. Kedekatannya dengan beberapa institusi pendidikan tinggi seperti Institut Teknologi Sepuluh Nopember (ITS), Universitas Airlangga (Unair Kampus C), Politeknik Elektronika Negeri Surabaya (PENS), dan Politeknik Perkapalan Negeri Surabaya (PPNS) juga diduga mempengaruhi karakteristik demografis pengunjungnya, dengan potensi segmen pelajar/mahasiswa yang signifikan.
        </p>
        <p>
        Sebagai pusat perbelanjaan yang relatif baru di tengah persaingan industri ritel yang ketat di Surabaya, aspek kualitas layanan dan kepuasan pengunjung menjadi faktor krusial bagi PCM untuk membangun reputasi yang kuat, menarik kunjungan berulang, dan mempertahankan loyalitas pelanggan dalam jangka panjang. Evaluasi berkelanjutan terhadap persepsi pengunjung menjadi penting untuk mengidentifikasi area-area yang memerlukan peningkatan dan inovasi.
        </p>
        </div>
        """, unsafe_allow_html=True
    )
