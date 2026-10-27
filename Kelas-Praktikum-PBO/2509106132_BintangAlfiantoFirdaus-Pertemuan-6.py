#Single Responsibility Principle
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def serang(self, target): # tugas 1: pertarungan
        target.health -= 10

    # def tampilkan_status(self): # tugas 2: tampilan
    #     print(f"{self.name} | HP {self.health}")

    # def simpan(self, nama_file): # tugas 3: penyimpanan
    #     with open(nama_file, "a") as f:
    #         f.write(f"{self.name},{self.health}\n")

class TampilanHero: # hanya tampilan
    def tampilkan(self, hero):
        print(f"{hero.name} | HP {hero.health}")

class PenyimpanHero: # hanya penyimpanan
    def simpan(self, hero, nama_file):
        with open(nama_file, "a") as f:
            f.write(f"{hero.name},{hero.health}\n")

esme = Hero("Esmeralda", 100)
Hero("Esmeralda", 100).serang(esme)
TampilanHero().menampilkanhero(esme)
PenyimpanHero().simpan(esme, "data_hero.txt")