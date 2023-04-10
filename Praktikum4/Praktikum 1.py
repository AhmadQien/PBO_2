class Peneliti:
    def __init__(self, nama, institusi):
        self.nama = nama
        self.institusi = institusi
        self.jurnal = None
    
    def hasil_penelitian(self, judul, isi):
        self.jurnal = Jurnal(judul, isi)
    
    def lihat_jurnal(self):
        if self.jurnal:
            print(f"Jurnal: {self.jurnal.judul}")
            print(f"Isi: {self.jurnal.isi}")
        else:
            print("Belum ada jurnal yang dihasilkan.")
        

class Jurnal:
    def __init__(self, judul, isi):
        self.judul = judul
        self.isi = isi

# membuat objek peneliti
peneliti1 = Peneliti("Usrop", "Universitas MC")

# melakukan penelitian dan menghasilkan jurnal
peneliti1.hasil_penelitian("Aku Tak Tau", "bukan berarti bodoh.")

# melihat jurnal yang dihasilkan
peneliti1.lihat_jurnal()

# membuat objek peneliti lain
peneliti2 = Peneliti("Ucok", "Universitas FMC")

# melihat jurnal yang dihasilkan (belum ada)
peneliti2.lihat_jurnal()

# melakukan penelitian dan menghasilkan jurnal
peneliti2.hasil_penelitian("satu tambah satu", "bukan berarti 2.")

# melihat jurnal yang dihasilkan
peneliti2.lihat_jurnal()
