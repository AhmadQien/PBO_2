class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def info(self):
        print(f"Nama : {self.nama}\ nim : {self.nim}")

Mahasiswa = Mahasiswa ("Muhammad Al Muttaqien", "210511152")
Mahasiswa.info()