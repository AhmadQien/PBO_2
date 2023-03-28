class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def get_details(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}")
class Karyawan(Orang):
    def __init__(self, nama, umur, id, gaji):
        super().__init__(nama, umur)
        self.id = id
        self.gaji = gaji
    def get_details(self):
        super().get_details()
        print(f"ID: {self.id}, Gaji: {self.gaji}")
class Menejer(Karyawan):
    def __init__(self, nama, umur, id, gaji, departemen):
        super().__init__(nama, umur, id, gaji)
        self.departemen = departemen
    def get_details(self):
        super().get_details()
        print(f"Departemen: {self.departemen}")

menejer = Menejer("Winarto", 22, 2001, "$1000", "PT.Makmur")
menejer.get_details()