# 📸 PENGOLAHAN CITRA DIGITAL

## 👩‍🎓 Identitas Mahasiswa

| Keterangan | Isi |
|------------|------|
| 👤 Nama | **Nadhia Shafira** |
| 🆔 NIM | **312410498** |
| 🏫 Kelas | **I241E** |
| 📚 Mata Kuliah | **Pengolahan Citra** |
| 👨‍🏫 Dosen Pengampu | **Dr. Muhamad Fatchan, S.Kom., M.Kom.** |

---

# 📖 RESUME JURNAL
## 🚗 License Plate Recognition System Menggunakan OpenCV dan OCR

### 🎯 Tujuan Penelitian
Penelitian ini bertujuan untuk mengembangkan sistem yang mampu mendeteksi dan mengenali nomor kendaraan secara otomatis menggunakan teknik pengolahan citra digital dan Optical Character Recognition (OCR).

---

### 📚 Latar Belakang
🚘 Pertumbuhan jumlah kendaraan yang semakin meningkat menyebabkan kebutuhan akan sistem identifikasi kendaraan yang cepat dan otomatis.

📸 Pengolahan citra digital memungkinkan komputer mendeteksi objek tertentu pada gambar, termasuk plat nomor kendaraan.

🔍 Teknologi OCR digunakan untuk membaca karakter yang terdapat pada plat nomor sehingga informasi kendaraan dapat diperoleh secara otomatis.

---

### ⚙️ Metode yang Digunakan

#### 🖼️ Akuisisi Citra
Gambar kendaraan diambil menggunakan kamera digital sebagai data masukan sistem.

#### ⚫ Konversi Grayscale
Gambar berwarna diubah menjadi grayscale untuk menyederhanakan proses pengolahan citra.

#### 🌫️ Gaussian Blur
Dilakukan proses penghalusan citra untuk mengurangi noise yang dapat mengganggu proses deteksi.

#### ✨ Edge Detection
Metode Canny Edge Detection digunakan untuk menemukan tepi objek pada gambar.

#### 🔲 Deteksi Kontur
Sistem mencari area berbentuk persegi panjang yang diduga sebagai lokasi plat nomor kendaraan.

#### 🔤 OCR (Optical Character Recognition)
Karakter pada plat nomor dibaca menggunakan Tesseract OCR sehingga menghasilkan teks berupa nomor kendaraan.

---

### 💡 Hasil Penelitian

✅ Sistem mampu mendeteksi area plat nomor kendaraan dengan baik.

✅ OCR berhasil membaca karakter pada plat nomor secara otomatis.

✅ Kombinasi OpenCV dan Tesseract OCR dapat digunakan sebagai solusi sederhana untuk sistem pengenalan plat nomor kendaraan.

---

### 📝 Kesimpulan

🎯 Pengolahan citra digital dapat dimanfaatkan untuk mendeteksi plat nomor kendaraan secara otomatis.

🚗 OpenCV berperan dalam proses deteksi objek plat nomor.

🔤 Tesseract OCR digunakan untuk mengenali karakter yang terdapat pada plat nomor.

📈 Sistem mampu memberikan hasil yang cukup baik untuk citra dengan kualitas yang jelas.

---

# 🚗 PRAKTIKUM 1
# DETEKSI DAN PENGENALAN PLAT NOMOR KENDARAAN

## 🎯 Tujuan Praktikum

📸 Mendeteksi lokasi plat nomor kendaraan menggunakan OpenCV.

🔤 Membaca nomor kendaraan menggunakan teknologi OCR (Optical Character Recognition).

🚗 Menghasilkan informasi nomor kendaraan secara otomatis dari sebuah gambar.

---

## 🛠️ Library yang Digunakan

- 🐍 OpenCV
- 🔤 Pytesseract
- 📊 Matplotlib

---

## ⚙️ Langkah Kerja

### 1️⃣ Membaca Gambar

📸 Program membaca gambar kendaraan yang akan diproses.

### 2️⃣ Konversi Grayscale

⚫ Gambar berwarna diubah menjadi grayscale agar proses pengolahan lebih sederhana.

### 3️⃣ Gaussian Blur

🌫️ Mengurangi noise pada citra sehingga proses deteksi menjadi lebih optimal.

### 4️⃣ Canny Edge Detection

✨ Mendeteksi tepi objek yang terdapat pada gambar.

### 5️⃣ Deteksi Kontur

🔲 Program mencari area berbentuk persegi panjang yang diduga sebagai plat nomor.

### 6️⃣ OCR

🔤 Tesseract OCR membaca karakter yang terdapat pada plat nomor kendaraan.

---

## 📸 Hasil Praktikum

### 🚗 Hasil Deteksi Plat Nomor

![Deteksi Plat Nomor](https://github.com/NadhiaShafira/pedestrian-detection/blob/c14b20fa6f1d1b57919f5d85333cad92d4eb2411/plate_results/deteksi_plat_nomor.png)

📌 Sistem berhasil mendeteksi lokasi plat nomor kendaraan.

📌 Plat nomor diberikan kotak hijau sebagai penanda area yang terdeteksi.

📌 OCR berhasil membaca karakter pada plat nomor kendaraan.

---

## 📝 Kesimpulan Praktikum

✅ OpenCV berhasil mendeteksi area plat nomor kendaraan.

✅ OCR berhasil mengenali karakter pada plat nomor.

✅ Sistem dapat digunakan sebagai dasar pengembangan Automatic Number Plate Recognition (ANPR).

---

# 🚶 PRAKTIKUM 2
# DETEKSI PEJALAN KAKI MENGGUNAKAN HOG DESCRIPTOR

## 🎯 Tujuan Praktikum

🚶 Mendeteksi keberadaan manusia pada gambar dan video menggunakan HOG Descriptor.

📸 Memahami implementasi Computer Vision menggunakan OpenCV.

🧠 Mengenal metode Human Detection berbasis Machine Learning bawaan OpenCV.

---

## 🛠️ Library yang Digunakan

- 🐍 OpenCV
- ⚡ Imutils

---

# 📸 DETEKSI PEJALAN KAKI PADA GAMBAR

## ⚙️ Langkah Kerja

### 1️⃣ Membaca Gambar

📸 Program membaca gambar yang berisi objek manusia.

### 2️⃣ Inisialisasi HOG Descriptor

🧠 HOG (Histogram of Oriented Gradients) digunakan untuk mendeteksi bentuk tubuh manusia.

### 3️⃣ Deteksi Manusia

🚶 Program melakukan pencarian objek manusia pada gambar.

### 4️⃣ Menampilkan Hasil

🔲 Setiap manusia yang berhasil terdeteksi diberikan kotak merah.

---

## 📸 Hasil Deteksi Gambar

![Deteksi Pejalan Kaki Pada Gambar](https://github.com/NadhiaShafira/pedestrian-detection/blob/7e6aac3b2d1dea6f9047153d265073cec6179464/hasil/Hasil%20Deteksi%20Gambar.png)

📌 Sistem berhasil mendeteksi objek manusia pada gambar.

📌 Kotak merah menunjukkan area manusia yang berhasil dikenali.

📌 Metode HOG mampu bekerja dengan baik pada gambar yang memiliki pencahayaan cukup.

---

# 🎥 DETEKSI PEJALAN KAKI PADA VIDEO

## ⚙️ Langkah Kerja

### 1️⃣ Membaca Video

🎥 Program membaca video frame demi frame.

### 2️⃣ HOG Descriptor

🧠 HOG digunakan untuk mendeteksi manusia pada setiap frame video.

### 3️⃣ Human Detection

🚶 Setiap manusia yang terdeteksi akan diberikan kotak merah.

### 4️⃣ Menampilkan Hasil

📺 Hasil deteksi ditampilkan secara realtime selama video berjalan.

---

## 📸 Hasil Deteksi Video

![Deteksi Pejalan Kaki Pada Video](screenshots/deteksi_video.png)

📌 Sistem berhasil mendeteksi manusia pada video.

📌 Kotak merah mengikuti objek manusia yang terdeteksi.

📌 Deteksi dilakukan secara realtime pada setiap frame video.

---

# 📋 KESIMPULAN AKHIR

✅ OpenCV dapat digunakan untuk mendeteksi berbagai objek pada citra digital.

✅ OCR mampu membaca karakter pada plat nomor kendaraan secara otomatis.

✅ HOG Descriptor efektif digunakan untuk mendeteksi manusia pada gambar maupun video.

✅ Pengolahan citra digital memiliki banyak penerapan dalam bidang keamanan, transportasi, dan sistem otomatisasi.

---

# 🙏 TERIMA KASIH

✨ Praktikum ini memberikan pemahaman mengenai implementasi Computer Vision menggunakan OpenCV untuk deteksi objek dan pengenalan karakter secara otomatis.
