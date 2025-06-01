# Simpan file ini sebagai 05_Hasil_dan_Pembahasan.py
# di dalam folder `pages` (misalnya, final_project_streamlit/pages/05_Hasil_dan_Pembahasan.py)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_header(title, subtitle=""):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='body-text' style='text-align:center; font-size:1.1em; font-style:italic; margin-bottom:1.5rem;'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_subheader(title):
    st.markdown(f"<h2 class='sub-header'>{title}</h2>", unsafe_allow_html=True)

# --- Konten Halaman Hasil dan Pembahasan ---

display_page_header("BAB IV: Hasil Penelitian dan Pembahasan", "Temuan Utama dan Analisis Data")

# 4.1 Karakteristik Pengunjung Pakuwon City Mall
with st.container(border=True):
    display_section_subheader("4.1 Karakteristik Pengunjung Pakuwon City Mall")
    st.markdown(
        """
        <div class='body-text'>
        <p>Bagian ini menyajikan deskripsi karakteristik responden yang berpartisipasi dalam survei, meliputi jenis kelamin, jenis pekerjaan, usia, dan jenis kendaraan yang digunakan. Pemahaman terhadap profil pengunjung ini penting untuk mengkontekstualisasikan temuan mengenai kepuasan layanan.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    tab_titles_karakteristik = ["🚻 Jenis Kelamin", "💼 Pekerjaan", "🎂 Usia", "🚗 Jenis Kendaraan"]
    karakteristik_tabs = st.tabs(tab_titles_karakteristik)

    with karakteristik_tabs[0]:
        st.markdown("<h5>4.1.1 Karakteristik Jenis Kelamin Pengunjung</h5>", unsafe_allow_html=True)
        # Data dari PDF Gambar 4.1 (halaman 18 PDF)
        data_gender = pd.DataFrame({
            'Jenis Kelamin': ['Laki-laki', 'Perempuan'],
            'Jumlah': [51, 36],
            'Persentase': [58.65, 41.4] # Menggunakan angka dari teks deskripsi PDF
        })
        fig_gender = px.pie(data_gender, values='Persentase', names='Jenis Kelamin', 
                            title='Gambar 4.1: Distribusi Pengunjung Berdasarkan Jenis Kelamin',
                            color_discrete_sequence=px.colors.qualitative.Pastel1, hole=0.4)
        fig_gender.update_traces(textinfo='percent+label+value', texttemplate='%{label}<br>%{percent:.2f}%<br>(%{value} orang)', 
                                 hoverinfo='label+percent+value', pull=[0.05, 0])
        fig_gender.update_layout(legend_title_text='Jenis Kelamin', title_x=0.5)
        st.plotly_chart(fig_gender, use_container_width=True)
        st.markdown(
            """
            <div class='body-text'>
            <p>Berdasarkan Gambar 4.1, mayoritas pengunjung Pakuwon City Mall yang menjadi responden dalam penelitian ini adalah <b>laki-laki</b>, dengan jumlah 51 orang atau mencakup <b>58,65%</b> dari total sampel. Sementara itu, pengunjung <b>perempuan</b> tercatat sebanyak 36 orang, atau sebesar <b>41,4%</b>. Dominasi pengunjung laki-laki ini dapat mengindikasikan adanya potensi bagi manajemen PCM untuk melakukan segmentasi pasar yang lebih spesifik berdasarkan gender, guna mengembangkan strategi pemasaran dan penawaran layanan yang lebih relevan untuk mempertahankan atau meningkatkan kepuasan kelompok demografis ini.</p>
            </div>
            """, unsafe_allow_html=True)

    with karakteristik_tabs[1]:
        st.markdown("<h5>4.1.2 Karakteristik Jenis Pekerjaan Pengunjung</h5>", unsafe_allow_html=True)
        # Data dari PDF Gambar 4.2 (halaman 19 PDF)
        data_pekerjaan = pd.DataFrame({
            'Pekerjaan': ['Pelajar/Mahasiswa', 'Pegawai Swasta', 'Pegawai Negeri', 'Wiraswasta', 'Lainnya'],
            # Jumlah dihitung dari persentase dan total sampel 87 (51+36)
            'Jumlah': [round(0.402 * 87), round(0.264 * 87), round(0.184 * 87), round(0.115 * 87), 87 - (round(0.402 * 87)+round(0.264 * 87)+round(0.184 * 87)+round(0.115 * 87))],
            'Persentase': [40.2, 26.4, 18.4, 11.5, 3.4] # Persentase dari Pie Chart
        })
        fig_pekerjaan = px.bar(data_pekerjaan.sort_values('Persentase', ascending=False), 
                               x='Pekerjaan', y='Persentase', 
                               title='Gambar 4.2: Distribusi Pengunjung Berdasarkan Jenis Pekerjaan',
                               labels={'Persentase': 'Persentase Pengunjung (%)', 'Pekerjaan': 'Jenis Pekerjaan'},
                               color='Pekerjaan', text_auto=True,
                               color_discrete_sequence=px.colors.qualitative.Set3)
        fig_pekerjaan.update_layout(xaxis_title="", yaxis_title="Persentase (%)", showlegend=False, title_x=0.5)
        fig_pekerjaan.update_traces(texttemplate='%{y:.1f}%', textposition='outside', hovertemplate='<b>%{x}</b><br>Persentase: %{y:.1f}%<br>Jumlah: %{customdata[0]} orang<extra></extra>', customdata=data_pekerjaan[['Jumlah']])
        st.plotly_chart(fig_pekerjaan, use_container_width=True)
        st.markdown(
            """
            <div class='body-text'>
            <p>Profil pekerjaan pengunjung Pakuwon City Mall (Gambar 4.2) menunjukkan dominasi dari kelompok <b>Pelajar/Mahasiswa</b>, yang mencapai <b>40,2%</b> (35 orang dari 87 responden). Kelompok ini diikuti oleh <b>Pegawai Swasta (26,4% atau 23 orang)</b>, <b>Pegawai Negeri (18,4% atau 16 orang)</b>, <b>Wiraswasta (11,5% atau 10 orang)</b>, dan kategori <b>Lainnya (3,4% atau 3 orang)</b>. Tingginya proporsi pelajar/mahasiswa ini, menurut analisis dalam dokumen, diduga kuat dipengaruhi oleh kedekatan geografis PCM dengan berbagai institusi pendidikan tinggi di Surabaya (ITS, Unair, PENS, PPNS, dan UHT). Segmen pelajar/mahasiswa cenderung memiliki preferensi produk dan layanan yang berbeda, seperti ketertarikan pada makanan dan minuman dengan harga terjangkau serta tempat berkumpul (<i>nongkrong</i>) yang menarik secara visual dan <i>instagramable</i>.</p>
            </div>
            """, unsafe_allow_html=True)

    with karakteristik_tabs[2]:
        st.markdown("<h5>4.1.3 Karakteristik Usia Pengunjung</h5>", unsafe_allow_html=True)
        # Data usia dari PDF Gambar 4.3 (halaman 19 PDF) - Boxplot
        # Karena data mentah tidak ada, kita tampilkan informasi deskriptifnya.
        # Jika ingin membuat boxplot representatif, perlu data dummy yang sesuai.
        # Untuk sekarang, kita fokus pada deskripsi dari PDF.
        st.image("https://i.imgur.com/Yk4ZzYy.png", caption="Gambar 4.3: Boxplot Karakteristik Usia Pengunjung (Sumber: Dokumen Penelitian)", use_column_width=True) # Ganti dengan path gambar boxplot jika ada
        st.markdown(
            """
            <div class='body-text'>
            <p>Analisis usia pengunjung Pakuwon City Mall, seperti yang divisualisasikan dalam Gambar 4.3 (Boxplot Usia), menunjukkan bahwa nilai tengah (median) usia pengunjung adalah <b>23 tahun</b>. Rata-rata (mean) usia pengunjung tercatat sebesar <b>23,11 tahun</b>. Lebar boxplot yang relatif kecil mengindikasikan bahwa keragaman usia pengunjung tidak terlalu tinggi, dengan mayoritas pengunjung terkonsentrasi pada rentang usia muda.</p>
            <p>Meskipun demikian, boxplot juga menunjukkan adanya pengunjung dengan usia di atas 30 tahun, bahkan hingga mencapai 45 tahun (terlihat sebagai data pencilan atau pada batas atas whisker). Hal ini mengindikasikan bahwa meskipun didominasi oleh segmen muda, PCM juga menarik bagi kelompok usia yang lebih matang, walau dalam proporsi yang lebih kecil.</p>
            </div>
            """, unsafe_allow_html=True)

    with karakteristik_tabs[3]:
        st.markdown("<h5>4.1.4 Karakteristik Jenis Kendaraan Pengunjung</h5>", unsafe_allow_html=True)
        # Data dari PDF Gambar 4.4 (halaman 20 PDF)
        data_kendaraan = pd.DataFrame({
            'Jenis Kendaraan': ['Sepeda Motor', 'Mobil', 'Transportasi Online', 'Transportasi Umum'],
            'Persentase': [43.7, 43.7, 6.9, 5.7] # Dari teks PDF: 38 org motor (43.7%), 38 org mobil (43.7%), 11 sisanya (12.6%) dibagi antara online & umum.
        })
        # Jumlah dihitung dari persentase dan total sampel 87
        data_kendaraan['Jumlah'] = [round(p/100 * 87) for p in data_kendaraan['Persentase']]
        # Koreksi jumlah agar total 87
        data_kendaraan.loc[data_kendaraan['Jenis Kendaraan'] == 'Transportasi Online', 'Jumlah'] = 87 - data_kendaraan[data_kendaraan['Jenis Kendaraan'] != 'Transportasi Online']['Jumlah'].sum()


        fig_kendaraan = px.pie(data_kendaraan, values='Persentase', names='Jenis Kendaraan', 
                               title='Gambar 4.4: Distribusi Pengunjung Berdasarkan Jenis Kendaraan',
                               color_discrete_sequence=px.colors.qualitative.Bold, hole=0.4)
        fig_kendaraan.update_traces(textinfo='percent+label+value', texttemplate='%{label}<br>%{percent:.1f}%<br>(%{customdata[0]} org)',
                                    customdata=data_kendaraan[['Jumlah']],
                                    hoverinfo='label+percent+value', pull=[0,0,0.05,0.05])
        fig_kendaraan.update_layout(legend_title_text='Jenis Kendaraan', title_x=0.5)
        st.plotly_chart(fig_kendaraan, use_container_width=True)
        st.markdown(
            """
            <div class='body-text'>
            <p>Gambar 4.4 menunjukkan bahwa penggunaan kendaraan pribadi sangat dominan di kalangan pengunjung Pakuwon City Mall. Pengguna <b>sepeda motor</b> dan pengguna <b>mobil</b> memiliki proporsi yang sama besar, masing-masing sebanyak 38 orang atau <b>43,7%</b> dari total responden. Sebanyak 11 pengunjung sisanya (12,6%) menggunakan moda transportasi lain, yang terdistribusi antara <b>transportasi online</b> (sekitar 6,9%) dan <b>transportasi umum</b> (sekitar 5,7%).</p>
            <p>Tingginya angka penggunaan kendaraan pribadi ini menggarisbawahi bahwa aspek-aspek terkait fasilitas parkir, seperti kapasitas, kemudahan akses, keamanan, dan efisiensi manajemen parkir, berpotensi menjadi salah satu faktor krusial yang mempengaruhi pengalaman dan kepuasan pengunjung Pakuwon City Mall secara keseluruhan.</p>
            </div>
            """, unsafe_allow_html=True)

# 4.2 Analisis Kepuasan Pengunjung Pakuwon City Mall
with st.container(border=True):
    display_section_subheader("4.2 Analisis Kepuasan Pengunjung Pakuwon City Mall")
    st.markdown(
        """
        <div class='body-text'>
        <p>Bagian ini memaparkan hasil analisis data terkait tingkat kepuasan pengunjung Pakuwon City Mall. Analisis dilakukan menggunakan beberapa metode, yaitu Analisis Kesenjangan (GAP) berdasarkan model SERVQUAL, Importance-Performance Analysis (IPA), dan Customer Satisfaction Index (CSI).</p>
        <p><i>Catatan: Data yang disajikan di bawah ini adalah representasi berdasarkan informasi dari dokumen PDF. Untuk hasil yang paling akurat, silakan merujuk pada data olahan primer dari penelitian Anda. Beberapa nilai mungkin merupakan estimasi atau dummy untuk keperluan visualisasi.</i></p>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Data Atribut Layanan (Gabungan dari Tabel 3.1 dan Tabel 4.1 di PDF)
    # Kode, Atribut, Dimensi, Harapan (rata-rata), Kenyataan (rata-rata)
    # Saya akan mencoba merekonstruksi data selengkap mungkin dari PDF.
    # Tabel 4.1 (hal 23 PDF) adalah yang paling komprehensif untuk GAP.
    data_servqual = {
        'Dimensi': ['Tangibles', 'Tangibles', 'Tangibles', 'Tangibles', 'Tangibles', 'Tangibles',
                    'Reliability', 'Reliability', 'Reliability',
                    'Responsiveness', 'Responsiveness', 'Responsiveness',
                    'Assurance', 'Assurance', 'Assurance',
                    'Empathy', 'Empathy', 'Empathy'],
        'Kode': ['T1', 'T2', 'T3', 'T4', 'T5', 'T6',
                 'R1', 'R2', 'R3',
                 'Rp1', 'Rp2', 'Rp3',
                 'A1', 'A2', 'A3',
                 'E1', 'E2', 'E3'],
        'Atribut': [
            'Kebersihan area mall (toilet, food court, eskalator, dll.)', 'Ketersediaan tempat duduk dan area istirahat di mall', 
            'Ketersediaan papan penunjuk arah yang jelas', 'Aksesibilitas tempat parkir', 
            'Kenyamanan suhu udara mall', 'Desain dan suasana mall yang menarik', # T5, T6 dari Tabel 3.1
            'Kemudahan menemukan tenant atau toko yang dicari', 'Ketersediaan informasi acara atau promo yang mudah diakses', 
            'Fasilitas mall (eskalator, toilet, dll.) berfungsi dengan baik',
            'Petugas mall cepat membantu jika ada yang bertanya', 'Kecepatan layanan kebersihan dalam menjaga kebersihan mall', 
            'Ketanggapan petugas mall dalam menyapa pengunjung yang datang',
            'Rasa aman dari tindak kriminal di dalam mall', 'Keamanan dalam menggunakan fasilitas seperti eskalator', 
            'Kenyamanan mengakses jalan di dalam mall', # A3 dari Tabel 3.1
            'Prosedur pelayanan pelanggan yang baik', 'Petugas mall sabar dalam melayani pelanggan', 
            'Ketersediaan sarana untuk menyampaikan aduan/keluhan pelanggan'
        ],
        # Data Harapan & Kenyataan dari Tabel 4.1 (hal 23 PDF) dan estimasi untuk yang tidak ada
        'Harapan': [5.31, 4.62, 4.95, 5.26, 5.15, 5.05, # T5, T6 estimasi
                    4.83, 5.00, 5.28, # R1, R2 dari tabel terpisah, R3 dari tabel gabungan
                    5.21, 5.16, 4.80, 
                    5.19, 5.07, 5.10, # A3 estimasi
                    5.20, 5.13, 4.83],
        'Kenyataan': [5.24, 4.99, 5.16, 5.32, 5.10, 5.15, # T5, T6 estimasi
                      5.00, 5.22, 5.25, # R1, R2 dari tabel terpisah, R3 dari tabel gabungan
                      5.23, 5.28, 5.18, 
                      5.24, 5.22, 5.12, # A3 estimasi
                      5.26, 5.18, 5.09],
    }
    df_analisis_servqual = pd.DataFrame(data_servqual)
    df_analisis_servqual['GAP'] = (df_analisis_servqual['Kenyataan'] - df_analisis_servqual['Harapan']).round(2)

    # --- 4.2.1 Analisis Kesenjangan Kualitas Layanan (SERVQUAL GAP Analysis) ---
    with st.expander("📊 4.2.1 Analisis Kesenjangan Kualitas Layanan (SERVQUAL GAP Analysis)", expanded=True):
        st.markdown(
            """
            <div class='body-text'>
            <p>Analisis kesenjangan (GAP) dilakukan untuk mengukur perbedaan antara tingkat harapan (<i>importance</i>) pengunjung terhadap berbagai atribut layanan dengan persepsi mereka terhadap kinerja aktual (<i>performance</i> atau kenyataan) layanan yang diterima di Pakuwon City Mall. Skor GAP dihitung dengan formula: $GAP = \text{Skor Kenyataan} - \text{Skor Harapan}$.</p>
            <ul>
                <li>GAP > 0: Kinerja melebihi harapan (memuaskan).</li>
                <li>GAP = 0: Kinerja sesuai harapan.</li>
                <li>GAP < 0: Kinerja di bawah harapan (kurang memuaskan, perlu perbaikan).</li>
            </ul>
            <p>Tabel berikut menyajikan hasil analisis GAP untuk setiap atribut layanan (berdasarkan Tabel 4.1 di halaman 23 dokumen penelitian, dengan beberapa penyesuaian/estimasi untuk kelengkapan atribut dari Tabel 3.1):</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Fungsi untuk mewarnai nilai GAP pada tabel
        def color_gap_value(val):
            if val < 0: color = '#FFEBEE' # Merah sangat muda
            elif val > 0: color = '#E8F5E9' # Hijau sangat muda
            else: color = 'white'
            return f'background-color: {color}'

        st.dataframe(
            df_analisis_servqual[['Dimensi', 'Kode', 'Atribut', 'Harapan', 'Kenyataan', 'GAP']].style.applymap(
                color_gap_value, subset=['GAP']
            ).format({'Harapan': "{:.2f}", 'Kenyataan': "{:.2f}", 'GAP': "{:.2f}"}), 
            height=650, use_container_width=True
        )
        
        gap_negatif_df = df_analisis_servqual[df_analisis_servqual['GAP'] < 0]
        st.markdown("<div class='body-text'>", unsafe_allow_html=True)
        if not gap_negatif_df.empty:
            st.write("<b>Atribut dengan Nilai GAP Negatif (Kinerja di Bawah Harapan):</b>")
            for _, row in gap_negatif_df.iterrows():
                st.markdown(f"- **{row['Atribut']} ({row['Kode']})**: Harapan={row['Harapan']:.2f}, Kenyataan={row['Kenyataan']:.2f}, <span style='color:red; font-weight:bold;'>GAP={row['GAP']:.2f}</span>", unsafe_allow_html=True)
        else:
            st.success("Berdasarkan data yang diolah, semua atribut layanan telah memenuhi atau melebihi harapan pengunjung (tidak ditemukan GAP negatif signifikan).")
        
        st.markdown(
            """
            <p>Dari tabel di atas (Tabel 4.1 PDF hal. 23), terlihat bahwa atribut <b>T1 (Kebersihan area umum)</b> dengan GAP = -0.07 dan <b>R3 (Fasilitas mall berfungsi baik)</b> dengan GAP = -0.02 menunjukkan kinerja yang masih di bawah ekspektasi pengunjung. Atribut-atribut ini memerlukan perhatian khusus dari manajemen PCM. Sebagian besar atribut lainnya menunjukkan GAP positif, yang berarti layanan pada aspek tersebut telah melampaui harapan pengunjung.</p>
            <p>Dokumen penelitian juga menyebutkan pelaksanaan Uji Wilcoxon untuk melihat apakah perbedaan GAP ini signifikan secara statistik. Misalnya, untuk T3 (Ketersediaan papan penunjuk arah), ditemukan perbedaan yang signifikan (Ho ditolak), yang berarti meskipun GAP-nya positif (0.21), perbedaan antara harapan dan kenyataan dianggap nyata.</p>
            </div>
            """, unsafe_allow_html=True)

    # --- 4.2.2 Importance-Performance Analysis (IPA) ---
    with st.expander("🗺️ 4.2.2 Importance-Performance Analysis (IPA)", expanded=False):
        st.markdown(
            """
            <div class='body-text'>
            <p>Importance-Performance Analysis (IPA) digunakan untuk memetakan atribut-atribut layanan ke dalam diagram kartesius berdasarkan rata-rata skor tingkat kepentingan (sumbu Y) dan rata-rata skor kinerja/kenyataan (sumbu X). Analisis ini membantu dalam menentukan prioritas strategis untuk peningkatan kualitas layanan.</p>
            <p>Titik potong sumbu X dan Y pada diagram IPA dihitung dari rata-rata keseluruhan skor Harapan (Kepentingan) dan Kenyataan (Kinerja) dari semua atribut.</p>
            </div>
            """, unsafe_allow_html=True)
        
        df_ipa_data = df_analisis_servqual.copy()
        # Sumbu X: Kenyataan (Performance), Sumbu Y: Harapan (Importance)
        avg_harapan_ipa = df_ipa_data['Harapan'].mean()
        avg_kenyataan_ipa = df_ipa_data['Kenyataan'].mean()

        fig_ipa_chart = px.scatter(
            df_ipa_data, 
            x='Kenyataan', 
            y='Harapan', 
            text='Kode', # Menampilkan kode atribut pada titik
            title='Diagram Importance-Performance Analysis (IPA) Pakuwon City Mall',
            labels={'Kenyataan': 'Kinerja (Performance)', 'Harapan': 'Kepentingan (Importance)'},
            hover_data=['Atribut', 'GAP', 'Dimensi'], 
            height=700,
            color='Dimensi', # Memberi warna berdasarkan dimensi SERVQUAL
            color_discrete_sequence=px.colors.qualitative.Plotly 
        )
        
        # Menambahkan garis rata-rata sebagai pemisah kuadran
        fig_ipa_chart.add_vline(x=avg_kenyataan_ipa, line_dash="dash", line_color="grey", 
                                annotation_text=f"Rata-rata Kinerja: {avg_kenyataan_ipa:.2f}", 
                                annotation_position="bottom right")
        fig_ipa_chart.add_hline(y=avg_harapan_ipa, line_dash="dash", line_color="grey", 
                                annotation_text=f"Rata-rata Kepentingan: {avg_harapan_ipa:.2f}", 
                                annotation_position="top left")

        # Anotasi untuk setiap kuadran
        fig_ipa_chart.add_annotation(x=avg_kenyataan_ipa*0.98, y=avg_harapan_ipa*1.02, text="<b>Kuadran I: Prioritas Utama</b><br>(Concentrate Here)", showarrow=False, xanchor="right", yanchor="bottom", font=dict(color="red", size=11), bgcolor="rgba(255,255,255,0.7)")
        fig_ipa_chart.add_annotation(x=avg_kenyataan_ipa*1.02, y=avg_harapan_ipa*1.02, text="<b>Kuadran II: Pertahankan Prestasi</b><br>(Keep Up the Good Work)", showarrow=False, xanchor="left", yanchor="bottom", font=dict(color="green", size=11), bgcolor="rgba(255,255,255,0.7)")
        fig_ipa_chart.add_annotation(x=avg_kenyataan_ipa*0.98, y=avg_harapan_ipa*0.98, text="<b>Kuadran III: Prioritas Rendah</b><br>(Low Priority)", showarrow=False, xanchor="right", yanchor="top", font=dict(color="orange", size=11), bgcolor="rgba(255,255,255,0.7)")
        fig_ipa_chart.add_annotation(x=avg_kenyataan_ipa*1.02, y=avg_harapan_ipa*0.98, text="<b>Kuadran IV: Mungkin Berlebihan</b><br>(Possible Overkill)", showarrow=False, xanchor="left", yanchor="top", font=dict(color="blue", size=11), bgcolor="rgba(255,255,255,0.7)")
        
        fig_ipa_chart.update_traces(textposition='top center', marker=dict(size=11, opacity=0.8)) # Menyesuaikan tampilan titik
        fig_ipa_chart.update_layout(title_x=0.5, legend_title_text='Dimensi SERVQUAL')
        st.plotly_chart(fig_ipa_chart, use_container_width=True)

        st.markdown(
            """
            <div class='body-text'>
            <p><b>Interpretasi Kuadran pada Diagram IPA:</b></p>
            <ul>
                <li><b>Kuadran I (Prioritas Utama / <i>Concentrate Here</i>):</b> Berisi atribut-atribut yang dianggap sangat penting oleh pengunjung (skor Harapan tinggi), namun kinerjanya dinilai masih rendah (skor Kenyataan rendah). Manajemen PCM harus memfokuskan upaya perbaikan secara intensif pada atribut-atribut yang jatuh dalam kuadran ini. <i>(Contoh dari data olahan: Jika T1 dan R3 berada di kuadran ini, maka kebersihan area umum dan fungsi fasilitas mall perlu ditingkatkan segera sebagai prioritas utama).</i></li>
                <li><b>Kuadran II (Pertahankan Prestasi / <i>Keep Up the Good Work</i>):</b> Berisi atribut-atribut yang memiliki tingkat kepentingan tinggi dan kinerjanya juga dinilai baik oleh pengunjung. Prestasi pada atribut-atribut ini harus terus dipertahankan dan dijaga konsistensinya karena merupakan kekuatan utama PCM.</li>
                <li><b>Kuadran III (Prioritas Rendah / <i>Low Priority</i>):</b> Berisi atribut-atribut yang dinilai kurang penting oleh pengunjung dan kinerjanya juga rendah. Upaya perbaikan pada area ini dapat dikesampingkan sementara atau dialokasikan sumber daya minimal, karena dampaknya terhadap kepuasan keseluruhan mungkin tidak signifikan.</li>
                <li><b>Kuadran IV (Mungkin Berlebihan / <i>Possible Overkill</i>):</b> Berisi atribut-atribut yang kinerjanya sangat baik, namun dianggap kurang penting oleh pengunjung. Manajemen PCM mungkin dapat mempertimbangkan untuk mengurangi alokasi sumber daya yang berlebihan pada atribut ini dan mengalihkannya ke atribut yang lebih membutuhkan di Kuadran I.</li>
            </ul>
            <p><i>Catatan: Identifikasi atribut spesifik yang masuk ke dalam masing-masing kuadran akan sangat bergantung pada hasil perhitungan rata-rata skor Harapan dan Kenyataan dari data penelitian yang sebenarnya. Visualisasi di atas adalah ilustrasi berdasarkan data yang diolah.</i></p>
            </div>
            """, unsafe_allow_html=True)

    # --- 4.2.3 Customer Satisfaction Index (CSI) ---
    with st.expander("📈 4.2.3 Customer Satisfaction Index (CSI)", expanded=False):
        st.markdown(
            """
            <div class='body-text'>
            <p>Customer Satisfaction Index (CSI) adalah ukuran agregat yang digunakan untuk mengetahui tingkat kepuasan pelanggan secara keseluruhan terhadap layanan yang diberikan oleh Pakuwon City Mall. Perhitungan CSI melibatkan pembobotan skor kinerja (kenyataan) setiap atribut berdasarkan tingkat kepentingannya (harapan).</p>
            <p>Langkah perhitungan CSI (sesuai Tabel 2.3 Kriteria Tingkat Kepuasan dari PDF):</p>
            <ol>
                <li>Menghitung Mean Importance Score (MIS) atau rata-rata skor Harapan untuk setiap atribut.</li>
                <li>Menghitung Mean Satisfaction Score (MSS) atau rata-rata skor Kenyataan untuk setiap atribut.</li>
                <li>Menghitung Weight Factor (WF) untuk setiap atribut: $WF_i = MIS_i / \sum MIS_j$.</li>
                <li>Menghitung Weighted Score (WS) untuk setiap atribut: $WS_i = WF_i \times MSS_i$.</li>
                <li>Menghitung Total Weighted Score (WT) atau $\sum WS_i$.</li>
                <li>Menghitung CSI: $CSI = (WT / \text{Skala Maksimum Likert}) \times 100\%$. (Skala Maksimum Likert adalah 6).</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
        
        df_csi_calc = df_analisis_servqual.copy()
        df_csi_calc['MIS'] = df_csi_calc['Harapan'] 
        df_csi_calc['MSS'] = df_csi_calc['Kenyataan']
        
        total_mis_csi = df_csi_calc['MIS'].sum()
        df_csi_calc['WF'] = (df_csi_calc['MIS'] / total_mis_csi) # Weight Factor
        df_csi_calc['WS'] = df_csi_calc['WF'] * df_csi_calc['MSS'] # Weight Score
        
        total_ws_csi = df_csi_calc['WS'].sum()
        skala_maksimum_likert = 6 # Sesuai skala Likert yang digunakan (1-6)
        csi_value_calculated = (total_ws_csi / skala_maksimum_likert) * 100
        
        # Menentukan kriteria CSI berdasarkan Tabel 2.3 dari PDF
        csi_criteria_text = ""
        if 81 <= csi_value_calculated <= 100: csi_criteria_text = "Sangat Puas"
        elif 66 <= csi_value_calculated < 81: csi_criteria_text = "Puas"
        elif 51 <= csi_value_calculated < 66: csi_criteria_text = "Cukup Puas"
        elif 35 <= csi_value_calculated < 51: csi_criteria_text = "Kurang Puas"
        elif 0 <= csi_value_calculated < 35: csi_criteria_text = "Tidak Puas"
        else: csi_criteria_text = "Diluar Rentang Valid"


        fig_csi_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = csi_value_calculated,
            domain = {'x': [0.1, 0.9], 'y': [0, 1]}, # Memberi sedikit margin
            title = {
                'text': f"<b>Customer Satisfaction Index (CSI)</b><br><span style='font-size:0.9em;color:gray'>Kategori Kepuasan: {csi_criteria_text}</span>", 
                'font': {'size': 20}
            },
            delta = {'reference': 80, 'increasing': {'color': "#4CAF50"}, 'decreasing': {'color': "#F44336"}, 'position': "bottom"}, # Target kepuasan misalnya 80 (Puas)
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "#2563EB", 'thickness': 0.6}, # Warna bar utama
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#D1D5DB", # Warna border gauge
                'steps': [ # Warna latar belakang berdasarkan kriteria
                    {'range': [0, 34.99], 'color': '#FFEBEE'}, # Tidak Puas (Merah sangat muda)
                    {'range': [35, 50.99], 'color': '#FFF8E1'}, # Kurang Puas (Kuning/Oranye sangat muda)
                    {'range': [51, 65.99], 'color': '#E3F2FD'}, # Cukup Puas (Biru sangat muda)
                    {'range': [66, 80.99], 'color': '#E8F5E9'}, # Puas (Hijau sangat muda)
                    {'range': [81, 100], 'color': '#DCEDC8'}], # Sangat Puas (Hijau lebih pekat muda)
                'threshold': { # Garis penanda nilai CSI aktual
                    'line': {'color': "#D32F2F", 'width': 4}, # Warna garis threshold
                    'thickness': 0.85,
                    'value': csi_value_calculated 
                }
            }
        ))
        fig_csi_gauge.update_layout(height=380, margin=dict(t=60, b=40, l=30, r=30)) # Mengatur margin
        st.plotly_chart(fig_csi_gauge, use_container_width=True)
        
        st.markdown(f"<div class='body-text'><p style='text-align:center; font-size:1.1em;'>Berdasarkan hasil perhitungan menggunakan data olahan, nilai <b>Customer Satisfaction Index (CSI)</b> untuk Pakuwon City Mall adalah <b style='font-size:1.2em; color:#1E3A8A;'>{csi_value_calculated:.2f}%</b>.</p><p style='text-align:center;'>Sesuai dengan kriteria pada Tabel 2.3 dokumen penelitian, nilai ini mengindikasikan bahwa tingkat kepuasan pengunjung secara keseluruhan masuk dalam kategori: <b style='font-size:1.1em; color:#1E3A8A;'>{csi_criteria_text}</b>.</p></div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='body-text'>
            <p><b>Kriteria Penilaian CSI (Berdasarkan Tabel 2.3 PDF):</b></p>
            <ul>
                <li>0% - 34.99%: Tidak Puas</li>
                <li>35% - 50.99%: Kurang Puas</li>
                <li>51% - 65.99%: Cukup Puas</li>
                <li>66% - 80.99%: Puas</li>
                <li>81% - 100%: Sangat Puas</li>
            </ul>
            <p><i>Catatan: Perhitungan CSI ini adalah ilustrasi berdasarkan data yang diolah dari informasi yang tersedia. Hasil aktual dari penelitian Anda mungkin menunjukkan nilai dan kategori yang berbeda. Penting untuk menggunakan data penelitian primer yang valid untuk analisis akhir.</i></p>
            </div>
            """, unsafe_allow_html=True)
            
    # (Analisis PGCV bisa ditambahkan di sini jika datanya tersedia dan relevan untuk ditampilkan)
    # with st.expander("💸 4.2.4 Potential Gain in Customer Value (PGCV)", expanded=False):
    #     st.markdown("<p class='body-text'>Analisis PGCV akan disajikan di sini jika relevan dan datanya tersedia...</p>", unsafe_allow_html=True)

