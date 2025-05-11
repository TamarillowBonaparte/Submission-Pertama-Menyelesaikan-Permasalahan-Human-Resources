# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
Submission Pertama: Menyelesaikan Permasalahan Human Resources Perusahan JAYA JAYA MAJU

Aplikasi ini dirancang untuk membantu perusahaan **Jaya Jaya Maju** dalam menganalisis dan memprediksi **attrition karyawan**. Dengan lebih dari 1000 karyawan yang tersebar di berbagai lokasi, perusahaan ini menghadapi tantangan besar dalam mengelola tingkat kepergian karyawan (attrition). Aplikasi ini memberikan wawasan berdasarkan data historis yang tersedia, serta memberikan prediksi dan rekomendasi tentang karyawan yang kemungkinan besar akan meninggalkan perusahaan.

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan. Walaupun perusahaan ini telah berkembang pesat, mereka mengalami kesulitan dalam mengelola sumber daya manusia, yang berimbas pada tingginya tingkat attrition di kalangan karyawan. Tingkat attrition yang tinggi lebih dari 10% per tahun menyebabkan perusahaan mengalami kerugian terkait biaya rekrutmen dan pelatihan serta gangguan dalam kelancaran operasional.

### Tantangan dalam Mempertahankan Karyawan
Tantangan utama yang dihadapi adalah mengidentifikasi faktor-faktor yang menyebabkan karyawan memilih untuk meninggalkan perusahaan. Beberapa faktor, seperti ketidakpuasan terhadap kompensasi, kurangnya kesempatan untuk berkembang, dan ketidaknyamanan dalam budaya perusahaan, sering menjadi penyebab utama.

### Dampak Attrition Terhadap Perusahaan
Tingkat attrition yang tinggi dapat berdampak negatif pada produktivitas, moral tim, dan biaya operasional. Hal ini juga dapat mempengaruhi citra perusahaan di pasar kerja, yang dapat memperburuk masalah dalam merekrut talenta baru.

### Permasalahan Bisnis

1. Menyusun strategi untuk mengurangi tingkat attrition yang tinggi.
2. Mengidentifikasi faktor-faktor yang paling berpengaruh terhadap keputusan karyawan untuk keluar.
3. Meningkatkan efisiensi dalam proses rekrutmen dan pelatihan.
4. Meningkatkan kesejahteraan dan kepuasan karyawan.
5. Memberikan rekomendasi berbasis data untuk perbaikan dalam kebijakan HR.

### Cakupan Proyek

1. Pengumpulan dan pembersihan data karyawan.
2. Analisis eksplorasi data untuk menemukan pola yang relevan.
3. Pengembangan model prediksi menggunakan teknik Random Forest.
4. Penyajian hasil analisis melalui dashboard interaktif.
5. Implementasi dan deployment aplikasi prediksi menggunakan Streamlit.

### Persiapan

Sumber data: Dataset employee_data.csv.

Tools: Python >3.10, Streamlit, scikit-learn, joblib, pandas, matplotlib.

Setup environment:
Instalasi environment:
```bash
pip install -r requirements.txt
```
atau secara manual:
```bash
pip install streamlit pandas scikit-learn joblib matplotlib seaborn
```
Menjalankan Aplikasi

Jalankan aplikasi Streamlit dengan:
```bash
streamlit run app.py
```
Aplikasi akan terbuka di browser default Anda di alamat
```
http://localhost:8501
```
## Business Dashboard

Visualisasi Data Attrition Karyawan - Jaya Jaya Maju
Proyek ini merupakan dashboard visualisasi data attrition (pengunduran diri karyawan) yang bertujuan membantu perusahaan memahami faktor-faktor yang memengaruhi tingkat keluar masuknya karyawan. Menggunakan Metabase sebagai visualisasi data, maka saya menyajikan dalam bentuk gambar, belum bisa di sajikan ke public karna bersifat lokal saat di jalankan metabase.

![Grafik Attrition](Moh%20Dani%20Kurniawan%20Sugiarto-Dashboard.jpg)

📌 Insight Utama:

Non-Attrition: 83.5%

Attrition: 16.5%

🔍 Analisis Berdasarkan:

Gender: Pria lebih banyak mengalami attrition dibanding wanita.

Departemen: Sales memiliki tingkat attrition tertinggi.

Pendidikan: Pendidikan menengah–tinggi memiliki retensi lebih baik.

Status Pernikahan: Karyawan single cenderung lebih sering resign.

Usia: Usia 31–36 tahun paling rentan terhadap attrition.

🛠 Tools & Visualisasi:

Donut Chart

Bar Chart

Sankey Diagram

🎯 Tujuan:
Membantu HR dalam mengidentifikasi kelompok berisiko tinggi untuk attrition dan menyusun strategi retensi yang lebih efektif.

## Conclusion

Model prediktif ini memberikan wawasan yang berharga tentang faktor-faktor yang mempengaruhi attrition karyawan dan membantu manajer HR dalam membuat keputusan yang lebih terinformasi. Dengan menggunakan aplikasi ini, Jaya Jaya Maju dapat menurunkan tingkat attrition dan meningkatkan kepuasan serta produktivitas karyawan.

### Rekomendasi Action Items (Optional)

- Input Data Karyawan: Pengguna diminta untuk memasukkan berbagai informasi tentang karyawan seperti usia, jenis kelamin, status pernikahan, pekerjaan, penghasilan bulanan, kepuasan pekerjaan, dan lainnya.

- Tab "Make Prediction": Setelah mengisi informasi, pengguna dapat menekan tombol "Predict Attrition" untuk memprediksi apakah karyawan tersebut berisiko tinggi untuk meninggalkan perusahaan.

- Tab "Model Information": Di sini, pengguna dapat melihat informasi mengenai model yang digunakan, metrik performa model (akurasi, presisi, recall, F1-score), serta pentingnya setiap fitur dalam model.

- Rekomendasi untuk Mengurangi Attrition: Setelah prediksi, aplikasi memberikan rekomendasi untuk mengurangi risiko attrition berdasarkan faktor-faktor yang mempengaruhi hasil prediksi.
