class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        
    def luas(self):
        return 3.14 * (self.jari_jari **4)
lingkaranA = Lingkaran(7)
print(f"luas lingkaran: {lingkaranA.luas()}") 