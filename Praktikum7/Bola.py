class Bola:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    @classmethod
    def define_calculator(cls, calc_type):
        if calc_type == "volume":
            cls.hitung_volume = lambda self: 4/3 * 3.14 * self.jari_jari ** 3
        elif calc_type == "luas_permukaan":
            cls.hitung_luas_permukaan = lambda self: 4 * 3.14 * self.jari_jari ** 2

Bola.define_calculator("volume")
Bola.define_calculator("luas_permukaan")

bola = Bola(4)
print(f"Volume bola: {bola.hitung_volume()}") # Output: Volume bola: 267.94666666666666
print(f"Luas permukaan bola: {bola.hitung_luas_permukaan()}") # Output: Luas permukaan bola: 201.6