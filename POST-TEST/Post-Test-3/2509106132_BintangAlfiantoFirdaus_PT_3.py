from abc import ABC, abstractmethod


# ============================================================
# GAME DAN INHERITANCE JENIS GAME
# ============================================================
class Game:
    nama_platform = "TopUp Game Online"
    total_game = 0
    status_sistem = "Aktif"

    def __init__(self, id_game, nama_game, publisher):
        self.id_game = id_game
        self.nama_game = nama_game
        self._publisher = publisher       # protected
        self.__status = "Aktif"           # private
        self.daftar_item = []             # agregasi: kumpulan referensi item
        Game.total_game += 1

    def tampilkan_info(self):
        print(f"Game: {self.nama_game} | Publisher: {self._publisher}")

    def tambah_item(self, item):
        self.daftar_item.append(item)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, nilai):
        if nilai not in ("Aktif", "Nonaktif"):
            raise ValueError("Status harus Aktif atau Nonaktif!")
        self.__status = nilai

    @classmethod
    def ubah_status_sistem(cls, status_baru):
        cls.status_sistem = status_baru

    @staticmethod
    def validasi_nama_game(nama):
        return len(nama.strip()) >= 3


class MobileGame(Game):
    def __init__(self, id_game, nama_game, publisher, ukuran_game):
        super().__init__(id_game, nama_game, publisher)
        self.ukuran_game = ukuran_game

    def tampilkan_info(self):  # overriding
        print(f"Mobile Game: {self.nama_game} | Ukuran: {self.ukuran_game} GB")


class PCGame(Game):
    def __init__(self, id_game, nama_game, publisher, spesifikasi_minimum):
        super().__init__(id_game, nama_game, publisher)
        self.spesifikasi_minimum = spesifikasi_minimum

    def tampilkan_info(self):  # overriding
        print(f"PC Game: {self.nama_game} | Spesifikasi: {self.spesifikasi_minimum}")


# ============================================================
# ABSTRAKSI: ABSTRACT BASE CLASS DAN SUBCLASS
# ============================================================
class LayananTopup(ABC):
    def __init__(self, id_item, nama_item, harga, jumlah_item, game):
        self.id_item = id_item
        self._nama_item = nama_item       # protected, dapat dipakai subclass
        self._harga = harga               # protected, dapat dipakai subclass
        self.jumlah_item = jumlah_item
        self.game = game
        self.__kode_internal = "INTERNAL-TOPUP"  # private untuk internal class

    @abstractmethod
    def proses_topup(self):
        """Setiap jenis layanan wajib menentukan proses top up sendiri."""
        pass

    @abstractmethod
    def hitung_biaya(self):
        """Setiap jenis layanan wajib menentukan perhitungan biayanya."""
        pass

    def jalankan(self):
        """Method konkret yang dipakai bersama oleh semua subclass."""
        print(f"Menjalankan layanan: {self._nama_item}")
        print(self.proses_topup())
        print(f"Total biaya: {self.format_rupiah(self.hitung_biaya())}")

    @staticmethod
    def format_rupiah(nilai):
        return f"Rp{nilai:,.0f}".replace(",", ".")

    def __str__(self):
        return f"{self._nama_item} ({self.format_rupiah(self._harga)})"


class ItemTopupDigital(LayananTopup):
    def __init__(self, id_item, nama_item, harga, jumlah_item, game, bonus_item):
        super().__init__(id_item, nama_item, harga, jumlah_item, game)
        self.bonus_item = bonus_item  # atribut unik subclass
        game.tambah_item(self)        # agregasi: game menyimpan referensi item

    def proses_topup(self):           # overriding
        return f"Top up digital berhasil. Bonus: {self.bonus_item}."

    def hitung_biaya(self):
        return self._harga * self.jumlah_item


class ItemTopupLogin(LayananTopup):
    def __init__(self, id_item, nama_item, harga, jumlah_item, game, metode_login):
        super().__init__(id_item, nama_item, harga, jumlah_item, game)
        self.metode_login = metode_login  # atribut unik subclass
        game.tambah_item(self)

    def proses_topup(self):           # overriding dengan perilaku berbeda
        return f"Top up membutuhkan login melalui {self.metode_login}."

    def hitung_biaya(self):
        biaya_layanan = 5000
        return (self._harga * self.jumlah_item) + biaya_layanan


# ============================================================
# AKUN DAN DETAIL TRANSAKSI
# ============================================================
class Akun:
    total_akun = 0

    def __init__(self, username, id_akun, email, password):
        self.username = username
        self.id_akun = id_akun
        self.email = email
        self.__password = password
        Akun.total_akun += 1

    def tampilkan_info(self):
        print(f"Username: {self.username} | ID: {self.id_akun} | Email: {self.email}")
        print("Password: ********")


class DetailTransaksi:
    def __init__(self, nama_item, harga, jumlah):
        self.nama_item = nama_item
        self.harga = harga
        self.jumlah = jumlah

    def hitung_subtotal(self):
        return self.harga * self.jumlah


class Transaksi:
    total_transaksi = 0

    def __init__(self, id_transaksi, akun, game, item):
        self.id_transaksi = id_transaksi
        self.akun = akun       # asosiasi
        self.game = game       # asosiasi
        self.item = item       # asosiasi
        # Komposisi: detail dibuat dan dimiliki oleh transaksi.
        self.__detail = DetailTransaksi(
            item._nama_item, item._harga, item.jumlah_item
        )
        self.__total_harga = item.hitung_biaya()
        Transaksi.total_transaksi += 1

    @property
    def total_harga(self):
        return self.__total_harga

    def tampilkan_transaksi(self):
        print(f"ID Transaksi: {self.id_transaksi}")
        print(f"Pelanggan   : {self.akun.username}")
        print(f"Game        : {self.game.nama_game}")
        print(f"Item        : {self.__detail.nama_item}")
        print(f"Subtotal    : {LayananTopup.format_rupiah(self.__detail.hitung_subtotal())}")
        print(f"Total bayar : {LayananTopup.format_rupiah(self.__total_harga)}")


# ============================================================
# DUCK TYPING: KELAS TIDAK TERKAIT INHERITANCE
# ============================================================
class NotifikasiEmail:
    def kirim(self, pesan):
        print(f"Email terkirim: {pesan}")


class NotifikasiSMS:
    def kirim(self, pesan):
        print(f"SMS terkirim: {pesan}")


def kirim_notifikasi(media, pesan):
    """Duck typing: fungsi menerima objek apa pun yang punya method kirim()."""
    media.kirim(pesan)


# ============================================================
# PROGRAM UTAMA DAN PENGUJIAN
# ============================================================
if __name__ == "__main__":
    print("=" * 58)
    print("       SISTEM TOP UP GAME ONLINE - POSTTEST")
    print("=" * 58)

    game_mobile = MobileGame("G001", "Mobile Legends", "Moonton", 5)
    game_pc = PCGame("G002", "Valorant", "Riot Games", "RAM 8 GB")

    item_digital = ItemTopupDigital(
        "I001", "86 Diamonds", 20000, 1, game_mobile, "Bonus 5 Diamonds"
    )
    item_login = ItemTopupLogin(
        "I002", "475 Valorant Points", 55000, 1, game_pc, "Riot Games"
    )

    akun = Akun("Bintang", "A001", "bintang@example.com", "rahasia123")

    print("\n" + "=" * 58)
    print("8.2 BUKTI PENGUJIAN ABSTRAKSI")
    print("=" * 58)

    print("\n--- PENGUJIAN ABSTRACT CLASS ---")
    try:
        LayananTopup("X", "Contoh", 1000, 1, game_mobile)
    except TypeError as error:
        print("Abstract class tidak dapat diinstansiasi.")
        print("TypeError berhasil ditangkap.")
        print("Pesan:", error)

    print("\n--- IMPLEMENTASI SUBCLASS ---")
    layanan = [item_digital, item_login]

    for item in layanan:
        item.jalankan()
        print()
    print("--- RELASI AGREGASI ---")
    print(f"Item pada {game_mobile.nama_game}: {len(game_mobile.daftar_item)}")
    print(f"Item pada {game_pc.nama_game}: {len(game_pc.daftar_item)}")

    print("\n--- TRANSAKSI (ASOSIASI DAN KOMPOSISI) ---")
    transaksi = Transaksi("T001", akun, game_mobile, item_digital)
    transaksi.tampilkan_transaksi()

    print("\n" + "=" * 58)
    print("8.3 BUKTI PENGUJIAN POLIMORFISME")
    print("=" * 58)

    print("\n--- POLIMORFISME VIA INHERITANCE ---")
    daftar_game = [game_mobile, game_pc]

    for game in daftar_game:
        game.tampilkan_info()

    print("\n--- POLIMORFISME VIA OVERRIDING ---")
    daftar_layanan = [item_digital, item_login]

    for item in daftar_layanan:
        print(item.proses_topup())

    print("\n--- DUCK TYPING ---")
    pesan = "Pesanan T001 sedang diproses."

    kirim_notifikasi(NotifikasiEmail(), pesan)
    kirim_notifikasi(NotifikasiSMS(), pesan)

    print("\n--- OPERATOR OVERLOADING: __str__ ---")
    print(item_digital)
    print("\n--- BUKTI ABSTRACT CLASS TIDAK BISA DIINSTANTIASI ---")
    try:
        LayananTopup("X", "Contoh", 1000, 1, game_mobile)
    except TypeError as error:
        print("TypeError berhasil ditangkap:")
        print(error)

    print("\n--- INHERITANCE GAME ---")
    game_mobile.tampilkan_info()
    game_pc.tampilkan_info()

    print("\nProgram selesai.")
