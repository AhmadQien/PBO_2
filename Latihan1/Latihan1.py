class Mobil:
    def __init__(self, merk, tahun_pembuatan):
        self.merk = merk
        self.tahun_pembuatan = tahun_pembuatan
    def info(self):
        print(f"mobil {self.merk} tahun_pembuatan {self.tahun_pembuatan}")

Mobil = Mobil ("Honda Civic Type R", "2023") 
Mobil.info()