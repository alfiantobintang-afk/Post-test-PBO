# ============================================================
# CLASS GAME
# ============================================================
class Game:
    # Atribut kelas
    nama_platform = "TopUp Game Online"
    total_game = 0
    status_sistem = "Aktif"

    def __init__(self, id_game, nama_game, publisher):
        # Atribut instance public
        self.id_game = id_game
        self.nama_game = nama_game
        self.publisher = publisher

        # Atribut private
        self.__status = "Aktif"

        Game.total_game += 1

    # Instance method
    def tampilkan_info(self):
        print(f"ID Game    : {self.id_game}")
        print(f"Nama Game  : {self.nama_game}")
        print(f"Publisher  : {self.publisher}")
        print(f"Status     : {self.__status}")

    # Getter
    @property
    def status(self):
        return self.__status

    # Setter
    @status.setter
    def status(self, nilai):
        if nilai not in ["Aktif", "Nonaktif"]:
            raise ValueError("Status harus Aktif atau Nonaktif!")
        self.__status = nilai

    # Class method
    @classmethod
    def ubah_status_sistem(cls, status_baru):
        cls.status_sistem = status_baru

    # Static method
    @staticmethod
    def validasi_nama_game(nama):
        return len(nama.strip()) >= 3


# ============================================================
# CLASS ITEM TOPUP
# ============================================================
class ItemTopup:
    # Atribut kelas
    nama_toko = "Bintang Top Up"
    total_item = 0
    mata_uang = "Rupiah"

    def __init__(self, id_item, nama_item, harga, jumlah_item, game):
        # Atribut instance public
        self.id_item = id_item
        self.nama_item = nama_item
        self.harga = harga
        self.game = game

        # Atribut private
        self.__jumlah_item = jumlah_item

        ItemTopup.total_item += 1

    # Instance method
    def tampilkan_item(self):
        print(f"ID Item      : {self.id_item}")
        print(f"Nama Item    : {self.nama_item}")
        print(f"Game         : {self.game.nama_game}")
        print(f"Harga        : Rp{self.harga:,}")
        print(f"Jumlah Item  : {self.__jumlah_item}")

    # Getter
    @property
    def jumlah_item(self):
        return self.__jumlah_item

    # Setter
    @jumlah_item.setter
    def jumlah_item(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah item tidak boleh negatif!")
        self.__jumlah_item = jumlah

    # Class method
    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        if not nama_baru.strip():
            raise ValueError("Nama toko tidak boleh kosong!")
        cls.nama_toko = nama_baru

    # Static method
    @staticmethod
    def hitung_total(harga, jumlah):
        if harga < 0 or jumlah < 0:
            raise ValueError("Harga dan jumlah tidak boleh negatif!")
        return harga * jumlah


# ============================================================
# CLASS AKUN
# ============================================================
class Akun:
    # Atribut kelas
    nama_layanan = "Bintang Top Up"
    total_akun = 0
    status_layanan = "Online"

    def __init__(self, username, id_akun, email, password):
        # Atribut instance public
        self.username = username
        self.id_akun = id_akun
        self.email = email

        # Atribut private
        self.__password = password

        Akun.total_akun += 1

    # Instance method
    def tampilkan_info(self):
        print(f"Username : {self.username}")
        print(f"ID Akun  : {self.id_akun}")
        print(f"Email    : {self.email}")
        print("Password : ********")

    # Getter
    @property
    def password(self):
        return self.__password

    # Setter
    @password.setter
    def password(self, password_baru):
        if len(password_baru) < 6:
            raise ValueError("Password minimal 6 karakter!")
        self.__password = password_baru

    # Class method
    @classmethod
    def ubah_status_layanan(cls, status):
        cls.status_layanan = status

    # Static method
    @staticmethod
    def validasi_email(email):
        return "@" in email and "." in email


# ============================================================
# CLASS TRANSAKSI
# ============================================================
class Transaksi:
    # Atribut kelas
    nama_sistem = "Sistem Transaksi Top Up"
    total_transaksi = 0
    status_transaksi = "Diproses"

    def __init__(self, id_transaksi, akun, game, item):
        # Atribut instance public
        self.id_transaksi = id_transaksi
        self.akun = akun
        self.game = game
        self.item = item

        # Atribut private
        self.__total_harga = ItemTopup.hitung_total(
            item.harga,
            item.jumlah_item
        )

        Transaksi.total_transaksi += 1

    # Instance method
    def tampilkan_transaksi(self):
        print(f"ID Transaksi : {self.id_transaksi}")
        print(f"Username     : {self.akun.username}")
        print(f"Game         : {self.game.nama_game}")
        print(f"Item         : {self.item.nama_item}")
        print(f"Total Harga  : Rp{self.__total_harga:,}")
        print(f"Status       : {Transaksi.status_transaksi}")

    # Getter
    @property
    def total_harga(self):
        return self.__total_harga

    # Setter
    @total_harga.setter
    def total_harga(self, harga):
        if harga < 0:
            raise ValueError("Total harga tidak boleh negatif!")
        self.__total_harga = harga

    # Class method
    @classmethod
    def ubah_status_transaksi(cls, status):
        if status not in ["Diproses", "Selesai", "Dibatalkan"]:
            raise ValueError("Status transaksi tidak valid!")
        cls.status_transaksi = status

    # Static method
    @staticmethod
    def format_rupiah(harga):
        return f"Rp{harga:,}"


# ============================================================
# PROGRAM UTAMA / MAIN CODE
# ============================================================

print("=" * 60)
print("        SISTEM TOP UP GAME ONLINE")
print("=" * 60)


# ============================================================
# CREATE - MEMBUAT DATA GAME
# ============================================================
print("\n--- CREATE GAME ---")

game1 = Game(
    "G001",
    "Mobile Legends",
    "Moonton"
)

game2 = Game(
    "G002",
    "Valorant",
    "Riot Games"
)

print("Game berhasil dibuat.")


# ============================================================
# CREATE - MEMBUAT DATA ITEM TOPUP
# ============================================================
print("\n--- CREATE ITEM TOP UP ---")

item1 = ItemTopup(
    "I001",
    "86 Diamonds",
    20000,
    86,
    game1
)

item2 = ItemTopup(
    "I002",
    "475 Valorant Points",
    55000,
    475,
    game2
)

print("Item top up berhasil dibuat.")


# ============================================================
# CREATE - MEMBUAT DATA AKUN
# ============================================================
print("\n--- CREATE AKUN ---")

akun1 = Akun(
    "Bintang",
    "A001",
    "bintang@gmail.com",
    "bintang123"
)

akun2 = Akun(
    "Andi",
    "A002",
    "andi@gmail.com",
    "andi1234"
)

print("Akun berhasil dibuat.")


# ============================================================
# CREATE - MEMBUAT TRANSAKSI
# ============================================================
print("\n--- CREATE TRANSAKSI ---")

transaksi1 = Transaksi(
    "T001",
    akun1,
    game1,
    item1
)

transaksi2 = Transaksi(
    "T002",
    akun2,
    game2,
    item2
)

print("Transaksi berhasil dibuat.")


# ============================================================
# READ
# ============================================================
print("\n" + "=" * 60)
print("READ DATA")
print("=" * 60)

print("\n--- DATA GAME ---")
game1.tampilkan_info()
print()
game2.tampilkan_info()

print("\n--- DATA ITEM TOP UP ---")
item1.tampilkan_item()
print()
item2.tampilkan_item()

print("\n--- DATA AKUN ---")
akun1.tampilkan_info()
print()
akun2.tampilkan_info()

print("\n--- DATA TRANSAKSI ---")
transaksi1.tampilkan_transaksi()
print()
transaksi2.tampilkan_transaksi()


# ============================================================
# CLASS METHOD
# ============================================================
print("\n" + "=" * 60)
print("PENGUJIAN CLASS METHOD")
print("=" * 60)

Game.ubah_status_sistem("Maintenance")
print("Status sistem Game :", Game.status_sistem)

ItemTopup.ubah_nama_toko("Bintang Game Store")
print("Nama toko          :", ItemTopup.nama_toko)

Akun.ubah_status_layanan("Online")
print("Status layanan     :", Akun.status_layanan)

Transaksi.ubah_status_transaksi("Selesai")
print("Status transaksi   :", Transaksi.status_transaksi)


# ============================================================
# STATIC METHOD
# ============================================================
print("\n" + "=" * 60)
print("PENGUJIAN STATIC METHOD")
print("=" * 60)

print(
    "Validasi nama game:",
    Game.validasi_nama_game("Mobile Legends")
)

# Perbaikan dilakukan pada baris berikut (ItemTopup diganti Transaksi)
print(
    "Total harga item 1:",
    Transaksi.format_rupiah(
        ItemTopup.hitung_total(item1.harga, item1.jumlah_item)
    )
)

print(
    "Validasi email:",
    Akun.validasi_email(akun1.email)
)

print(
    "Format harga transaksi:",
    Transaksi.format_rupiah(transaksi1.total_harga)
)


# ============================================================
# GETTER
# ============================================================
print("\n" + "=" * 60)
print("PENGUJIAN GETTER")
print("=" * 60)

print("Status Game       :", game1.status)
print("Jumlah Item       :", item1.jumlah_item)
print("Password Akun     :", akun1.password)
print("Total Harga       :", transaksi1.total_harga)


# ============================================================
# SETTER VALID
# ============================================================
print("\n" + "=" * 60)
print("PENGUJIAN SETTER DATA VALID")
print("=" * 60)

game1.status = "Nonaktif"
print("Status Game setelah diubah:", game1.status)

item1.jumlah_item = 100
print("Jumlah item setelah diubah:", item1.jumlah_item)

akun1.password = "passwordbaru"
print("Password berhasil diubah.")

transaksi1.total_harga = 25000
print("Total harga setelah diubah:", transaksi1.total_harga)


# ============================================================
# SETTER TIDAK VALID
# ============================================================
print("\n" + "=" * 60)
print("PENGUJIAN SETTER DATA TIDAK VALID")
print("=" * 60)

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
# DELETE
# ============================================================
print("\n" + "=" * 60)
print("DELETE DATA")
print("=" * 60)

# Pelanggan menghapus orderan
print("Transaksi T002 dihapus.")
del transaksi2

# Admin menghapus menu item
print("Item I002 dihapus.")
del item2

# Admin menghapus menu game
print("Game G002 dihapus.")
del game2


# ============================================================
# INFORMASI JUMLAH DATA
# ============================================================
print("\n" + "=" * 60)
print("JUMLAH DATA")
print("=" * 60)

print("Total Game       :", Game.total_game)
print("Total Item Topup :", ItemTopup.total_item)
print("Total Akun       :", Akun.total_akun)
print("Total Transaksi  :", Transaksi.total_transaksi)

print("\nProgram selesai.")