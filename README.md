# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
Submission Pertama: Menyelesaikan Permasalahan Human Resources Perusahan JAYA JAYA MAJU

Aplikasi ini dirancang untuk membantu perusahaan **Jaya Jaya Maju** dalam menganalisis dan memprediksi **attrition karyawan**. Dengan lebih dari 1000 karyawan yang tersebar di berbagai lokasi, perusahaan ini menghadapi tantangan besar dalam mengelola tingkat kepergian karyawan (attrition). Aplikasi ini memberikan wawasan berdasarkan data historis yang tersedia, serta memberikan prediksi dan rekomendasi tentang karyawan yang kemungkinan besar akan meninggalkan perusahaan. Sumber data [employee data](https://drive.google.com/file/d/115xCHo1GhWoz1x6xdFdHOVLSrU_9qIL0/view?usp=sharing)

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan. Walaupun perusahaan ini telah berkembang pesat, mereka mengalami kesulitan dalam mengelola sumber daya manusia, yang berimbas pada tingginya tingkat attrition di kalangan karyawan. Tingkat attrition yang tinggi lebih dari 10% per tahun menyebabkan perusahaan mengalami kerugian terkait biaya rekrutmen dan pelatihan serta gangguan dalam kelancaran operasional.

### Tantangan dalam Mempertahankan Karyawan
Tantangan utama yang dihadapi adalah mengidentifikasi faktor-faktor yang menyebabkan karyawan memilih untuk meninggalkan perusahaan. Beberapa faktor, seperti ketidakpuasan terhadap kompensasi, kurangnya kesempatan untuk berkembang, dan ketidaknyamanan dalam budaya perusahaan, sering menjadi penyebab utama.

### Dampak Attrition Terhadap Perusahaan
Tingkat attrition yang tinggi dapat berdampak negatif pada produktivitas, moral tim, dan biaya operasional. Hal ini juga dapat mempengaruhi citra perusahaan di pasar kerja, yang dapat memperburuk masalah dalam merekrut talenta baru.

### Permasalahan Bisnis

Perusahaan Jaya Jaya Maju saat ini menghadapi tingkat attrition (pengunduran diri karyawan) yang sangat tinggi. Dari analisis data employee_data.csv, terlihat bahwa dari 1470 karyawan, terdapat 412 kasus attrition (28%), yang menunjukkan hampir sepertiga karyawan memilih untuk mengundurkan diri. Tingginya tingkat attrition ini menimbulkan beberapa dampak signifikan:

- Peningkatan Biaya Operasional: Setiap kali karyawan mengundurkan diri, perusahaan harus mengeluarkan biaya tambahan untuk rekrutmen, wawancara, hingga pelatihan karyawan baru. Dari visualisasi data terlihat bahwa sebagian besar yang mengundurkan diri berasal dari departemen Research & Development, yang umumnya membutuhkan keterampilan khusus dan waktu adaptasi lebih panjang.

- Penurunan Kualitas Layanan Pendidikan: Dalam bisnis edutech, kualitas pengajar dan staf pendukung sangat memengaruhi hasil belajar. Dengan tingkat pergantian karyawan yang tinggi, terutama di kalangan karyawan bergelar Bachelor yang mendominasi attrition (seperti terlihat pada histogram pendidikan), konsistensi layanan pembelajaran menjadi terganggu.
Hambatan Pengembangan Bisnis Jangka Panjang: Data menunjukkan bahwa kelompok Milenial dan karyawan dengan status Single adalah yang paling banyak keluar. Kelompok demografis ini sering kali membawa energi dan ide-ide inovatif yang sangat dibutuhkan untuk pengembangan produk edutech. Kehilangan mereka secara terus-menerus dapat menghambat inovasi dan daya saing perusahaan.

- Masalah Retensi Talenta Strategis: Hasil analisis menunjukkan karyawan dengan jarak tempuh menengah (Intermediate_distance) memiliki tingkat attrition tinggi. Ini mengindikasikan adanya masalah work-life balance, khususnya bagi karyawan yang menghabiskan waktu signifikan untuk perjalanan ke tempat kerja namun tidak cukup dekat untuk kemudahan akses atau cukup jauh untuk kebijakan kerja jarak jauh.

- Ketidakefektifan Kebijakan SDM: Model Random Forest yang dikembangkan dalam analisis mengidentifikasi ketidaksesuaian antara kebijakan SDM saat ini dengan kebutuhan karyawan, terutama dalam hal promosi, pengembangan karir, dan kebijakan jam kerja, yang mungkin menjadi pendorong utama keputusan untuk keluar.

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

Berdasarkan analisis data dan model Random Forest yang telah dikembangkan dengan akurasi 90%, beberapa karakteristik umum dari pegawai yang cenderung melakukan attrition telah teridentifikasi:

- Demografis: Karyawan dari generasi Milenial (usia 28-42 tahun) memiliki tingkat attrition tertinggi, diikuti oleh Gen Z (18-27 tahun). Mayoritas yang mengundurkan diri adalah karyawan berstatus Single, menunjukkan bahwa pegawai tanpa tanggung jawab keluarga lebih mungkin mencari peluang di tempat lain.

- Pendidikan dan Departemen: Lulusan dengan gelar Bachelor mendominasi kelompok yang keluar, dengan konsentrasi tinggi pada departemen Research & Development. Hal ini mengindikasikan adanya ketidaksesuaian antara ekspektasi karir profesional dengan realitas yang ditawarkan perusahaan untuk posisi yang membutuhkan keahlian teknis tinggi.

- Faktor Geografis: Pegawai dengan kategori jarak tempuh Intermediate_distance (6-25 km) menunjukkan kecenderungan attrition yang lebih tinggi. Jarak ini cukup jauh untuk menyebabkan kelelahan perjalanan namun tidak cukup jauh untuk mendapatkan fleksibilitas kerja jarak jauh, menciptakan situasi "zona abu-abu" yang tidak menguntungkan.

- Gender: Data menunjukkan bahwa karyawan laki-laki memiliki tingkat pengunduran diri yang lebih tinggi dibandingkan karyawan perempuan, yang mungkin berkaitan dengan perbedaan dalam prioritas karir dan kecenderungan mengambil risiko.

- Pola Karir: Meskipun tidak disebutkan secara langsung dalam visualisasi, model Random Forest mengidentifikasi variabel seperti JobLevel dan YearsWithCurrManager sebagai prediktor penting, menunjukkan bahwa stagnasi karir dan hubungan dengan manajemen merupakan faktor signifikan dalam keputusan untuk keluar.

Model prediktif ini memberikan departemen HR kemampuan untuk mengidentifikasi karyawan dengan risiko attrition tinggi berdasarkan karakteristik di atas. Dengan memahami profil karyawan yang cenderung keluar, HR dapat mengembangkan program retensi yang ditargetkan seperti:

- Program mentoring khusus untuk karyawan Milenial dan Gen Z
- Evaluasi ulang jalur karir dan sistem promosi untuk lulusan Bachelor di departemen R&D
- Kebijakan kerja fleksibel atau tunjangan transportasi untuk karyawan dengan jarak tempuh menengah
- Program pengembangan profesional yang lebih terstruktur untuk mencegah stagnasi karir

Implementasi strategi berbasis data ini diproyeksikan dapat menurunkan tingkat attrition secara signifikan, mengurangi biaya rekrutmen dan pelatihan, serta meningkatkan stabilitas dan produktivitas di seluruh departemen, terutama di Research & Development yang merupakan area kritis untuk inovasi dan pertumbuhan perusahaan.

### Rekomendasi Action Items (Optional)

- Input Data Karyawan: Pengguna diminta untuk memasukkan berbagai informasi tentang karyawan seperti usia, jenis kelamin, status pernikahan, pekerjaan, penghasilan bulanan, kepuasan pekerjaan, dan lainnya.

- Tab "Make Prediction": Setelah mengisi informasi, pengguna dapat menekan tombol "Predict Attrition" untuk memprediksi apakah karyawan tersebut berisiko tinggi untuk meninggalkan perusahaan.

- Tab "Model Information": Di sini, pengguna dapat melihat informasi mengenai model yang digunakan, metrik performa model (akurasi, presisi, recall, F1-score), serta pentingnya setiap fitur dalam model.

- Rekomendasi untuk Mengurangi Attrition: Setelah prediksi, aplikasi memberikan rekomendasi untuk mengurangi risiko attrition berdasarkan faktor-faktor yang mempengaruhi hasil prediksi.
