class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "bergerak")

class Anjing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)

        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Guk Guk!")

anjingA = Anjing("Doggy", 4, "Pitbull")
anjingA.bergerak() # output: Doggy bergerak
anjingA.bersuara() # output: Guk Guk!