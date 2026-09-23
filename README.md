# Sistem Top Up Game Online (OOP Python)

Program CLI sederhana berbasis Object-Oriented Programming (OOP) dalam bahasa pemrograman Python untuk mengelola data game, item top-up, akun pengguna, dan transaksi pada sistem toko digital.

---

## Fitur Utama

- Management Data (CRUD Basic): Pembuatan instansiasi (Create), menampilkan data (Read), dan penghapusan objek (Delete).
- Enkapsulasi dan Proteksi Data: Menggunakan atribut private (__status, __jumlah_item, __password, __total_harga) yang dikelola secara aman melalui @property (Getter) dan Setter.
- Validasi Data: Setter dan metode kelas dilengkapi dengan pengujian kondisi untuk mencegah input data yang tidak valid (misal: harga/jumlah bernilai negatif atau password kurang dari 6 karakter).
- Class dan Static Methods: Penggunaan @classmethod untuk mengubah state tingkat kelas dan @staticmethod untuk utilitas independen seperti validasi teks serta format rupiah.

---

## Struktur Kelas (Class Design)

### 1. Game
* Atribut Kelas: nama_platform, total_game, status_sistem
* Atribut Instansiasi: id_game, nama_game, publisher, __status (private)
* Fungsi Utama:
  * tampilkan_info() -> Menampilkan detail game.
  * @property status dan @status.setter -> Mengambil dan menguji validasi status (Aktif / Nonaktif).
  * ubah_status_sistem() -> Class method untuk mengubah status sistem platform.
  * validasi_nama_game() -> Static method untuk memeriksa kecukupan panjang nama game.

### 2. ItemTopup
* Atribut Kelas: nama_toko, total_item, mata_uang
* Atribut Instansiasi: id_item, nama_item, harga, game, __jumlah_item (private)
* Fungsi Utama:
  * tampilkan_item() -> Menampilkan informasi item beserta nama game terkait.
  * @property jumlah_item dan @jumlah_item.setter -> Mengelola stok/jumlah item dengan proteksi nilai non-negatif.
  * ubah_nama_toko() -> Class method untuk memperbarui nama toko.
  * hitung_total() -> Static method kalkulasi total harga (harga * jumlah).

### 3. Akun
* Atribut Kelas: nama_layanan, total_akun, status_layanan
* Atribut Instansiasi: username, id_akun, email, __password (private)
* Fungsi Utama:
  * tampilkan_info() -> Menampilkan info pengguna (password disembunyikan sebagai ********).
  * @property password dan @password.setter -> Mengubah password dengan syarat minimal 6 karakter.
  * ubah_status_layanan() -> Class method untuk mengubah status operasional layanan.
  * validasi_email() -> Static method pengecekan format e-mail sederhana.

### 4. Transaksi
* Atribut Kelas: nama_sistem, total_transaksi, status_transaksi
* Atribut Instansiasi: id_transaksi, akun, game, item, __total_harga (private)
* Fungsi Utama:
  * tampilkan_transaksi() -> Menampilkan invoice ringkas transaksi.
  * @property total_harga dan @total_harga.setter -> Proteksi manipulasi total harga.
  * ubah_status_transaksi() -> Class method untuk mengubah status transaksi (Diproses, Selesai, Dibatalkan).
  * format_rupiah() -> Static method untuk memformat angka ke format string Rupiah (RpXX,XXX).

---

## Cara Menjalankan Program

1. Pastikan Python 3.x telah terinstall di komputer Anda.
2. Jalankan perintah berikut melalui terminal / command prompt:

```bash
python nama_file_anda.py
