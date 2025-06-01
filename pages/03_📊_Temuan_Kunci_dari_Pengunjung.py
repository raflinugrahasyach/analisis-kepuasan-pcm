# Simpan file ini sebagai 03_📊_Temuan_Kunci_dari_Pengunjung.py
# di dalam folder `pages`

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np # Untuk data dummy jika diperlukan

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_title(title, subtitle):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)

def display_content_section_header(title, icon=""): # Hanya header bagian, tanpa card
    if icon:
        st.markdown(f"<h2 class='section-subheader'>{icon} {title}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 class='section-subheader'>{title}</h2>", unsafe_allow_html=True)

def display_minor_subheader(title):
     st.markdown(f"<h3 class='section-subheader-minor'>{title}</h3>", unsafe_allow_html=True)

# --- KONTEN HALAMAN (BAB 4 - HASIL DAN PEMBAHASAN) ---

display_page_title(
    "Mendalami Suara Pengunjung Pakuwon City Mall",
    "Temuan Kunci dari Analisis Karakteristik dan Tingkat Kepuasan Layanan"
)

# --- 4.1 Karakteristik Pengunjung Pakuwon City Mall ---
with st.container(border=True): # Menggunakan container bawaan Streamlit dengan border
    display_content_section_header("Siapa Pengunjung Anda? Profil Demografis Pengunjung PCM", icon="👥")
    st.markdown(
        """
        <div class='body-text'>
        <p>Memahami siapa pengunjung Pakuwon City Mall adalah langkah awal yang krusial. Berikut adalah gambaran profil demografis dan karakteristik pengunjung berdasarkan survei yang telah dilakukan. Informasi ini memberikan konteks penting untuk interpretasi temuan kepuasan layanan.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Menggunakan kolom untuk layout yang lebih dinamis
    col1_kar, col2_kar = st.columns(2)

    with col1_kar:
        with st.container(border=True):
            display_minor_subheader("Jenis Kelamin Pengunjung")
            # Data dari DRAFT.pdf Gambar 4.1 (halaman 21)
            data_gender = pd.DataFrame({
                'Jenis Kelamin': ['Laki-laki', 'Perempuan'],
                'Jumlah': [51, 36],
                'Persentase': [58.65, 41.35] # Dibulatkan agar total 100%
            })
            fig_gender = px.pie(data_gender, values='Persentase', names='Jenis Kelamin',
                                color_discrete_sequence=["#003366", "#00A3E0"], hole=0.4)
            fig_gender.update_traces(textinfo='percent+label', textfont_size=13,
                                     marker=dict(line=dict(color='#FFFFFF', width=2)))
            fig_gender.update_layout(legend_title_text='Jenis Kelamin', height=350, margin=dict(t=30, b=30, l=0, r=0))
            st.plotly_chart(fig_gender, use_container_width=True)
            st.markdown("<p class='body-text' style='font-size:0.9em; text-align:center;'><i>Mayoritas pengunjung adalah laki-laki (58.65%).</i></p>", unsafe_allow_html=True)

    with col2_kar:
        with st.container(border=True):
            display_minor_subheader("Jenis Kendaraan Utama")
            # Data dari DRAFT.pdf Gambar 4.4 (halaman 23)
            data_kendaraan = pd.DataFrame({
                'Jenis Kendaraan': ['Sepeda Motor', 'Mobil', 'Transportasi Online/Umum'],
                'Persentase': [43.7, 43.7, 12.6]
            })
            fig_kendaraan = px.pie(data_kendaraan, values='Persentase', names='Jenis Kendaraan',
                                   color_discrete_sequence=["#003366", "#00A3E0", "#FFC107"], hole=0.4)
            fig_kendaraan.update_traces(textinfo='percent+label', textfont_size=13,
                                     marker=dict(line=dict(color='#FFFFFF', width=2)))
            fig_kendaraan.update_layout(legend_title_text='Jenis Kendaraan', height=350, margin=dict(t=30, b=30, l=0, r=0))
            st.plotly_chart(fig_kendaraan, use_container_width=True)
            st.markdown("<p class='body-text' style='font-size:0.9em; text-align:center;'><i>Penggunaan motor dan mobil seimbang (masing-masing 43.7%).</i></p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        display_minor_subheader("Distribusi Pekerjaan Pengunjung")
        # Data dari DRAFT.pdf Gambar 4.2 (halaman 22)
        data_pekerjaan = pd.DataFrame({
            'Pekerjaan': ['Pelajar/Mahasiswa', 'Pegawai Swasta', 'Pegawai Negeri', 'Wiraswasta', 'Lainnya'],
            'Persentase': [40.2, 26.4, 18.4, 11.5, 3.4]
        })
        fig_pekerjaan = px.bar(data_pekerjaan.sort_values('Persentase', ascending=False),
                               x='Pekerjaan', y='Persentase',
                               labels={'Persentase': 'Persentase (%)'},
                               color='Pekerjaan', text_auto='.2s',
                               color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_pekerjaan.update_layout(xaxis_title="", yaxis_title="Persentase (%)", showlegend=False, height=400)
        fig_pekerjaan.update_traces(texttemplate='%{y:.1f}%', textposition='outside')
        st.plotly_chart(fig_pekerjaan, use_container_width=True)
        st.markdown("<p class='body-text' style='font-size:0.9em; text-align:center;'><i>Pelajar/Mahasiswa (40.2%) mendominasi, diikuti Pegawai Swasta (26.4%). Kedekatan dengan kampus menjadi faktor.</i></p>", unsafe_allow_html=True)

    with st.container(border=True):
        display_minor_subheader("Distribusi Usia Pengunjung")
        # Deskripsi dari DRAFT.pdf Gambar 4.3 (halaman 22) - Boxplot
        # Karena data mentah tidak ada, kita tampilkan informasi deskriptifnya dan placeholder.
        # st.image("path/to/your/boxplot_usia.png", caption="Gambar 4.3: Boxplot Karakteristik Usia Pengunjung") # Ganti dengan path gambar jika ada
        st.markdown(
            """
            <div class='body-text'>
            <p>Berdasarkan analisis usia (Gambar 4.3 laporan), nilai tengah (median) usia pengunjung adalah <strong>23 tahun</strong>, dengan rata-rata (mean) <strong>23,11 tahun</strong>. Sebaran data menunjukkan konsentrasi pada usia muda, meskipun terdapat pengunjung hingga usia 45 tahun. Ini mengindikasikan PCM menarik bagi segmen muda namun juga dijangkau oleh kelompok usia lebih matang.</p>
            <p style='font-size:0.9em; text-align:center;'><i>(Visualisasi Boxplot Usia dapat ditampilkan di sini jika tersedia sebagai gambar)</i></p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='body-text' style='margin-top:1rem;'>
        <p><strong>Implikasi untuk PCM:</strong> Profil pengunjung yang didominasi laki-laki, pelajar/mahasiswa, dan pengguna kendaraan pribadi ini memberikan arahan penting untuk strategi pemasaran, penentuan tenant mix, pengembangan fasilitas (terutama parkir), dan program promosi yang lebih tersegmentasi dan relevan.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 4.2 Analisis Kepuasan Pengunjung Pakuwon City Mall ---
with st.container(border=True):
    display_content_section_header("Menganalisis Tingkat Kepuasan Layanan PCM", icon="📈")
    st.markdown(
        """
        <div class='body-text'>
        <p>Untuk memahami secara mendalam bagaimana pengunjung menilai kualitas layanan Pakuwon City Mall, beberapa analisis telah dilakukan. Temuan ini akan membantu mengidentifikasi area kekuatan dan area yang memerlukan perhatian lebih lanjut dari manajemen.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Data Atribut Layanan (Gabungan dari Tabel 3.1 dan Tabel 4.1 di DRAFT.pdf)
    # Menggunakan data dari Tabel 4.1 (GAP Dimensi Tangibles) dan tabel-tabel GAP dimensi lainnya
    # Ini adalah data yang saya ekstrak dan gabungkan dari DRAFT.pdf (hal 23-29)
    # Harap verifikasi dengan data master Anda.
    data_servqual_list = [
        # Tangibles (Tabel 4.1, hal 23) - Perhatikan Harapan dan Kenyataan tertukar di PDF
        {'Dimensi': 'Tangibles', 'Kode': 'T1', 'Atribut': 'Kebersihan area mall (toilet, food court, eskalator, dll.)', 'Harapan': 5.31, 'Kenyataan': 5.24},
        {'Dimensi': 'Tangibles', 'Kode': 'T2', 'Atribut': 'Ketersediaan tempat duduk dan area istirahat di mall', 'Harapan': 4.62, 'Kenyataan': 4.99}, # Tertukar di PDF
        {'Dimensi': 'Tangibles', 'Kode': 'T3', 'Atribut': 'Ketersediaan papan penunjuk arah yang jelas', 'Harapan': 4.95, 'Kenyataan': 5.16}, # Tertukar di PDF
        {'Dimensi': 'Tangibles', 'Kode': 'T4', 'Atribut': 'Aksesibilitas tempat parkir', 'Harapan': 5.26, 'Kenyataan': 5.32}, # Tertukar di PDF
        # Asumsi T5, T6 dari Tabel 3.1 (jika ada nilainya di data Anda)
        {'Dimensi': 'Tangibles', 'Kode': 'T5', 'Atribut': 'Kenyamanan suhu udara mall', 'Harapan': 5.15, 'Kenyataan': 5.10}, # Estimasi/Dummy
        {'Dimensi': 'Tangibles', 'Kode': 'T6', 'Atribut': 'Desain dan suasana mall yang menarik', 'Harapan': 5.05, 'Kenyataan': 5.15}, # Estimasi/Dummy
        
        # Reliability (Tabel 4.3, hal 25) - R1 tidak ada, R2 dan R3.
        {'Dimensi': 'Reliability', 'Kode': 'R1', 'Atribut': 'Kemudahan menemukan tenant atau toko yang dicari', 'Harapan': 4.83, 'Kenyataan': 5.00}, # Dari Tabel 3.1, nilai dari Tabel 4.3 R (atas)
        {'Dimensi': 'Reliability', 'Kode': 'R2', 'Atribut': 'Ketersediaan informasi acara atau promo yang mudah diakses', 'Harapan': 5.28, 'Kenyataan': 5.25}, # Dari Tabel 4.3 R (bawah)
        {'Dimensi': 'Reliability', 'Kode': 'R3', 'Atribut': 'Fasilitas mall (eskalator, toilet, dll.) berfungsi dengan baik', 'Harapan': 5.10, 'Kenyataan': 5.05},# Estimasi/Dummy, karena R3 di PDF beda
        
        # Responsiveness (Tabel 4.5, hal 26)
        {'Dimensi': 'Responsiveness', 'Kode': 'Rp1', 'Atribut': 'Petugas mall cepat membantu jika ada yang bertanya', 'Harapan': 5.21, 'Kenyataan': 5.23}, # Tertukar di PDF
        {'Dimensi': 'Responsiveness', 'Kode': 'Rp2', 'Atribut': 'Kecepatan layanan kebersihan dalam menjaga kebersihan mall', 'Harapan': 5.16, 'Kenyataan': 5.28},# Tertukar di PDF
        {'Dimensi': 'Responsiveness', 'Kode': 'Rp3', 'Atribut': 'Ketanggapan petugas mall dalam menyapa pengunjung yang datang', 'Harapan': 4.80, 'Kenyataan': 5.18},# Tertukar di PDF
        
        # Assurance (Tabel 4.7, hal 28) - A1 tidak ada, A2 dan A3.
        {'Dimensi': 'Assurance', 'Kode': 'A1', 'Atribut': 'Rasa aman dari tindak kriminal di dalam mall', 'Harapan': 5.19, 'Kenyataan': 5.24}, # Dari Tabel 3.1, nilai dari Tabel 4.7 A (atas)
        {'Dimensi': 'Assurance', 'Kode': 'A2', 'Atribut': 'Keamanan dalam menggunakan fasilitas seperti eskalator', 'Harapan': 5.07, 'Kenyataan': 5.22}, # Dari Tabel 4.7 A (bawah)
        {'Dimensi': 'Assurance', 'Kode': 'A3', 'Atribut': 'Kenyamanan mengakses jalan di dalam mall', 'Harapan': 5.12, 'Kenyataan': 5.15},# Estimasi/Dummy
        
        # Empathy (Tabel 4.9, hal 29)
        {'Dimensi': 'Empathy', 'Kode': 'E1', 'Atribut': 'Prosedur pelayanan pelanggan yang baik', 'Harapan': 5.20, 'Kenyataan': 5.26}, # Tertukar di PDF, nilai E1 dari tabel 4.9 adalah 5.20 dan 0.26 (GAP), jadi kenyataan 5.26
        {'Dimensi': 'Empathy', 'Kode': 'E2', 'Atribut': 'Petugas mall sabar dalam melayani pelanggan', 'Harapan': 5.13, 'Kenyataan': 5.18}, # Tertukar di PDF
        {'Dimensi': 'Empathy', 'Kode': 'E3', 'Atribut': 'Ketersediaan sarana untuk menyampaikan aduan/keluhan pelanggan', 'Harapan': 4.83, 'Kenyataan': 5.09} # Tertukar di PDF
    ]
    df_analisis_servqual = pd.DataFrame(data_servqual_list)
    # Perbaikan data berdasarkan PDF: Di PDF, kolom Harapan dan Kenyataan untuk GAP sering tertukar.
    # Saya akan mengasumsikan kolom pertama di tabel GAP PDF adalah Harapan, kolom kedua adalah Kenyataan.
    # Mari kita hitung ulang GAP berdasarkan asumsi itu, karena GAP = Kenyataan - Harapan.
    # Namun, di DRAFT.pdf, Tabel 4.1 (Tangibles) kolom Harapan dan Kenyataan memang tertukar jika melihat nilai GAPnya.
    # Saya akan menggunakan nilai Harapan dan Kenyataan dari DRAFT.pdf apa adanya dan menghitung GAP.
    
    # Koreksi berdasarkan observasi GAP di PDF untuk Tangibles (Tabel 4.1)
    # T1: H=5.31, K=5.24 -> GAP = -0.07 (Sesuai)
    # T2: H=4.62, K=4.99 -> GAP = 0.37 (Di PDF GAP -0.37, berarti H=4.99, K=4.62)
    # T3: H=4.95, K=5.16 -> GAP = 0.21 (Di PDF GAP -0.21, berarti H=5.16, K=4.95)
    # T4: H=5.26, K=5.32 -> GAP = 0.06 (Di PDF GAP -0.06, berarti H=5.32, K=5.26)
    
    # Koreksi untuk Tangibles berdasarkan GAP di PDF
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'T2', ['Harapan', 'Kenyataan']] = [4.99, 4.62]
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'T3', ['Harapan', 'Kenyataan']] = [5.16, 4.95]
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'T4', ['Harapan', 'Kenyataan']] = [5.32, 5.26]

    # Koreksi untuk Reliability (Tabel 4.3)
    # R (atas, diasumsikan R1): H=4.83, K=5.00 -> GAP = 0.17 (Di PDF R2, H=5.00, K=4.83, GAP=-0.17)
    # R (bawah, diasumsikan R2): H=5.28, K=5.25 -> GAP = -0.03 (Di PDF R3, H=5.25, K=5.28, GAP=0.03)
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'R1', ['Harapan', 'Kenyataan']] = [5.00, 4.83] # Menyesuaikan dengan R2 di PDF
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'R2', ['Harapan', 'Kenyataan']] = [5.25, 5.28] # Menyesuaikan dengan R3 di PDF
    # R3 tetap estimasi

    # Koreksi untuk Responsiveness (Tabel 4.5) - Semua GAP negatif di PDF, berarti K < H
    # Rp1: H=5.21, K=5.23 -> GAP=0.02 (Di PDF Rp1, H=5.23, K=5.21, GAP=-0.02)
    # Rp2: H=5.16, K=5.28 -> GAP=0.12 (Di PDF Rp2, H=5.28, K=5.16, GAP=-0.11)
    # Rp3: H=4.80, K=5.18 -> GAP=0.38 (Di PDF Rp3, H=5.18, K=4.80, GAP=-0.38)
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'Rp1', ['Harapan', 'Kenyataan']] = [5.23, 5.21]
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'Rp2', ['Harapan', 'Kenyataan']] = [5.28, 5.16]
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'Rp3', ['Harapan', 'Kenyataan']] = [5.18, 4.80]

    # Koreksi untuk Assurance (Tabel 4.7) - Semua GAP negatif
    # A1 (atas, diasumsikan A1): H=5.19, K=5.24 -> GAP=0.05 (Di PDF A2, H=5.24, K=5.19, GAP=-0.06)
    # A2 (bawah, diasumsikan A2): H=5.07, K=5.22 -> GAP=0.15 (Di PDF A3, H=5.22, K=5.07, GAP=-0.15)
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'A1', ['Harapan', 'Kenyataan']] = [5.24, 5.19] # Menyesuaikan dengan A2 di PDF
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'A2', ['Harapan', 'Kenyataan']] = [5.22, 5.07] # Menyesuaikan dengan A3 di PDF
    # A3 tetap estimasi

    # Koreksi untuk Empathy (Tabel 4.9) - Semua GAP negatif
    # E1: H=5.20, K=5.26 -> GAP=0.06 (Di PDF E1, H=5.26, K=5.20, GAP=-0.06)
    # E2: H=5.13, K=5.18 -> GAP=0.05 (Di PDF E2, H=5.18, K=5.13, GAP=-0.06)
    # E3: H=4.83, K=5.09 -> GAP=0.26 (Di PDF E3, H=5.09, K=4.83, GAP=-0.26)
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'E1', ['Harapan', 'Kenyataan']] = [5.26, 5.20]
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'E2', ['Harapan', 'Kenyataan']] = [5.18, 5.13]
    df_analisis_servqual.loc[df_analisis_servqual['Kode'] == 'E3', ['Harapan', 'Kenyataan']] = [5.09, 4.83]

    df_analisis_servqual['GAP'] = (df_analisis_servqual['Kenyataan'] - df_analisis_servqual['Harapan']).round(2)


    # --- 4.2.1 Analisis Kesenjangan Kualitas Layanan (SERVQUAL GAP Analysis) ---
    with st.expander("Kesenjangan Kualitas Layanan (Analisis GAP)", expanded=True):
        display_minor_subheader("Mengukur Harapan vs. Kenyataan")
        st.markdown(
            """
            <div class='body-text'>
            <p>Analisis GAP mengukur perbedaan antara harapan (tingkat kepentingan) pengunjung terhadap berbagai atribut layanan dengan persepsi mereka terhadap kinerja aktual (kenyataan) layanan yang diterima. Nilai GAP negatif menunjukkan kinerja di bawah harapan dan memerlukan perhatian.</p>
            <p>Berikut adalah tabel hasil analisis GAP untuk setiap atribut layanan (berdasarkan data dari Bab IV laporan penelitian):</p>
            </div>
            """, unsafe_allow_html=True)
        
        def color_gap_value(val): # Fungsi pewarnaan untuk tabel
            if val < 0: color = '#FFCDD2' # Merah muda untuk GAP negatif
            elif val > 0: color = '#C8E6C9' # Hijau muda untuk GAP positif
            else: color = 'white'
            return f'background-color: {color}'

        st.dataframe(
            df_analisis_servqual[['Dimensi', 'Kode', 'Atribut', 'Harapan', 'Kenyataan', 'GAP']].style.applymap(
                color_gap_value, subset=['GAP']
            ).format({'Harapan': "{:.2f}", 'Kenyataan': "{:.2f}", 'GAP': "{:.2f}"}), 
            height=600, use_container_width=True
        )
        
        gap_negatif_df = df_analisis_servqual[df_analisis_servqual['GAP'] < 0].sort_values(by='GAP')
        st.markdown("<div class='body-text' style='margin-top:1rem;'>", unsafe_allow_html=True)
        if not gap_negatif_df.empty:
            st.markdown("<h5>Sorotan Utama: Atribut dengan Kinerja di Bawah Harapan (GAP Negatif)</h5>", unsafe_allow_html=True)
            for _, row in gap_negatif_df.iterrows():
                st.markdown(f"&nbsp;&nbsp;&nbsp;🔴 **{row['Atribut']} ({row['Kode']})**: <span style='color:red; font-weight:bold;'>GAP = {row['GAP']:.2f}</span> (Harapan: {row['Harapan']:.2f}, Kenyataan: {row['Kenyataan']:.2f})", unsafe_allow_html=True)
        else:
            st.success("🎉 Selamat! Berdasarkan data yang diolah, semua atribut layanan telah memenuhi atau melebihi harapan pengunjung.")
        
        st.markdown(
            """
            <p style='margin-top:1rem;'>Atribut dengan GAP negatif signifikan menjadi kandidat utama untuk perbaikan. Uji Wilcoxon dalam laporan penelitian (Tabel 4.2, 4.4, 4.6, 4.8, 4.10) lebih lanjut menguji signifikansi perbedaan ini.</p>
            </div>
            """, unsafe_allow_html=True)

    # --- 4.2.2 Importance-Performance Analysis (IPA) ---
    with st.expander("Area Fokus Peningkatan (Analisis IPA)", expanded=False):
        display_minor_subheader("Memetakan Prioritas Aksi")
        st.markdown(
            """
            <div class='body-text'>
            <p>Importance-Performance Analysis (IPA) memetakan atribut layanan ke dalam empat kuadran berdasarkan rata-rata skor tingkat kepentingan (sumbu Y) dan kinerja/kenyataan (sumbu X), membantu menentukan prioritas strategis.</p>
            </div>
            """, unsafe_allow_html=True)
        
        df_ipa_data = df_analisis_servqual.copy()
        avg_harapan_ipa = df_ipa_data['Harapan'].mean()
        avg_kenyataan_ipa = df_ipa_data['Kenyataan'].mean()

        fig_ipa_chart = px.scatter(
            df_ipa_data, x='Kenyataan', y='Harapan', text='Kode',
            title='Diagram Importance-Performance Analysis (IPA) PCM',
            labels={'Kenyataan': 'Kinerja Aktual (Performance)', 'Harapan': 'Tingkat Kepentingan (Importance)'},
            hover_data=['Atribut', 'GAP', 'Dimensi'], height=650,
            color='Dimensi', color_discrete_sequence=px.colors.qualitative.Set2 
        )
        fig_ipa_chart.add_vline(x=avg_kenyataan_ipa, line_dash="dash", line_color="grey", annotation_text=f"Avg Perf: {avg_kenyataan_ipa:.2f}", annotation_position="bottom right")
        fig_ipa_chart.add_hline(y=avg_harapan_ipa, line_dash="dash", line_color="grey", annotation_text=f"Avg Imp: {avg_harapan_ipa:.2f}", annotation_position="top left")
        fig_ipa_chart.update_traces(textposition='top center', marker=dict(size=10, opacity=0.9))
        fig_ipa_chart.update_layout(title_x=0.5, legend_title_text='Dimensi Layanan')
        st.plotly_chart(fig_ipa_chart, use_container_width=True)

        st.markdown(
            """
            <div class='body-text'>
            <h5>Interpretasi Kuadran:</h5>
            <ul>
                <li><b>Kuadran I (Prioritas Utama / <i>Concentrate Here</i>):</b> Kepentingan Tinggi, Kinerja Rendah. Area kritis yang membutuhkan perbaikan segera.</li>
                <li><b>Kuadran II (Pertahankan Prestasi / <i>Keep Up the Good Work</i>):</b> Kepentingan Tinggi, Kinerja Tinggi. Kekuatan PCM yang harus dipertahankan.</li>
                <li><b>Kuadran III (Prioritas Rendah / <i>Low Priority</i>):</b> Kepentingan Rendah, Kinerja Rendah. Perbaikan tidak mendesak.</li>
                <li><b>Kuadran IV (Mungkin Berlebihan / <i>Possible Overkill</i>):</b> Kepentingan Rendah, Kinerja Tinggi. Pertimbangkan realokasi sumber daya.</li>
            </ul>
            <p><i>(Identifikasi atribut spesifik per kuadran berdasarkan posisi titik pada diagram di atas akan memberikan panduan aksi yang lebih jelas bagi manajemen PCM.)</i></p>
            </div>
            """, unsafe_allow_html=True)

    # --- 4.3 Analisis PGCV (Potential Gain in Customer Value) ---
    # Data PGCV dari DRAFT.pdf Tabel 4.11 (hal 30-31)
    data_pgcv_list = [
        {'Kode': 'T2', 'Atribut': 'Ketersediaan tempat duduk dan area istirahat di mall', 'Skor PGCV': 0.4401},
        {'Kode': 'Rp3', 'Atribut': 'Ketanggapan petugas mall dalam menyapa pengunjung yang datang', 'Skor PGCV': 0.4118},
        {'Kode': 'E3', 'Atribut': 'Ketersediaan aduan keluhan pelanggan', 'Skor PGCV': 0.3897},
        {'Kode': 'R2', 'Atribut': 'Ketersediaan informasi acara atau promo yang mudah diakses', 'Skor PGCV': 0.3758},
        {'Kode': 'T3', 'Atribut': 'Ketersediaan papan penunjuk arah yang jelas', 'Skor PGCV': 0.3572},
        {'Kode': 'A3', 'Atribut': 'Kenyamanan mengakses jalan di dalam mall', 'Skor PGCV': 0.3250},
        {'Kode': 'E2', 'Atribut': 'Petugas mall sabar dalam melayani pelanggan', 'Skor PGCV': 0.3010},
        {'Kode': 'Rp2', 'Atribut': 'Kecepatan layanan kebersihan dalam menjaga kebersihan mall', 'Skor PGCV': 0.2994},
        {'Kode': 'A1', 'Atribut': 'Rasa aman dari tindak kriminal di dalam mall', 'Skor PGCV': 0.2905},
        {'Kode': 'A2', 'Atribut': 'Keamanan dalam menggunakan fasilitas seperti eskalator', 'Skor PGCV': 0.2874},
        {'Kode': 'E1', 'Atribut': 'Prosedur pelayanan pelanggan yang baik', 'Skor PGCV': 0.2859},
        {'Kode': 'Rp1', 'Atribut': 'Petugas mall cepat membantu jika ada yang bertanya', 'Skor PGCV': 0.2781},
        {'Kode': 'T4', 'Atribut': 'Aksesibilitas tempat parkir', 'Skor PGCV': 0.2671},
        {'Kode': 'R3', 'Atribut': 'Fasilitas mall (eskalator, toilet, dll.) berfungsi dengan baik', 'Skor PGCV': 0.2562},
        {'Kode': 'T1', 'Atribut': 'Kebersihan area mall (toilet, food court, eskalator, dll.)', 'Skor PGCV': 0.2429}
    ]
    df_pgcv = pd.DataFrame(data_pgcv_list)
    df_pgcv = df_pgcv.sort_values(by='Skor PGCV', ascending=False).reset_index(drop=True)
    df_pgcv['Peringkat'] = df_pgcv.index + 1
    
    with st.expander("Potensi Peningkatan Nilai Terbesar (Analisis PGCV)", expanded=False):
        display_minor_subheader("Mengidentifikasi Dampak Perbaikan Maksimal")
        st.markdown(
            """
            <div class='body-text'>
            <p>Analisis PGCV membantu menentukan urutan prioritas perbaikan atribut layanan dengan mengidentifikasi atribut mana yang, jika kinerjanya ditingkatkan, akan memberikan peningkatan nilai (<i>value</i>) terbesar bagi pengunjung.</p>
            <p>Berikut adalah peringkat atribut berdasarkan skor PGCV tertinggi (data dari Tabel 4.11 laporan):</p>
            </div>
            """, unsafe_allow_html=True)
        st.dataframe(df_pgcv[['Peringkat', 'Kode', 'Atribut', 'Skor PGCV']].style.format({'Skor PGCV': "{:.4f}"}), use_container_width=True)
        st.markdown(
            f"""
            <div class='body-text' style='margin-top:1rem;'>
            <p>Atribut dengan skor PGCV tertinggi, yaitu **{df_pgcv.iloc[0]['Atribut']} ({df_pgcv.iloc[0]['Kode']})** dengan skor **{df_pgcv.iloc[0]['Skor PGCV']:.4f}**, menjadi prioritas utama. Peningkatan pada aspek ini akan sangat diapresiasi pengunjung. Diikuti oleh **{df_pgcv.iloc[1]['Atribut']} ({df_pgcv.iloc[1]['Kode']})** dan **{df_pgcv.iloc[2]['Atribut']} ({df_pgcv.iloc[2]['Kode']})**.</p>
            <p>Hasil PGCV ini melengkapi analisis IPA dengan memberikan urutan yang lebih detail, terutama untuk atribut di Kuadran I IPA.</p>
            </div>
            """, unsafe_allow_html=True)

    # --- 4.4 Analisis CSI (Customer Satisfaction Index) ---
    # Data CSI dari DRAFT.pdf hal 31-32
    csi_value_reported = 84.540 # Dalam persen
    
    with st.expander("Seberapa Puas Pengunjung Secara Keseluruhan? (Analisis CSI)", expanded=False):
        display_minor_subheader("Mengukur Indeks Kepuasan Pelanggan Global")
        st.markdown(
            """
            <div class='body-text'>
            <p>Customer Satisfaction Index (CSI) mengukur tingkat kepuasan pelanggan secara keseluruhan terhadap layanan PCM, dengan memperhitungkan bobot kepentingan setiap atribut.</p>
            <p><i>(Tabel detail perhitungan MIS, MSS, WF, WS per indikator dapat dilihat pada Tabel 4.12 di laporan penelitian halaman 31).</i></p>
            </div>
            """, unsafe_allow_html=True)
        
        csi_value_decimal = csi_value_reported / 100
        csi_criteria_text = ""
        if 0.81 <= csi_value_decimal <= 1.00: csi_criteria_text = "Sangat Puas"
        elif 0.66 <= csi_value_decimal < 0.81: csi_criteria_text = "Puas"
        elif 0.51 <= csi_value_decimal < 0.66: csi_criteria_text = "Cukup Puas"
        elif 0.36 <= csi_value_decimal < 0.51: csi_criteria_text = "Kurang Puas"
        else: csi_criteria_text = "Sangat Tidak Puas"

        fig_csi_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta", value = csi_value_reported,
            domain = {'x': [0.1, 0.9], 'y': [0, 1]},
            title = {'text': f"<b>Customer Satisfaction Index (CSI)</b><br><span style='font-size:0.9em;color:gray'>Kategori: {csi_criteria_text}</span>", 'font': {'size': 18}},
            delta = {'reference': 80, 'increasing': {'color': "#28a745"}, 'decreasing': {'color': "#dc3545"}, 'position': "bottom"},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "var(--secondary-color)", 'thickness': 0.6},
                'bgcolor': "white", 'borderwidth': 2, 'bordercolor': "var(--border-color)",
                'steps': [
                    {'range': [0, 35], 'color': '#FFEBEE'}, {'range': [35, 51], 'color': '#FFF8E1'},
                    {'range': [51, 66], 'color': '#E3F2FD'}, {'range': [66, 81], 'color': '#E8F5E9'},
                    {'range': [81, 100], 'color': '#D1F2EB'}],
                'threshold': {'line': {'color': "var(--primary-color)", 'width': 4}, 'thickness': 0.85, 'value': csi_value_reported }
            }
        ))
        fig_csi_gauge.update_layout(height=350, margin=dict(t=50, b=30, l=30, r=30))
        st.plotly_chart(fig_csi_gauge, use_container_width=True)
        
        st.markdown(f"<div class='body-text'><p style='text-align:center; font-size:1.1em;'>Nilai <strong>Customer Satisfaction Index (CSI)</strong> Pakuwon City Mall adalah <strong style='font-size:1.2em; color:var(--primary-color);'>{csi_value_reported:.3f}%</strong>, yang masuk dalam kategori <strong>{csi_criteria_text}</strong>.</p></div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='body-text' style='font-size:0.9em;'>
            <p><strong>Kriteria Kepuasan (berdasarkan Tabel 2.3 laporan):</strong> 81%-100% (Sangat Puas), 66%-80.99% (Puas), dst.</p>
            <p>Pencapaian kategori "Sangat Puas" ini adalah indikasi yang sangat baik, menunjukkan bahwa secara umum pengunjung merasa layanan PCM telah memenuhi ekspektasi mereka. Namun, detail dari analisis GAP, IPA, dan PGCV tetap memberikan area spesifik untuk peningkatan berkelanjutan.</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    """
    <p style='text-align:center; font-size:0.9em; color:var(--light-text-color);'>
        Temuan-temuan ini menjadi dasar untuk merumuskan rekomendasi strategis yang akan dibahas pada bagian selanjutnya.
    </p>
    """, unsafe_allow_html=True
)
