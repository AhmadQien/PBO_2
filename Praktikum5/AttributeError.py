class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def get_umur(self):
        return self.umur

manusia = Manusia("Gilang", 23)

try:
    print(manusia.alamat)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")

try:
    print(manusia.get_alamat())
except AttributeError:
    print("Objek tidak memiliki metode yang diminta!")