class Hewan:
    def __init__(self, nama):
        self.nama =  nama
    def suara(self):
        print("Suara Hewan")
class Kucing(Hewan):
    def __init__(self, nama, keturunan):
        super().__init__(nama)
        self.keturunan = keturunan
    def suara(self):
        print("Meow")
class Persia(Kucing):
    def __init__(self, nama, keturunan, asal):
        super().__init__(nama, keturunan)
        self.asal = asal
    def suara(self):
        print("kucing mengeong")

persia = Persia ("Meow", "Persia", "US")
persia.suara()