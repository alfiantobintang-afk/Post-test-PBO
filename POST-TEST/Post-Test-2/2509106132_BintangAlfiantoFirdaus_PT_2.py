# ============================================================
# SUPERCLASS GAME
# ============================================================
class Game:
    nama_platform = "TopUp Game Online"
    total_game = 0
    status_sistem = "Aktif"

    def __init__(self, id_game, nama_game, publisher):
        self.id_game = id_game
        self.nama_game = nama_game

        # Protected: dapat diakses subclass
        self._publisher = publisher

        # Private: khusus internal superclass
        self.__status = "Aktif"

        # Agregasi: game menyimpan referensi item top up
        self.daftar_item = []

        Game.total_game += 1

    def tampilkan_info(self):
        print(f"ID Game   : {self.id_game}")
        print(f"Nama Game : {self.nama_game}")
        print(f"Publisher : {self._publisher}")
        print(f"Status    : {self.__status}")

    def tambah_item(self, item):
        self.daftar_item.append(item)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, nilai):
        if nilai not in ["Aktif", "Nonaktif"]:
            raise ValueError("Status harus Aktif atau Nonaktif!")
        self.__status = nilai

    @classmethod
    def ubah_status_sistem(cls, status_baru):
        cls.status_sistem = status_baru

    @staticmethod
    def validasi_nama_game(nama):
        return len(nama.strip()) >= 3


# ============================================================
# SUBCLASS 1: MOBILE GAME
# ============================================================
class MobileGame(Game):
    def __init__(self, id_game, nama_game, publisher,
                 ukuran_game):
        super().__init__(id_game, nama_game, publisher)

        # Atribut unik subclass
        self.ukuran_game = ukuran_game

    # Method overriding
    def tampilkan_info(self):
        print("\n=== INFORMASI MOBILE GAME ===")
        print(f"ID Game      : {self.id_game}")
        print(f"Nama Game    : {self.nama_game}")
        print(f"Publisher    : {self._publisher}")
        print(f"Ukuran Game  : {self.ukuran_game} GB")
        print(f"Status       : {self.status}")


# ============================================================
# SUBCLASS 2: PC GAME
# ============================================================
class PCGame(Game):
    def __init__(self, id_game, nama_game, publisher,
                 spesifikasi_minimum):
        super().__init__(id_game, nama_game, publisher)

        # Atribut unik subclass
        self.spesifikasi_minimum = spesifikasi_minimum

    # Method overriding
    def tampilkan_info(self):
        print("\n=== INFORMASI PC GAME ===")
        print(f"ID Game       : {self.id_game}")
        print(f"Nama Game     : {self.nama_game}")
        print(f"Publisher     : {self._publisher}")
        print(f"Spesifikasi   : {self.spesifikasi_minimum}")
        print(f"Status        : {self.status}")


# ============================================================
# CLASS ITEM TOPUP
# ============================================================
class ItemTopup:
    nama_toko = "Bintang Top Up"
    total_item = 0
    mata_uang = "Rupiah"

    def __init__(self, id_item, nama_item, harga,
                 jumlah_item, game):
        self.id_item = id_item
        self.nama_item = nama_item
        self.harga = harga
        self.game = game
        self.__jumlah_item = jumlah_item

        # Agregasi: item terhubung dengan game
        # Game dan item tetap berupa objek terpisah
        game.tambah_item(self)

        ItemTopup.total_item += 1

    def tampilkan_item(self):
        print(f"ID Item     : {self.id_item}")
        print(f"Nama Item   : {self.nama_item}")
        print(f"Game        : {self.game.nama_game}")
        print(f"Harga       : {self.format_rupiah(self.harga)}")
        print(f"Jumlah Item : {self.__jumlah_item}")

    @property
    def jumlah_item(self):
        return self.__jumlah_item

    @jumlah_item.setter
    def jumlah_item(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah item tidak boleh negatif!")
        self.__jumlah_item = jumlah

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        if not nama_baru.strip():
            raise ValueError("Nama toko tidak boleh kosong!")
        cls.nama_toko = nama_baru

    @staticmethod
    def hitung_total(harga, jumlah):
        if harga < 0 or jumlah < 0:
            raise ValueError("Harga dan jumlah tidak boleh negatif!")
        return harga * jumlah

    @staticmethod
    def format_rupiah(harga):
        return f"Rp{harga:,}".replace(",", ".")


# ============================================================
# CLASS AKUN
# ============================================================
class Akun:
    nama_layanan = "Bintang Top Up"
    total_akun = 0
    status_layanan = "Online"

    def __init__(self, username, id_akun, email, password):
        self.username = username
        self.id_akun = id_akun
        self.email = email
        self.__password = password

        Akun.total_akun += 1

    def tampilkan_info(self):
        print(f"Username : {self.username}")
        print(f"ID Akun  : {self.id_akun}")
        print(f"Email    : {self.email}")
        print("Password : ********")

    @property
    def password(self):
        # Password tidak ditampilkan secara langsung
        return self.__password

    @password.setter
    def password(self, password_baru):
        if len(password_baru) < 6:
            raise ValueError("Password minimal 6 karakter!")
        self.__password = password_baru

    @classmethod
    def ubah_status_layanan(cls, status):
        cls.status_layanan = status

    @staticmethod
    def validasi_email(email):
        return "@" in email and "." in email


# ============================================================
# CLASS DETAIL TRANSAKSI
# ============================================================
class DetailTransaksi:
    def __init__(self, nama_item, harga, jumlah):
        self.nama_item = nama_item
        self.harga = harga
        self.jumlah = jumlah

    def hitung_subtotal(self):
        return self.harga * self.jumlah


# ============================================================
# CLASS TRANSAKSI
# ============================================================
class Transaksi:
    nama_sistem = "Sistem Transaksi Top Up"
    total_transaksi = 0
    status_transaksi = "Diproses"

    def __init__(self, id_transaksi, akun, game, item):
        self.id_transaksi = id_transaksi

        # Asosiasi: transaksi berhubungan dengan akun
        self.akun = akun

        # Asosiasi: transaksi menggunakan game
        self.game = game

        # Asosiasi: transaksi menggunakan item top up
        self.item = item

        # Komposisi: detail dibuat dan dimiliki transaksi
        # Detail berisi salinan data item pada saat transaksi
        self.__detail = DetailTransaksi(
            item.nama_item,
            item.harga,
            item.jumlah_item
        )

        self.__total_harga = self.__detail.hitung_subtotal()

        Transaksi.total_transaksi += 1

    def tampilkan_transaksi(self):
        print(f"ID Transaksi : {self.id_transaksi}")
        print(f"Username     : {self.akun.username}")
        print(f"Game         : {self.game.nama_game}")
        print(f"Item         : {self.__detail.nama_item}")
        print(f"Jumlah       : {self.__detail.jumlah}")
        print(
            f"Total Harga  : "
            f"{ItemTopup.format_rupiah(self.__total_harga)}"
        )
        print(f"Status       : {Transaksi.status_transaksi}")

    @property
    def total_harga(self):
        return self.__total_harga

    @total_harga.setter
    def total_harga(self, harga):
        if harga < 0:
            raise ValueError("Total harga tidak boleh negatif!")
        self.__total_harga = harga

    @classmethod
    def ubah_status_transaksi(cls, status):
        if status not in ["Diproses", "Selesai", "Dibatalkan"]:
            raise ValueError("Status transaksi tidak valid!")
        cls.status_transaksi = status

    @staticmethod
    def format_rupiah(harga):
        return f"Rp{harga:,}".replace(",", ".")


# ============================================================
# PROGRAM UTAMA
# ============================================================
print("=" * 55)
print("       SISTEM TOP UP GAME ONLINE")
print("          BINTANG TOP UP")
print("=" * 55)


# CREATE GAME
print("\n--- DATA GAME ---")

game1 = MobileGame(
    "G001", "Mobile Legends", "Moonton", 5
)

game2 = PCGame(
    "G002", "Valorant", "Riot Games", "RAM 8 GB"
)

game1.tampilkan_info()
game2.tampilkan_info()


# CREATE ITEM TOP UP
print("\n--- DATA ITEM TOP UP ---")

item1 = ItemTopup(
    "I001", "86 Diamonds", 20000, 86, game1
)

item2 = ItemTopup(
    "I002", "475 Valorant Points", 55000, 475, game2
)

item1.tampilkan_item()
print()
item2.tampilkan_item()


# CREATE AKUN
print("\n--- DATA AKUN ---")

akun1 = Akun(
    "Bintang", "A001", "bintang@gmail.com", "bintang123"
)

akun2 = Akun(
    "Andi", "A002", "andi@gmail.com", "andi1234"
)

akun1.tampilkan_info()
print()
akun2.tampilkan_info()


# CREATE TRANSAKSI
print("\n--- DATA TRANSAKSI ---")

transaksi1 = Transaksi("T001", akun1, game1, item1)
transaksi2 = Transaksi("T002", akun2, game2, item2)

transaksi1.tampilkan_transaksi()
print()
transaksi2.tampilkan_transaksi()


# ============================================================
# PENGUJIAN INHERITANCE
# ============================================================
print("\n--- PENGUJIAN INHERITANCE ---")

print("MobileGame merupakan Game:",
      isinstance(game1, Game))

print("PCGame merupakan Game:",
      isinstance(game2, Game))

print("Publisher Mobile Game:", game1._publisher)
print("Ukuran Mobile Game:", game1.ukuran_game, "GB")
print("Spesifikasi PC Game:", game2.spesifikasi_minimum)


# ============================================================
# PENGUJIAN RELASI UML
# ============================================================
print("\n--- PENGUJIAN RELASI UML ---")

# Agregasi
print("Jumlah item pada Mobile Legends:",
      len(game1.daftar_item))

print("Jumlah item pada Valorant:",
      len(game2.daftar_item))

# Asosiasi
print("Akun transaksi T001:",
      transaksi1.akun.username)

print("Game transaksi T001:",
      transaksi1.game.nama_game)

# Komposisi
print("Detail transaksi T001:",
      transaksi1.total_harga)


# ============================================================
# PENGUJIAN GETTER DAN SETTER
# ============================================================
print("\n--- GETTER DAN SETTER ---")

print("Status game:", game1.status)
game1.status = "Nonaktif"
print("Status setelah diubah:", game1.status)

print("Jumlah item:", item1.jumlah_item)
item1.jumlah_item = 100
print("Jumlah item setelah diubah:", item1.jumlah_item)

akun1.password = "passwordbaru"
print("Password berhasil diperbarui.")

transaksi1.total_harga = 25000
print("Total transaksi setelah diubah:",
      transaksi1.total_harga)


# ============================================================
# PENGUJIAN CLASS METHOD DAN STATIC METHOD
# ============================================================
print("\n--- CLASS METHOD DAN STATIC METHOD ---")

Game.ubah_status_sistem("Maintenance")
print("Status sistem:", Game.status_sistem)

ItemTopup.ubah_nama_toko("Bintang Game Store")
print("Nama toko:", ItemTopup.nama_toko)

Akun.ubah_status_layanan("Online")
print("Status layanan:", Akun.status_layanan)

Transaksi.ubah_status_transaksi("Selesai")
print("Status transaksi:", Transaksi.status_transaksi)

print("Validasi nama game:",
      Game.validasi_nama_game("Mobile Legends"))

print("Validasi email:",
      Akun.validasi_email(akun1.email))

print("Format harga:",
      Transaksi.format_rupiah(transaksi1.total_harga))


# ============================================================
# PENGUJIAN VALIDASI
# ============================================================
print("\n--- PENGUJIAN VALIDASI ---")

try:
    game1.status = "Tidak Jelas"
except ValueError as e:
    print("Error Game:", e)

try:
    item1.jumlah_item = -10
except ValueError as e:
    print("Error Item:", e)

try:
    akun1.password = "123"
except ValueError as e:
    print("Error Password:", e)

try:
    transaksi1.total_harga = -5000
except ValueError as e:
    print("Error Transaksi:", e)


# ============================================================
# INFORMASI JUMLAH DATA
# ============================================================
print("\n--- JUMLAH DATA ---")

print("Total Game       :", Game.total_game)
print("Total Item Topup :", ItemTopup.total_item)
print("Total Akun       :", Akun.total_akun)
print("Total Transaksi  :", Transaksi.total_transaksi)

print("\nProgram selesai.")