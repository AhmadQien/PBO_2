class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def menyanyi(self):
        print(f"{self.nama} sedang menyanyi.")

class Mahasiswa(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip

    def menari(self):
        print(f"{self.nama} dengan NIM {self.nip} sedang menari.")

dosenA = Mahasiswa("Rahman", 32, "123456")
dosenA.menyanyi() # Output: Rahman sedang menyanyi.
dosenA.menari() # Output: Rahman dengan NIM 123456 sedang menari.