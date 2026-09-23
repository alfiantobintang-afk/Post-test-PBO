class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo
def get_saldo(self):
    return self.__saldo
def set_saldo(self, saldo_baru):
    if saldo_baru < 0:
        print("Saldo tidak boleh negatif.")
    else:
        self.__saldo = saldo_baru

rekening = RekeningBank("Budi", 100000)
print(rekening.get_saldo())
rekening.set_saldo(-500) # ditolak oleh validasi
rekening.set_saldo(200000) # diterima
print(rekening.get_saldo())