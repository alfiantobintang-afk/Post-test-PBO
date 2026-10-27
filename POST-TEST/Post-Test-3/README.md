# Sistem Top Up Game Online — Bintang Top Up

## 1. Deskripsi Program

Sistem Top Up Game Online — Bintang Top Up merupakan program berbasis Python yang digunakan untuk mengelola data game, item top up, akun pengguna, dan transaksi pembelian item game.

Program ini dibuat untuk memenuhi tugas Posttest Pemrograman Berorientasi Objek (OOP) dengan menerapkan konsep inheritance, relasi UML, abstraksi menggunakan Abstract Base Class (ABC), polimorfisme, duck typing, dan operator overloading.

## 2. Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Paradigma pemrograman: Object-Oriented Programming (OOP)
- Library: `abc`
- Tools diagram: diagrams.net (draw.io)
- Editor: Visual Studio Code atau editor Python lainnya

## 3. Class Diagram

Class Diagram menggambarkan struktur kelas, atribut utama, method, serta hubungan antarobjek dalam Sistem Top Up Game Online.

### 3.1 Gambar Class Diagram

Gambar dalam bentuk draw.io
https://drive.google.com/file/d/1tPlTm8EEeJQQaFo3lGevmbHDRFQhi-wy/view?usp=sharing

Gambar 1. Class Diagram Sistem Top Up Game Online.

### 3.2 Penjelasan Relasi UML

#### A. Asosiasi (Association)

Relasi asosiasi terdapat antara kelas `Transaksi` dengan kelas `Akun`, `Game`, dan `ItemTopup`. Kelas `Transaksi` menggunakan objek-objek tersebut untuk mencatat informasi akun pembeli, game yang dipilih, dan item yang dibeli.

#### B. Agregasi (Aggregation)

Relasi agregasi terdapat antara kelas `Game` dan `ItemTopup`. Sebuah game memiliki daftar item top up melalui atribut `daftar_item`, sedangkan objek item dibuat secara terpisah sehingga tetap dapat berdiri sendiri meskipun tidak lagi terhubung dengan game tersebut.

#### C. Komposisi (Composition)

Relasi komposisi terdapat antara kelas `Transaksi` dan `DetailTransaksi`. Objek `DetailTransaksi` dibuat di dalam konstruktor `Transaksi` sebagai bagian dari transaksi tersebut.

Ketiga relasi harus diterapkan dalam kode program, bukan hanya digambarkan pada diagram. Implementasi komposisi merupakan rancangan kepemilikan objek dan tidak otomatis menjamin penghapusan objek bagian ketika objek pemilik dihapus dalam Python.

## 4. Penerapan Inheritance

Inheritance atau pewarisan digunakan agar subclass dapat mewarisi atribut dan method dari superclass.

Pada program ini, kelas `Game` berfungsi sebagai superclass, sedangkan `MobileGame` dan `PCGame` merupakan subclass.

### Kelas yang digunakan

- `Game`: superclass yang menyimpan informasi umum game.
- `MobileGame`: subclass dengan atribut tambahan `ukuran_game`.
- `PCGame`: subclass dengan atribut tambahan `spesifikasi_minimum`.

Kedua subclass memanggil konstruktor superclass menggunakan `super().__init__(...)`. Method `tampilkan_info()` di-override untuk menghasilkan informasi berbeda sesuai dengan karakteristik masing-masing jenis game.

Program juga menerapkan atribut protected, seperti `_publisher`, dan atribut private, seperti `__status`, untuk mengatur akses terhadap data.

## 5. Penerapan Abstraksi (Abstract Base Class)

Abstraksi diterapkan menggunakan modul `abc`, yaitu `ABC` dan dekorator `@abstractmethod`.

Abstract class berfungsi sebagai kerangka yang menentukan method yang wajib diimplementasikan oleh subclass.

Ketentuan implementasi:

- Minimal satu abstract class.
- Minimal dua abstract method.
- Minimal dua subclass yang mengimplementasikan seluruh abstract method.
- Minimal satu method konkret yang dapat digunakan bersama oleh seluruh subclass.

Abstract class tidak dapat diinstansiasi secara langsung selama masih memiliki abstract method yang belum diimplementasikan.

### Bukti Abstract Class Tidak Dapat Diinstansiasi

Pengujian dilakukan menggunakan `try-except TypeError`.

Contoh keluaran yang diharapkan:

```text
=== PENGUJIAN ABSTRACT CLASS ===
Abstract class tidak dapat diinstansiasi.
TypeError berhasil ditangkap.
```

Keluaran tersebut merupakan contoh format hasil pengujian. Screenshot laporan harus menggunakan hasil aktual dari program yang dijalankan.

## 6. Penerapan Polimorfisme

Polimorfisme memungkinkan objek dari kelas berbeda menjalankan method yang sama dengan perilaku yang berbeda.

### 6.1 Polimorfisme melalui Pewarisan

Polimorfisme melalui pewarisan diterapkan dengan melakukan overriding terhadap method `tampilkan_info()` pada subclass `MobileGame` dan `PCGame`.

Kedua objek dipanggil melalui satu perulangan yang berisi objek dari subclass berbeda. Setiap objek menjalankan implementasi method miliknya sendiri tanpa menggunakan rantai `if/elif` untuk memeriksa tipe objek.

### 6.2 Duck Typing

Duck typing diterapkan melalui dua kelas yang tidak memiliki hubungan inheritance, tetapi menyediakan method dengan nama yang sama.

Kedua objek diproses menggunakan satu fungsi yang memanggil method tersebut. Fungsi dapat bekerja selama objek menyediakan method yang dibutuhkan tanpa harus memeriksa tipe kelasnya.

Nama kelas dan method yang digunakan harus disesuaikan dengan kode program utama.

### 6.3 Operator Overloading

Operator overloading diterapkan dengan mendefinisikan minimal satu magic method pada salah satu kelas.

Contohnya, method `__str__()` digunakan untuk menentukan representasi teks objek ketika ditampilkan menggunakan `print()`. Alternatif lainnya adalah `__add__()` untuk mendefinisikan perilaku operator penjumlahan pada objek tertentu.

Implementasi yang dicantumkan dalam laporan harus sesuai dengan magic method yang benar-benar tersedia pada kode program.

## 7. Penerapan Encapsulation

Encapsulation digunakan untuk membatasi akses langsung terhadap data tertentu dan mengatur cara data dibaca atau diubah.

Contoh penerapan dalam program:

- Public: `nama_game`, `id_game`, dan `username`.
- Protected: `_publisher`.
- Private: `__status`, `__password`, dan `__detail`.
- Getter dan setter digunakan untuk membaca atau mengubah data dengan validasi.

Validasi membantu mencegah data yang tidak sesuai, seperti jumlah item negatif, status game yang tidak valid, atau password yang terlalu pendek.

## 8. Screenshot Output Program

Screenshot berikut harus disiapkan setelah program berhasil dijalankan.

### 8.1 Output Program Utama

![Output program utama](docs/output-program.png)

Gambar 2. Output program yang menampilkan informasi game, item top up, akun, dan transaksi.

### 8.2 Bukti Pengujian Abstraksi

![Bukti abstract class tidak dapat diinstansiasi](docs/output-abstraksi.png)

Gambar 3. Output pengujian yang menunjukkan abstract class tidak dapat diinstansiasi dan menghasilkan `TypeError`.

### 8.3 Bukti Pengujian Polimorfisme

![Bukti polimorfisme](docs/output-polimorfisme.png)

Gambar 4. Output pemanggilan method pada objek subclass berbeda, duck typing, dan operator overloading.

Gambar harus berupa screenshot asli dari hasil eksekusi program dan disimpan di folder `docs` agar dapat ditampilkan dengan benar pada README GitHub.

## 9. Struktur Folder Proyek

```text
Bintang-Top-Up/
├── main.py
├── README.md
└── docs/
    ├── class-diagram.png
    ├── output-program.png
    ├── output-abstraksi.png
    └── output-polimorfisme.png
```

## 10. Cara Menjalankan Program

1. Pastikan Python telah terinstal.
2. Buka folder proyek melalui Visual Studio Code atau terminal.
3. Simpan kode utama dalam file `main.py`.
4. Jalankan perintah berikut:

```bash
python main.py
```

Pada Windows, jika perintah tersebut tidak tersedia, gunakan:

```bash
py main.py
```

5. Periksa hasil keluaran program dan pastikan seluruh pengujian berjalan sesuai dengan implementasi kode.

## 11. Kesimpulan

Sistem Top Up Game Online — Bintang Top Up merupakan program pengelolaan game, akun, item top up, dan transaksi yang menerapkan konsep Pemrograman Berorientasi Objek menggunakan Python.

Penerapan inheritance, relasi UML, abstraksi, encapsulation, dan polimorfisme membantu menghasilkan struktur program yang terorganisasi, mendukung penggunaan ulang kode, serta memudahkan pengembangan fitur pada masa mendatang.

---

Nama Proyek: Sistem Top Up Game Online — Bintang Top Up

Mata Kuliah: Pemrograman Berorientasi Objek

Bahasa Pemrograman: Python
