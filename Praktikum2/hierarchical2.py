class Bentuk:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
    def get_nama(self):
        return self.nama
    def get_warna(self):
        return self.warna
class DuaDimensi(Bentuk):
    def __init__(self, nama, warna, sisi):
        super().__init__(nama, warna)
        self.sisi = sisi
    def get_sisi(self):
        return self.sisi
class TigaDimensi(Bentuk):
    def __init__(self, nama, warna, rupa):
        super().__init__(nama, warna)
        self.rupa = rupa
    def get_rupa(self):
        return self.rupa
# Hierarchical Inheritance
class Bola(TigaDimensi):
    def __init__(self, name, warna, rupa, radius):
        super().__init__(name, warna, rupa)
        self.radius = radius
    def get_radius(self):
        return self.radius