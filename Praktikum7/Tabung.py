class Tabung:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    @classmethod
    def define_calculator(cls, calc_type):
        if calc_type == "volume":
            cls.hitung_volume = lambda self: 3.14 * self.jari_jari ** 2 * self.tinggi
        elif calc_type == "luas_permukaan":
            cls.hitung_luas_permukaan = lambda self: 2 * 3.14 * self.jari_jari * (self.jari_jari + self.tinggi)

Tabung.define_calculator("volume")
Tabung.define_calculator("luas_permukaan")

tabung = Tabung(2, 5)
print(f"Volume tabung: {tabung.hitung_volume()}") # Output: Volume tabung: 62.8
print(f"Luas permukaan tabung: {tabung.hitung_luas_permukaan()}") # Output: Luas permukaan tabung: 94.2