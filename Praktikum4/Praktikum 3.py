class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        
    def tulis_buku(self, judul, tahun_terbit):
        buku = Buku(judul, tahun_terbit, self)
        self.daftar_buku.append(buku)
        return buku
        
    def lihat_daftar_buku(self):
        print(f"Daftar buku yang ditulis oleh {self.nama}:")
        if self.daftar_buku:
            for buku in self.daftar_buku:
                print(f"- {buku.judul} ({buku.tahun_terbit})")
        else:
            print("Belum menulis buku.")
        
        
class Buku:
    def __init__(self, judul, tahun_terbit, penulis):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penulis = penulis

# membuat objek penulis
penulis1 = Penulis("Usrop Markup")

# menulis buku
buku1 = penulis1.tulis_buku("Munir", 1999)
buku2 = penulis1.tulis_buku("Novan Si", 2010)

# lihat daftar buku
penulis1.lihat_daftar_buku()