class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
class Penyanyi:
    def __init__(self, lagu, genre):
        self.lagu = lagu
        self.genre = genre
    def display_info(self):
        print(f"Lagu: {self.lagu}")
class PenyanyiPekerja(Orang, Pekerja, Penyanyi):
    def __init__(self, nama, umur, pekerjaan, gaji, lagu, genre):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Penyanyi.__init__(self, lagu, genre)
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Lagu: {self.lagu}") 
# contoh penggunaan
penyanyi_pekerjaC = PenyanyiPekerja("Rosa", 30, "Penyanyi", "$3
                                    000", "Pudar", "Fiksi")
penyanyi_pekerjaC.display_info()