class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi
    
    @classmethod
    def define_calculator(cls, calc_type):
        if calc_type == "volume":
            cls.hitung_volume = lambda self: self.sisi ** 3
        elif calc_type == "luas_permukaan":
            cls.hitung_luas_permukaan = lambda self: 6 * self.sisi ** 2

Kubus.define_calculator("volume")
Kubus.define_calculator("luas_permukaan")

kubus = Kubus(3)
print(f"Volume kubus: {kubus.hitung_volume()}") # Output: Volume kubus: 27
print(f"Luas permukaan kubus: {kubus.hitung_luas_permukaan()}") # Output: Luas permukaan kubus: 54
