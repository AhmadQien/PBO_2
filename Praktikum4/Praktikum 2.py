class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
    
    def bergabung_kelompok(self, kelompok):
        self.kelompok = kelompok
        kelompok.tambah_anggota(self)
    
    def keluar_kelompok(self):
        if self.kelompok:
            self.kelompok.hapus_anggota(self)
            self.kelompok = None
        else:
            print("Anda belum bergabung ke kelompok.")
        

class KelompokKKM:
    def __init__(self, nomor):
        self.nomor = nomor
        self.anggota = []
    
    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)
    
    def hapus_anggota(self, mahasiswa):
        if mahasiswa in self.anggota:
            self.anggota.remove(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan di kelompok ini.")
    
    def lihat_anggota(self):
        print(f"Anggota kelompok {self.nomor}:")
        for mahasiswa in self.anggota:
            print(f"- {mahasiswa.nama} ({mahasiswa.nim})")

# membuat objek mahasiswa
mhs1 = Mahasiswa("Usrop", "567")
mhs2 = Mahasiswa("Ucok", "789")

# membuat objek kelompok KKM
kelompok1 = KelompokKKM(1)

# bergabung ke kelompok
mhs1.bergabung_kelompok(kelompok1)
mhs2.bergabung_kelompok(kelompok1)

# lihat anggota kelompok
kelompok1.lihat_anggota()

# keluar dari kelompok
mhs1.keluar_kelompok()

# lihat anggota kelompok setelah ada yang keluar
kelompok1.lihat_anggota()