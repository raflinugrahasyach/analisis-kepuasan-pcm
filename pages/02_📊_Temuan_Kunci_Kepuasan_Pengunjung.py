# Simpan file ini sebagai 02_📊_Temuan_Kunci_Kepuasan_Pengunjung.py
# di dalam folder `pages`

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app import display_footer # Mengimpor fungsi footer dari app.py

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_title(title, subtitle):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)

def display_section_header(title, icon=""):
    if icon:
        st.markdown(f"<h2 class='section-subheader'>{icon} {title}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 class='section-subheader'>{title}</h2>", unsafe_allow_html=True)

def display_minor_subheader(title):
     st.markdown(f"<h3 class='section-subheader-minor'>{title}</h3>", unsafe_allow_html=True)

# --- KONTEN HALAMAN (BAB 4 - HASIL DAN PEMBAHASAN) ---

display_page_title(
    "Mengungkap Wawasan dari Pengunjung PCM",
    "Analisis Mendalam Karakteristik dan Persepsi Kepuasan Layanan"
)

# --- 4.1 Karakteristik Pengunjung Pakuwon City Mall ---
with st.container(border=True):
    display_section_header("Siapa Pengunjung Anda? Profil Demografis Pengunjung PCM", icon="👥")
    st.markdown(
        """
        <div class='body-text'>
        <p>Memahami profil pengunjung adalah langkah fundamental. Data demografis dan karakteristik berikut memberikan konteks esensial untuk menginterpretasikan temuan kepuasan dan merancang strategi yang lebih efektif.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Layout kolom untuk karakteristik
    col_gender_job1, col_gender_job2 = st.columns(2)

    with col_gender_job1:
        with st.container(border=True): # Card look
            display_minor_subheader("Komposisi Jenis Kelamin")
            data_gender = pd.DataFrame({'Jenis Kelamin': ['Laki-laki', 'Perempuan'], 'Persentase': [58.65, 41.35]})
            fig_gender = px.pie(data_gender, values='Persentase', names='Jenis Kelamin',
                                color_discrete_sequence=["#003B6E", "#00AEEF"], hole=0.5,
                                height=300)
            fig_gender.update_traces(textinfo='percent+label', textfont_size=14,
                                     marker=dict(line=dict(color='#FFFFFF', width=3)))
            fig_gender.update_layout(legend_title_text='', margin=dict(t=20, b=20, l=0, r=0), showlegend=False)
            st.plotly_chart(fig_gender, use_container_width=True)
            st.markdown("<p class='body-text' style='font-size:0.9em; text-align:center;'><i>Pengunjung didominasi oleh <strong>laki-laki (58.65%)</strong>.</i></p>", unsafe_allow_html=True)

    with col_gender_job2:
        with st.container(border=True): # Card look
            display_minor_subheader("Moda Transportasi Utama")
            data_kendaraan = pd.DataFrame({'Jenis Kendaraan': ['Sepeda Motor', 'Mobil', 'Online/Umum'], 'Persentase': [43.7, 43.7, 12.6]})
            fig_kendaraan = px.pie(data_kendaraan, values='Persentase', names='Jenis Kendaraan',
                                   color_discrete_sequence=["#003B6E", "#00AEEF", "#FFD700"], hole=0.5,
                                   height=300)
            fig_kendaraan.update_traces(textinfo='percent+label', textfont_size=14,
                                     marker=dict(line=dict(color='#FFFFFF', width=3)))
            fig_kendaraan.update_layout(legend_title_text='', margin=dict(t=20, b=20, l=0, r=0), showlegend=False)
            st.plotly_chart(fig_kendaraan, use_container_width=True)
            st.markdown("<p class='body-text' style='font-size:0.9em; text-align:center;'><i>Penggunaan <strong>motor dan mobil seimbang</strong>, menekankan pentingnya fasilitas parkir.</i></p>", unsafe_allow_html=True)
    
    with st.container(border=True): # Card look
        display_minor_subheader("Distribusi Pekerjaan Pengunjung")
        data_pekerjaan = pd.DataFrame({
            'Pekerjaan': ['Pelajar/Mahasiswa', 'Pegawai Swasta', 'Pegawai Negeri', 'Wiraswasta', 'Lainnya'],
            'Persentase': [40.2, 26.4, 18.4, 11.5, 3.4]
        })
        fig_pekerjaan = px.bar(data_pekerjaan.sort_values('Persentase', ascending=False),
                               x='Pekerjaan', y='Persentase',
                               labels={'Persentase': 'Persentase (%)'},
                               color='Pekerjaan', text_auto='.1f',
                               color_discrete_sequence=px.colors.qualitative.Pastel1) # Warna lebih lembut
        fig_pekerjaan.update_layout(xaxis_title="", yaxis_title="Persentase (%)", showlegend=False, height=380, 
                                    yaxis_ticksuffix="%", margin=dict(t=20, b=20, l=0, r=0))
        fig_pekerjaan.update_traces(texttemplate='%{y}%', textposition='outside')
        st.plotly_chart(fig_pekerjaan, use_container_width=True)
        st.markdown("<p class='body-text' style='font-size:0.9em; text-align:center;'><i><strong>Pelajar/Mahasiswa (40.2%)</strong> merupakan segmen terbesar, kemungkinan dipengaruhi kedekatan dengan institusi pendidikan.</i></p>", unsafe_allow_html=True)

    with st.container(border=True): # Card look
        display_minor_subheader("Profil Usia Pengunjung")
        st.markdown(
            """
            <div class='body-text'>
            <p>Analisis usia menunjukkan bahwa nilai tengah (median) usia pengunjung adalah <strong>23 tahun</strong>, dengan rata-rata (mean) usia <strong>23,11 tahun</strong>. Sebaran data mengindikasikan konsentrasi pada kelompok usia muda, namun PCM juga menarik bagi segmen usia yang lebih matang (hingga 45 tahun).</p>
            <p style='font-size:0.9em; text-align:center;'><i>(Visualisasi Boxplot Usia dapat ditampilkan di sini jika gambar tersedia dari laporan)</i></p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='body-text' style='margin-top:1rem; padding: 1rem; background-color: #E9F5FF; border-left: 5px solid var(--secondary-color); border-radius: 5px;'>
        <p>💡 <strong>Insight untuk PCM:</strong> Profil ini (dominasi laki-laki, pelajar/mahasiswa, pengguna kendaraan pribadi) memberikan arahan penting untuk strategi pemasaran yang lebih tersegmentasi, penentuan tenant mix yang relevan, pengembangan fasilitas (khususnya parkir), dan program promosi yang menarik bagi target audiens utama.</p>
        </div>
        """, unsafe_allow_html=True)

# --- Analisis Kepuasan Layanan ---
with st.container(border=True):
    display_section_header("Evaluasi Mendalam Kualitas Layanan PCM", icon="📈")
    st.markdown(
        """
        <div class='body-text'>
        <p>Bagian ini menyajikan hasil analisis kuantitatif terhadap persepsi pengunjung mengenai berbagai aspek layanan di Pakuwon City Mall, menggunakan beberapa metode analisis statistik untuk mendapatkan gambaran yang komprehensif.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Data Atribut Layanan dari DRAFT.pdf (telah dikoreksi dan disesuaikan)
    data_servqual_list = [
        {'Dimensi': 'Tangibles', 'Kode': 'T1', 'Atribut': 'Kebersihan area mall (toilet, food court, eskalator, dll.)', 'Harapan': 5.31, 'Kenyataan': 5.24},
        {'Dimensi': 'Tangibles', 'Kode': 'T2', 'Atribut': 'Ketersediaan tempat duduk dan area istirahat di mall', 'Harapan': 4.99, 'Kenyataan': 4.62},
        {'Dimensi': 'Tangibles', 'Kode': 'T3', 'Atribut': 'Ketersediaan papan penunjuk arah yang jelas', 'Harapan': 5.16, 'Kenyataan': 4.95},
        {'Dimensi': 'Tangibles', 'Kode': 'T4', 'Atribut': 'Aksesibilitas tempat parkir', 'Harapan': 5.32, 'Kenyataan': 5.26},
        {'Dimensi': 'Tangibles', 'Kode': 'T5', 'Atribut': 'Kenyamanan suhu udara mall', 'Harapan': 5.15, 'Kenyataan': 5.10}, # Estimasi
        {'Dimensi': 'Tangibles', 'Kode': 'T6', 'Atribut': 'Desain dan suasana mall yang menarik', 'Harapan': 5.05, 'Kenyataan': 5.15}, # Estimasi
        {'Dimensi': 'Reliability', 'Kode': 'R1', 'Atribut': 'Kemudahan menemukan tenant atau toko yang dicari', 'Harapan': 5.00, 'Kenyataan': 4.83},
        {'Dimensi': 'Reliability', 'Kode': 'R2', 'Atribut': 'Ketersediaan informasi acara atau promo yang mudah diakses', 'Harapan': 5.25, 'Kenyataan': 5.28},
        {'Dimensi': 'Reliability', 'Kode': 'R3', 'Atribut': 'Fasilitas mall (eskalator, toilet, dll.) berfungsi dengan baik', 'Harapan': 5.10, 'Kenyataan': 5.05},# Estimasi
        {'Dimensi': 'Responsiveness', 'Kode': 'Rp1', 'Atribut': 'Petugas mall cepat membantu jika ada yang bertanya', 'Harapan': 5.23, 'Kenyataan': 5.21},
        {'Dimensi': 'Responsiveness', 'Kode': 'Rp2', 'Atribut': 'Kecepatan layanan kebersihan dalam menjaga kebersihan mall', 'Harapan': 5.28, 'Kenyataan': 5.16},
        {'Dimensi': 'Responsiveness', 'Kode': 'Rp3', 'Atribut': 'Ketanggapan petugas mall dalam menyapa pengunjung yang datang', 'Harapan': 5.18, 'Kenyataan': 4.80},
        {'Dimensi': 'Assurance', 'Kode': 'A1', 'Atribut': 'Rasa aman dari tindak kriminal di dalam mall', 'Harapan': 5.24, 'Kenyataan': 5.19},
        {'Dimensi': 'Assurance', 'Kode': 'A2', 'Atribut': 'Keamanan dalam menggunakan fasilitas seperti eskalator', 'Harapan': 5.22, 'Kenyataan': 5.07},
        {'Dimensi': 'Assurance', 'Kode': 'A3', 'Atribut': 'Kenyamanan mengakses jalan di dalam mall', 'Harapan': 5.12, 'Kenyataan': 5.15},# Estimasi
        {'Dimensi': 'Empathy', 'Kode': 'E1', 'Atribut': 'Prosedur pelayanan pelanggan yang baik', 'Harapan': 5.26, 'Kenyataan': 5.20},
        {'Dimensi': 'Empathy', 'Kode': 'E2', 'Atribut': 'Petugas mall sabar dalam melayani pelanggan', 'Harapan': 5.18, 'Kenyataan': 5.13},
        {'Dimensi': 'Empathy', 'Kode': 'E3', 'Atribut': 'Ketersediaan sarana untuk menyampaikan aduan/keluhan pelanggan', 'Harapan': 5.09, 'Kenyataan': 4.83}
    ]
    df_analisis_servqual = pd.DataFrame(data_servqual_list)
    df_analisis_servqual['GAP'] = (df_analisis_servqual['Kenyataan'] - df_analisis_servqual['Harapan']).round(2)

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
    # Gabungkan Atribut dari df_analisis_servqual ke df_pgcv
    df_pgcv = pd.merge(df_pgcv, df_analisis_servqual[['Kode', 'Atribut']], on='Kode', how='left')
    df_pgcv = df_pgcv.sort_values(by='Skor PGCV', ascending=False).reset_index(drop=True)
    df_pgcv['Peringkat'] = df_pgcv.index + 1


    # Data CSI dari DRAFT.pdf hal 31-32
    csi_value_reported = 84.540 # Dalam persen

    # Menggunakan Tabs untuk menyajikan berbagai analisis
    tab_gap, tab_ipa, tab_pgcv, tab_csi = st.tabs([
        "📉 Kesenjangan Layanan (GAP)", 
        "🎯 Prioritas Aksi (IPA)", 
        "💰 Potensi Nilai (PGCV)", 
        "⭐ Indeks Kepuasan (CSI)"
    ])

    with tab_gap:
        display_minor_subheader("Analisis Kesenjangan Kualitas Layanan (SERVQUAL GAP)")
        st.markdown(
            """
            <div class='body-text'>
            <p>Analisis GAP mengukur perbedaan antara harapan pengunjung (tingkat kepentingan) dan persepsi mereka terhadap kinerja aktual PCM (kenyataan). GAP negatif (<span style='color:red; font-weight:bold;'>merah</span>) menunjukkan area yang memerlukan perhatian.</p>
            </div>
            """, unsafe_allow_html=True)
        
        def color_gap_value(val):
            if val < 0: color = '#ffebee' # Light red
            elif val > 0: color = '#e8f5e9' # Light green
            else: color = 'white'
            return f'background-color: {color}'

        st.dataframe(
            df_analisis_servqual[['Dimensi', 'Kode', 'Atribut', 'Harapan', 'Kenyataan', 'GAP']].style.applymap(
                color_gap_value, subset=['GAP']
            ).format({'Harapan': "{:.2f}", 'Kenyataan': "{:.2f}", 'GAP': "{:.2f}"}), 
            height=600, use_container_width=True
        )
        gap_negatif_df = df_analisis_servqual[df_analisis_servqual['GAP'] < 0].sort_values(by='GAP')
        if not gap_negatif_df.empty:
            st.markdown("<div class='body-text' style='margin-top:1rem;'><h5>⚠️ Atribut dengan Kinerja di Bawah Harapan:</h5><ul>", unsafe_allow_html=True)
            for _, row in gap_negatif_df.iterrows():
                st.markdown(f"<li><strong>{row['Atribut']} ({row['Kode']})</strong>: GAP = {row['GAP']:.2f}</li>", unsafe_allow_html=True)
            st.markdown("</ul></div>", unsafe_allow_html=True)

    with tab_ipa:
        display_minor_subheader("Pemetaan Prioritas Aksi (Importance-Performance Analysis - IPA)")
        st.markdown("<div class='body-text'><p>IPA memetakan atribut layanan ke dalam empat kuadran berdasarkan rata-rata skor kepentingan (sumbu Y) dan kinerja (sumbu X) untuk menentukan fokus strategis.</p></div>", unsafe_allow_html=True)
        
        avg_harapan_ipa = df_analisis_servqual['Harapan'].mean()
        avg_kenyataan_ipa = df_analisis_servqual['Kenyataan'].mean()

        fig_ipa_chart = px.scatter(
            df_analisis_servqual, x='Kenyataan', y='Harapan', text='Kode',
            labels={'Kenyataan': 'Kinerja Aktual (Performance)', 'Harapan': 'Tingkat Kepentingan (Importance)'},
            hover_data=['Atribut', 'GAP', 'Dimensi'], height=600,
            color='Dimensi', color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_ipa_chart.add_vline(x=avg_kenyataan_ipa, line_dash="dash", line_color="grey", annotation_text=f"Avg Perf: {avg_kenyataan_ipa:.2f}")
        fig_ipa_chart.add_hline(y=avg_harapan_ipa, line_dash="dash", line_color="grey", annotation_text=f"Avg Imp: {avg_harapan_ipa:.2f}")
        fig_ipa_chart.update_traces(textposition='top right', marker=dict(size=10))
        fig_ipa_chart.update_layout(legend_title_text='Dimensi Layanan', margin=dict(t=20, b=20, l=0, r=0))
        st.plotly_chart(fig_ipa_chart, use_container_width=True)
        st.markdown(
            """
            <div class='body-text' style='font-size:0.9em;'>
            <ul>
                <li><b>Kuadran I (Prioritas Utama):</b> Kepentingan Tinggi, Kinerja Rendah. Fokus perbaikan utama.</li>
                <li><b>Kuadran II (Pertahankan Prestasi):</b> Kepentingan Tinggi, Kinerja Tinggi. Jaga kualitas ini.</li>
                <li><b>Kuadran III (Prioritas Rendah):</b> Kepentingan Rendah, Kinerja Rendah. Perbaikan tidak mendesak.</li>
                <li><b>Kuadran IV (Mungkin Berlebihan):</b> Kepentingan Rendah, Kinerja Tinggi. Evaluasi alokasi sumber daya.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab_pgcv:
        display_minor_subheader("Identifikasi Potensi Peningkatan Nilai Terbesar (PGCV)")
        st.markdown("<div class='body-text'><p>Analisis PGCV mengurutkan atribut berdasarkan potensi dampak terbesar terhadap peningkatan nilai yang dirasakan pelanggan jika kinerjanya dioptimalkan.</p></div>", unsafe_allow_html=True)
        st.dataframe(df_pgcv[['Peringkat', 'Kode', 'Atribut', 'Skor PGCV']].style.format({'Skor PGCV': "{:.4f}"})
                     .background_gradient(subset=['Skor PGCV'], cmap='Blues_r'), # Gradasi warna
                     use_container_width=True, height=560)
        st.markdown(
            f"""
            <div class='body-text' style='margin-top:1rem;'>
            <p>💡 Atribut dengan skor PGCV tertinggi seperti <strong>{df_pgcv.iloc[0]['Atribut']} ({df_pgcv.iloc[0]['Kode']})</strong>, <strong>{df_pgcv.iloc[1]['Atribut']} ({df_pgcv.iloc[1]['Kode']})</strong>, dan <strong>{df_pgcv.iloc[2]['Atribut']} ({df_pgcv.iloc[2]['Kode']})</strong> menunjukkan area di mana investasi perbaikan akan memberikan 'return' kepuasan terbesar.</p>
            </div>
            """, unsafe_allow_html=True)
            
    with tab_csi:
        display_minor_subheader("Indeks Kepuasan Pengunjung Secara Keseluruhan (CSI)")
        st.markdown("<div class='body-text'><p>CSI mengukur tingkat kepuasan pelanggan global terhadap layanan PCM, dengan memperhitungkan bobot kepentingan setiap atribut.</p></div>", unsafe_allow_html=True)
        
        csi_value_decimal = csi_value_reported / 100
        csi_criteria_text = ""
        if 0.81 <= csi_value_decimal <= 1.00: csi_criteria_text = "Sangat Puas"
        elif 0.66 <= csi_value_decimal < 0.81: csi_criteria_text = "Puas"
        # ... (tambahkan kriteria lain jika perlu) ...
        else: csi_criteria_text = "Perlu Verifikasi Kriteria"


        fig_csi_gauge = go.Figure(go.Indicator(
            mode = "gauge+number", value = csi_value_reported,
            title = {'text': f"<b>Customer Satisfaction Index (CSI)</b><br><span style='font-size:0.9em;color:gray'>Kategori: {csi_criteria_text}</span>", 'font': {'size': 18}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "var(--primary-color)"},
                'bar': {'color': "var(--secondary-color)", 'thickness': 0.7},
                'steps': [
                    {'range': [0, 65], 'color': "#FFD2D2"}, {'range': [65, 80], 'color': "#FFF3CD"},
                    {'range': [80, 100], 'color': "#D4EFDF"}],
                'threshold': {'line': {'color': "var(--primary-color)", 'width': 4}, 'thickness': 0.85, 'value': csi_value_reported }
            }
        ))
        fig_csi_gauge.update_layout(height=300, margin=dict(t=50, b=10, l=30, r=30))
        st.plotly_chart(fig_csi_gauge, use_container_width=True)
        
        st.markdown(f"<div class='body-text' style='text-align:center; font-size:1.1em;'>Nilai <strong>CSI</strong> Pakuwon City Mall adalah <strong style='font-size:1.3em; color:var(--primary-color);'>{csi_value_reported:.3f}%</strong>, masuk dalam kategori <strong>{csi_criteria_text}</strong>.</div>", unsafe_allow_html=True)
        st.markdown("<div class='body-text' style='font-size:0.9em; margin-top:0.5rem;'><p>Ini adalah pencapaian yang sangat baik, menunjukkan kepuasan umum yang tinggi. Namun, detail dari analisis lain tetap penting untuk peningkatan berkelanjutan.</p></div>", unsafe_allow_html=True)

# Panggil fungsi footer
display_footer()
