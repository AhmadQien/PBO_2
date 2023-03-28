class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama, "sedang belajar")

class Koki:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def memasak(self):
        print(self.nama, "sedang memasak")

class MahasiswaKoki(Mahasiswa, Koki):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Koki.__init__(self, nama, pekerjaan)

    def tidur(self):
        print(self.nama, "sedang tidur")

mhs_pekerja = MahasiswaKoki("Dadang", "120005", "Operator")
mhs_pekerja.belajar() # output: Dadang sedang belajar
mhs_pekerja.memasak() # output: Dadang sedang memasak
mhs_pekerja.tidur() # output: Dadang sedang tidur