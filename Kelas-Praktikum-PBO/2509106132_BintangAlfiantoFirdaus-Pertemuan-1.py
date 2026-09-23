class mobil:
    def __init__(self, brand, series, warna):
        self.brand = brand
        self.series = series
        self.warna = warna

    def infomobil(self):
        print(f"mobil ini memiliki brand {self.brand}")