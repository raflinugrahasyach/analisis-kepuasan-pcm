# Simpan file ini sebagai 02_📖_Memahami_Konteks_Riset.py
# di dalam folder `pages`

import streamlit as st

# --- Fungsi Bantuan (Menggunakan gaya global dari app.py) ---
def display_page_title(title, subtitle):
    st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)

def display_content_section(title, content_html, icon="", expanded_default=False):
    if icon:
        expander_label = f"{icon} {title}"
    else:
        expander_label = title
    
    with st.expander(expander_label, expanded=expanded_default):
        st.markdown(f"<div class='body-text'>{content_html}</div>", unsafe_allow_html=True)

# --- KONTEN HALAMAN (RINGKASAN BAB 1 - PENDAHULUAN) ---

display_page_title(
    "Memahami Konteks Riset Kepuasan Pengunjung",
    "Latar Belakang, Tujuan, dan Ruang Lingkup Penelitian untuk Pakuwon City Mall"
)

# --- 1.1 Latar Belakang (Diringkas) ---
latar_belakang_html = """
    <p>Industri ritel modern, khususnya pusat perbelanjaan, memiliki peran strategis dalam pertumbuhan ekonomi perkotaan. Surabaya, sebagai kota metropolitan, menunjukkan aktivitas konsumen yang tinggi di berbagai pusat perbelanjaan, termasuk Pakuwon City Mall (PCM) yang hadir sebagai <i>lifestyle mall</i> premium di Surabaya Timur sejak akhir 2020.</p>
    <p>Sebagai pemain yang relatif baru, PCM perlu terus beradaptasi dan meningkatkan kualitas layanan untuk memenuhi ekspektasi konsumen yang beragam. Kualitas layanan adalah faktor kunci yang mempengaruhi persepsi dan minat kunjungan ulang. Meskipun ada model seperti SERVQUAL, penelitian spesifik mengenai kepuasan pengunjung PCM masih terbatas, padahal tinjauan awal menunjukkan adanya area yang memerlukan perhatian.</p>
    <p>Oleh karena itu, penelitian ini bertujuan melakukan analisis komprehensif menggunakan metode SERVQUAL, IPA, PGCV, dan CSI untuk memberikan rekomendasi strategis kepada manajemen PCM dalam meningkatkan kualitas layanan.</p>
"""
display_content_section(
    "Mengapa Riset Ini Dilakukan? (Latar Belakang)",
    latar_belakang_html,
    icon="💡",
    expanded_default=True
)

# --- 1.2 Rumusan Masalah (Disajikan sebagai Pertanyaan Kunci) ---
rumusan_masalah_html = """
    <p>Penelitian ini berupaya menjawab pertanyaan-pertanyaan kunci berikut terkait Pakuwon City Mall:</p>
    <ol>
        <li>Bagaimana profil dan karakteristik pengunjung PCM?</li>
        <li>Sejauh mana kualitas layanan PCM saat ini telah memenuhi harapan pengunjung (analisis GAP SERVQUAL)?</li>
        <li>Aspek layanan mana yang menjadi prioritas utama untuk ditingkatkan berdasarkan tingkat kepentingan dan kinerja (analisis IPA)?</li>
        <li>Pada aspek layanan mana perbaikan akan memberikan peningkatan nilai terbesar bagi pengunjung (analisis PGCV)?</li>
        <li>Bagaimana tingkat kepuasan pengunjung PCM secara keseluruhan (analisis CSI)?</li>
    </ol>
"""
display_content_section(
    "Pertanyaan Kunci yang Dijawab Riset Ini (Rumusan Masalah)",
    rumusan_masalah_html,
    icon="❓"
)

# --- 1.3 Tujuan Penelitian (Disajikan sebagai Kontribusi Riset) ---
tujuan_penelitian_html = """
    <p>Sejalan dengan pertanyaan kunci di atas, tujuan utama dari penelitian ini adalah untuk:</p>
    <ul>
        <li>Memberikan gambaran detail mengenai <strong>profil pengunjung</strong> PCM.</li>
        <li>Menganalisis secara mendalam <strong>tingkat kesenjangan kualitas layanan</strong> yang dirasakan pengunjung.</li>
        <li>Mengidentifikasi dan memetakan <strong>area layanan yang menjadi prioritas</strong> untuk tindakan perbaikan dan pengembangan.</li>
        <li>Menentukan urutan prioritas perbaikan atribut layanan yang memberikan <strong>dampak nilai terbesar</strong>.</li>
        <li>Menyediakan ukuran kuantitatif yang komprehensif mengenai <strong>tingkat kepuasan pengunjung PCM secara keseluruhan</strong>.</li>
    </ul>
"""
display_content_section(
    "Kontribusi dan Tujuan Utama Riset (Tujuan Penelitian)",
    tujuan_penelitian_html,
    icon="🎯"
)

# --- 1.4 Manfaat Penelitian (Fokus pada Manfaat untuk PCM) ---
manfaat_penelitian_html = """
    <p>Hasil penelitian ini diharapkan memberikan manfaat signifikan, terutama bagi <strong>Manajemen Pakuwon City Mall</strong>, berupa:</p>
    <ul>
        <li><strong>Data Empiris Valid:</strong> Menyediakan dasar data yang kuat mengenai persepsi dan kepuasan pengunjung terhadap kualitas layanan saat ini.</li>
        <li><strong>Rekomendasi Strategis:</strong> Memberikan panduan konkret dan prioritas area perbaikan layanan yang dapat diimplementasikan untuk meningkatkan pengalaman pengunjung.</li>
        <li><strong>Dasar Pengambilan Keputusan:</strong> Membantu dalam alokasi sumber daya yang lebih efektif dan efisien untuk program peningkatan kualitas layanan dan fasilitas.</li>
        <li><strong>Peningkatan Daya Saing:</strong> Upaya peningkatan kepuasan pelanggan dapat berkontribusi pada peningkatan loyalitas dan daya saing PCM di industri ritel Surabaya.</li>
    </ul>
    <p>Selain itu, penelitian ini juga bermanfaat bagi akademisi sebagai referensi studi dan bagi penulis untuk pengembangan kompetensi riset.</p>
"""
display_content_section(
    "Manfaat Riset Ini untuk Pakuwon City Mall (Manfaat Penelitian)",
    manfaat_penelitian_html,
    icon="🌟"
)

# --- 1.5 Batasan Masalah (Ringkas) ---
batasan_masalah_html = """
    <p>Untuk menjaga fokus dan kedalaman analisis, penelitian ini memiliki beberapa batasan, diantaranya:</p>
    <ul>
        <li>Fokus pada pengunjung Pakuwon City Mall Surabaya.</li>
        <li>Pengambilan data dilakukan pada periode waktu tertentu di pintu keluar utama.</li>
        <li>Dimensi kualitas layanan mengacu pada kerangka SERVQUAL yang disesuaikan.</li>
    </ul>
"""
display_content_section(
    "Ruang Lingkup dan Batasan Studi (Batasan Masalah)",
    batasan_masalah_html,
    icon="🚧"
)

st.markdown("---")
st.markdown(
    """
    <p style='text-align:center; font-size:0.9em; color:var(--light-text-color);'>
        Pemahaman konteks ini menjadi dasar untuk menganalisis temuan kunci dari pengunjung.
    </p>
    """, unsafe_allow_html=True
)
