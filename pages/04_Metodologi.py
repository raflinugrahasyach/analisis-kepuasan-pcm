# Simpan file ini sebagai 04_Metodologi.py
# di dalam folder `pages` (misalnya, final_project_streamlit/pages/04_Metodologi.py)

import streamlit as st

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_header(title, subtitle=""):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='body-text' style='text-align:center; font-size:1.1em; font-style:italic; margin-bottom:1.5rem;'>{subtitle}</p>", unsafe_allow_html=True)

# --- Konten Halaman Metodologi ---
# Setiap bagian akan menggunakan st.expander

display_page_header("BAB III: Metode Penelitian", "Rancangan, Pendekatan, dan Teknik Analisis yang Digunakan")

with st.expander("💾 3.1 Sumber Data dan Jenis Data", expanded=True):
    st.markdown(
        """
        <div class='body-text'>
        <p>Penelitian ini menggunakan <b>data primer</b> sebagai sumber informasi utama. Data primer adalah data yang dikumpulkan secara langsung oleh peneliti dari sumber pertama untuk menjawab tujuan penelitian yang spesifik.</p>
        <p>Jenis data yang dikumpulkan meliputi:</p>
        <ul>
            <li><b>Data Kuantitatif:</b> Berupa skor atau angka hasil penilaian responden terhadap kuesioner terkait harapan (<i>importance</i>) dan persepsi kenyataan (<i>performance</i>) kualitas layanan Pakuwon City Mall. Skor ini menggunakan skala Likert.</li>
            <li><b>Data Kategorikal/Nominal:</b> Berupa informasi mengenai karakteristik demografis responden, seperti jenis kelamin, usia (dapat dikategorikan), pekerjaan, dan jenis kendaraan yang digunakan.</li>
        </ul>
        <p>Pengumpulan data primer dilakukan melalui survei langsung dengan menyebarkan kuesioner kepada pengunjung Pakuwon City Mall Surabaya. Direncanakan survei dilakukan selama 7 hari untuk mencakup variasi pengunjung pada hari kerja dan akhir pekan.</p>
        </div>
        """, unsafe_allow_html=True
    )

with st.expander("🎯 3.2 Populasi dan Teknik Pengambilan Sampel", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p><b>Populasi:</b></p>
        <p>Populasi target dalam penelitian ini adalah seluruh individu yang merupakan pengunjung Pakuwon City Mall Surabaya. Mengingat ukuran populasi yang sangat besar dan dinamis (<i>infinite population</i> atau sulit dihitung secara pasti), maka estimasi ukuran populasi dilakukan untuk keperluan perhitungan sampel.</p>
        <p>Berdasarkan survei pendahuluan yang dilakukan pada jam puncak kunjungan (Jumat, Sabtu, Minggu pukul 19.00-20.00 WIB), jumlah pengunjung tertinggi tercatat pada hari Sabtu, yaitu sebanyak 793 orang dalam satu jam. Angka ini (N=793) digunakan sebagai dasar perkiraan populasi untuk perhitungan ukuran sampel, dengan asumsi bahwa periode puncak dapat memberikan gambaran yang cukup representatif.</p>
        
        <p><b>Teknik Pengambilan Sampel:</b></p>
        <p>Teknik pengambilan sampel yang digunakan adalah <b>probability sampling</b> dengan metode <b>sampling acak sistematis (systematic random sampling)</b>. Metode ini dipilih karena memberikan kesempatan yang sama bagi setiap elemen populasi untuk terpilih menjadi sampel dan relatif mudah diimplementasikan di lapangan.</p>
        <p>Langkah-langkah pengambilan sampel adalah sebagai berikut:</p>
        <ol>
            <li>
                <b>Menentukan Ukuran Sampel (n):</b>
                Ukuran sampel dihitung menggunakan rumus estimasi proporsi untuk populasi terbatas (karena N diketahui dari survei pendahuluan), namun seringkali rumus Slovin atau rumus untuk populasi besar juga digunakan jika N sangat besar. Dalam dokumen PDF, digunakan rumus:
                $$ n = \\frac{N \cdot P(1-P)}{(N-1)D + P(1-P)} $$
                Dimana:
                <ul>
                    <li>$N$ = Ukuran populasi acuan (793)</li>
                    <li>$P$ = Taksiran proporsi populasi (digunakan 0,5 untuk mendapatkan ukuran sampel maksimal jika tidak ada informasi proporsi sebelumnya)</li>
                    <li>$D = (B / Z_{1-\alpha/2})^2$, merupakan kuadrat dari kesalahan yang dapat ditoleransi dibagi nilai Z.</li>
                    <li>$B$ = Batas kekeliruan yang diinginkan (<i>margin of error</i>), ditetapkan sebesar 0,1 (10%).</li>
                    <li>$Z_{1-\alpha/2}$ = Nilai Z pada tingkat kepercayaan 95% (tingkat signifikansi $\alpha=0,05$), yaitu 1,96.</li>
                </ul>
                Perhitungan dari PDF:
                $D = (0,1 / 1,96)^2 \approx 0,0026031$
                $n = (793 \cdot 0,5 \cdot (1-0,5)) / ((793-1) \cdot 0,0026031 + 0,5 \cdot (1-0,5))$
                $n = 198,25 / (792 \cdot 0,0026031 + 0,25)$
                $n = 198,25 / (2,0616552 + 0,25) = 198,25 / 2,3116552 \approx 85,759$
                Maka, ukuran sampel minimum yang diambil dibulatkan menjadi <b>86 responden</b>.
            </li>
            <li>
                <b>Menghitung Interval Sampel (k):</b>
                Interval sampel dihitung dengan rumus: $k = N/n$.
                $k = 793 / 86 \approx 9,22$. Dibulatkan menjadi <b>10</b> (sesuai PDF).
                Ini berarti setiap 10 pengunjung yang memenuhi kriteria dan keluar dari pintu utama akan dipilih sebagai responden.
            </li>
            <li>
                <b>Menentukan Sampel Pertama Secara Acak:</b>
                Satu unit sampel pertama dipilih secara acak dari $k$ pengunjung pertama (yaitu, dari pengunjung ke-1 hingga ke-10). Misalnya, jika angka acak yang terpilih adalah 3 (sesuai PDF), maka pengunjung ke-3 yang keluar adalah responden pertama.
            </li>
            <li>
                <b>Memilih Sampel Berikutnya Secara Sistematis:</b>
                Responden berikutnya dipilih dengan menambahkan interval $k$ pada nomor urut responden sebelumnya. Jadi, jika responden pertama adalah pengunjung ke-3, maka responden kedua adalah pengunjung ke-$(3+10)=13$, responden ketiga adalah pengunjung ke-$(13+10)=23$, dan seterusnya, hingga jumlah sampel terpenuhi.
            </li>
        </ol>
        <p>Pengambilan sampel dilakukan pada pengunjung yang keluar melalui pintu utama Pakuwon City Mall.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
with st.expander("📊 3.3 Variabel Penelitian dan Definisi Operasional", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p>Variabel yang digunakan dalam penelitian ini dapat dikelompokkan menjadi variabel karakteristik responden dan variabel kualitas layanan (SERVQUAL).</p>
        
        <p><b>A. Variabel Karakteristik Responden:</b></p>
        <ol>
            <li><b>Jenis Kelamin (X1):</b> Perbedaan biologis antara laki-laki dan perempuan. Skala: Nominal (1=Laki-laki, 2=Perempuan).</li>
            <li><b>Usia (X2):</b> Waktu hidup responden sejak dilahirkan, diukur dalam tahun. Skala: Rasio.</li>
            <li><b>Pekerjaan (X3):</b> Aktivitas utama yang dilakukan responden untuk mendapatkan upah/gaji. Skala: Nominal (1=Pelajar/Mahasiswa, 2=Pegawai Swasta, 3=Pegawai Negeri, 4=Wiraswasta, 5=Ibu Rumah Tangga/Tidak Bekerja, 6=Lainnya).</li>
            <li><b>Jenis Kendaraan (X4):</b> Moda transportasi yang digunakan responden untuk datang ke PCM. Skala: Nominal (1=Sepeda motor, 2=Mobil, 3=Transportasi umum, 4=Transportasi online).</li>
        </ol>

        <p><b>B. Variabel Kualitas Layanan (SERVQUAL):</b></p>
        <p>Diukur berdasarkan persepsi dan harapan responden terhadap berbagai atribut layanan, menggunakan skala Likert 6 poin (1=Sangat Tidak Puas/Sangat Tidak Penting hingga 6=Sangat Puas/Sangat Penting). Penggunaan 6 poin bertujuan untuk menghindari kecenderungan responden memilih jawaban netral.</p>
        
        <ol>
            <li><b>Tangibles (Bukti Fisik) (X5):</b> Daya tarik fasilitas fisik, perlengkapan, dan materi yang digunakan perusahaan.
                <ul>
                    <li>T1: Kebersihan area mall (toilet, food court, eskalator, dll.)</li>
                    <li>T2: Ketersediaan tempat duduk dan area istirahat di mall</li>
                    <li>T3: Ketersediaan papan penunjuk arah yang jelas</li>
                    <li>T4: Aksesibilitas tempat parkir</li>
                    <li>T5: Kenyamanan suhu udara mall</li>
                    <li>T6: Desain dan suasana mall yang menarik</li>
                </ul>
            </li>
            <li><b>Reliability (Keandalan) (X6):</b> Kemampuan perusahaan memberikan layanan yang akurat dan tidak membuat kesalahan.
                <ul>
                    <li>R1: Kemudahan menemukan tenant atau toko yang dicari</li>
                    <li>R2: Ketersediaan informasi acara atau promo yang mudah diakses</li>
                    <li>R3: Fasilitas mall (eskalator, toilet, dll.) berfungsi dengan baik</li>
                </ul>
            </li>
            <li><b>Responsiveness (Daya Tanggap) (X7):</b> Kemampuan dan kesediaan karyawan membantu konsumen dan menanggapi permintaannya.
                <ul>
                    <li>Rp1: Petugas mall cepat membantu jika ada yang bertanya</li>
                    <li>Rp2: Kecepatan layanan kebersihan dalam menjaga kebersihan mall</li>
                    <li>Rp3: Ketanggapan petugas mall dalam menyapa pengunjung yang datang</li>
                </ul>
            </li>
            <li><b>Assurance (Jaminan) (X8):</b> Kemampuan karyawan/perusahaan menumbuhkan kepercayaan konsumen.
                <ul>
                    <li>A1: Rasa aman dari tindak kriminal di dalam mall</li>
                    <li>A2: Keamanan dalam menggunakan fasilitas seperti eskalator</li>
                    <li>A3: Kenyamanan mengakses jalan di dalam mall</li>
                </ul>
            </li>
            <li><b>Empathy (Empati) (X9 - sesuai penomoran di PDF untuk Empathy):</b> Pemahaman perusahaan/karyawan terhadap konsumen dan pemberian perhatian personal.
                <ul>
                    <li>E1: Prosedur pelayanan pelanggan yang baik</li>
                    <li>E2: Petugas mall sabar dalam melayani pelanggan</li>
                    <li>E3: Ketersediaan sarana untuk menyampaikan aduan/keluhan pelanggan</li>
                </ul>
            </li>
        </ol>
        </div>
        """, unsafe_allow_html=True
    )

with st.expander("⚙️ 3.4 Instrumen Penelitian dan Skala Pengukuran", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p><b>Instrumen Penelitian:</b></p>
        <p>Instrumen utama yang digunakan adalah <b>kuesioner terstruktur</b>. Kuesioner ini dirancang untuk mengumpulkan data mengenai karakteristik responden serta persepsi dan harapan mereka terhadap kualitas layanan Pakuwon City Mall. Kuesioner terdiri dari dua bagian utama:</p>
        <ol>
            <li>Bagian pertama berisi pertanyaan terkait data demografis responden (jenis kelamin, usia, pekerjaan, jenis kendaraan).</li>
            <li>Bagian kedua berisi daftar pernyataan (atribut layanan) yang dikelompokkan berdasarkan lima dimensi SERVQUAL (Tangibles, Reliability, Responsiveness, Assurance, Empathy). Untuk setiap pernyataan, responden diminta memberikan dua jenis penilaian:
                <ul>
                    <li><b>Tingkat Harapan (Importance):</b> Seberapa penting atribut tersebut bagi responden.</li>
                    <li><b>Tingkat Persepsi Kenyataan (Performance):</b> Seberapa baik kinerja Pakuwon City Mall pada atribut tersebut menurut pengalaman responden.</li>
                </ul>
            </li>
        </ol>
        
        <p><b>Skala Pengukuran:</b></p>
        <p>Untuk mengukur tingkat harapan dan persepsi kenyataan pada atribut kualitas layanan, digunakan <b>skala Likert 6 poin</b>. Alasan penggunaan 6 poin adalah untuk menghilangkan pilihan tengah (netral) yang seringkali menjadi bias, sehingga memaksa responden untuk lebih cenderung ke arah setuju/tidak setuju atau puas/tidak puas. Rentang skala adalah sebagai berikut (contoh untuk persepsi):</p>
        <ul>
            <li>1 = Sangat Tidak Puas</li>
            <li>2 = Tidak Puas</li>
            <li>3 = Cukup Tidak Puas (atau Agak Tidak Puas)</li>
            <li>4 = Cukup Puas (atau Agak Puas)</li>
            <li>5 = Puas</li>
            <li>6 = Sangat Puas</li>
        </ul>
        <p>Skala serupa (misalnya, Sangat Tidak Penting hingga Sangat Penting) digunakan untuk mengukur tingkat harapan.</p>
        
        <p><b>Uji Validitas dan Reliabilitas Instrumen:</b></p>
        <p>Sebelum kuesioner digunakan untuk pengumpulan data utama, akan dilakukan uji coba (<i>pilot survey</i>) kepada sejumlah responden (misalnya, 30 orang) yang memiliki karakteristik serupa dengan populasi target. Data hasil uji coba akan dianalisis untuk:</p>
        <ul>
            <li><b>Uji Validitas:</b> Untuk memastikan bahwa setiap butir pertanyaan dalam kuesioner benar-benar mengukur variabel yang seharusnya diukur. Dapat digunakan teknik korelasi Pearson Product Moment, di mana skor setiap item dikorelasikan dengan skor total konstruknya. Item dianggap valid jika nilai $r_{hitung} > r_{tabel}$ pada tingkat signifikansi tertentu (misalnya, $\alpha=0,05$).</li>
            <li><b>Uji Reliabilitas:</b> Untuk memastikan bahwa kuesioner konsisten dan stabil dalam mengukur variabel jika digunakan berulang kali pada kondisi yang sama. Metode yang umum digunakan adalah Cronbach's Alpha. Kuesioner dianggap reliabel jika nilai Cronbach's Alpha $\geq 0,60$ (atau standar lain yang lebih tinggi seperti 0,70).</li>
        </ul>
        <p>Butir pertanyaan yang tidak valid atau tidak reliabel akan direvisi atau dihilangkan dari kuesioner akhir.</p>
        </div>
        """, unsafe_allow_html=True
    )

with st.expander("🛠️ 3.5 Teknik Analisis Data", expanded=False):
    st.markdown(
        """
        <div class='body-text'>
        <p>Data yang telah terkumpul akan diolah dan dianalisis menggunakan beberapa teknik statistik dan metode analisis, baik deskriptif maupun inferensial, dengan bantuan perangkat lunak statistik (misalnya, SPSS, R, atau Python).</p>
        <ol>
            <li>
                <b>Analisis Statistik Deskriptif:</b>
                Digunakan untuk memberikan gambaran umum mengenai karakteristik responden (distribusi frekuensi, persentase, mean, median, modus) dan untuk meringkas skor rata-rata harapan serta persepsi kenyataan untuk setiap atribut layanan.
            </li>
            <li>
                <b>Analisis Kesenjangan Kualitas Layanan (SERVQUAL GAP Analysis):</b>
                <ul>
                    <li>Menghitung skor rata-rata harapan ($E_i$) dan skor rata-rata persepsi kenyataan ($P_i$) untuk setiap atribut layanan ke-i.</li>
                    <li>Menghitung nilai kesenjangan (GAP) untuk setiap atribut: $GAP_i = P_i - E_i$.</li>
                    <li>Menginterpretasikan nilai GAP: GAP negatif menunjukkan kinerja di bawah harapan, GAP positif menunjukkan kinerja melebihi harapan, dan GAP nol menunjukkan kinerja sesuai harapan.</li>
                    <li>(Opsional, sesuai PDF) Uji Wilcoxon Signed-Rank Test: Digunakan untuk menguji apakah terdapat perbedaan yang signifikan secara statistik antara skor harapan dan skor persepsi kenyataan untuk setiap atribut layanan (karena data berpasangan dan mungkin tidak berdistribusi normal).</li>
                </ul>
            </li>
            <li>
                <b>Importance-Performance Analysis (IPA):</b>
                <ul>
                    <li>Memplot skor rata-rata harapan (sumbu Y) melawan skor rata-rata persepsi kenyataan (sumbu X) untuk setiap atribut layanan ke dalam diagram kartesius.</li>
                    <li>Menentukan titik potong sumbu X dan Y, biasanya menggunakan rata-rata keseluruhan skor harapan dan persepsi kenyataan.</li>
                    <li>Mengidentifikasi atribut-atribut yang masuk ke dalam masing-masing dari empat kuadran (Kuadran I: Prioritas Utama, Kuadran II: Pertahankan Prestasi, Kuadran III: Prioritas Rendah, Kuadran IV: Mungkin Berlebihan) dan memberikan interpretasi strategis.</li>
                </ul>
            </li>
            <li>
                <b>Potential Gain in Customer Value (PGCV):</b>
                <ul>
                    <li>Menghitung Achieved Customer Value (ACV), Ultimately Desired Customer Value (UDCV), dan Indeks PGCV terbobot untuk setiap atribut layanan, terutama yang menjadi fokus perbaikan dari analisis IPA.</li>
                    <li>Mengurutkan atribut berdasarkan nilai Indeks PGCV tertinggi untuk menentukan prioritas perbaikan yang memberikan dampak peningkatan nilai terbesar bagi pelanggan.</li>
                </ul>
            </li>
            <li>
                <b>Customer Satisfaction Index (CSI):</b>
                <ul>
                    <li>Menghitung Mean Importance Score (MIS) dan Mean Satisfaction Score (MSS) untuk setiap atribut.</li>
                    <li>Menghitung Weight Factor (WF) untuk setiap atribut berdasarkan MIS-nya.</li>
                    <li>Menghitung Weighted Score (WS) dengan mengalikan WF dengan MSS untuk setiap atribut.</li>
                    <li>Menghitung Total Weighted Score (WT) dengan menjumlahkan semua WS.</li>
                    <li>Menghitung CSI dengan rumus: $CSI = (WT / \text{Skala Maksimum}) \times 100\%$.</li>
                    <li>Menginterpretasikan nilai CSI berdasarkan kriteria tingkat kepuasan yang telah ditetapkan (misalnya, Sangat Puas, Puas, dll.).</li>
                </ul>
            </li>
        </ol>
        </div>
        """, unsafe_allow_html=True
    )

with st.expander("🌊 3.6 Diagram Alir Penelitian", expanded=False):
    st.image("https://i.imgur.com/xU7gT9U.png", caption="Diagram Alir Tahapan Penelitian (Sumber: Diadaptasi dari dokumen penelitian)", use_column_width=True)
    st.markdown(
        """
        <div class='body-text'>
        <p>Diagram alir di atas mengilustrasikan urutan logis dari tahapan-tahapan yang dilakukan dalam penelitian ini. Proses dimulai dari identifikasi masalah dan penentuan topik, dilanjutkan dengan studi literatur dan penyusunan kerangka konseptual. Tahap berikutnya adalah perancangan metodologi penelitian, termasuk pengembangan instrumen (kuesioner) dan rencana pengambilan sampel. Sebelum pengumpulan data utama, dilakukan uji validitas dan reliabilitas instrumen. Setelah data terkumpul, dilakukan analisis data menggunakan berbagai metode yang telah dijelaskan (SERVQUAL, IPA, PGCV, CSI). Akhirnya, hasil analisis diinterpretasikan untuk menarik kesimpulan dan merumuskan saran atau rekomendasi bagi pihak terkait.</p>
        </div>
        """, unsafe_allow_html=True
    )
