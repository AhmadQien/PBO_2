import pygame

class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Suara Kucing.mp3"

class Anjing(Hewan):
    def suara(self):
        return "Suara Anjing.mp3"

class Kelelawar(Hewan):
    def suara(self):
        return "Suara Kelelawar.mp3"

class Burung(Hewan):
    def suara(self):
        return "Suara Burung.mp3"

class Kambing(Hewan):
    def suara(self):
        return "Suara Kambing.mp3"

class Gajah(Hewan):
    def suara(self):
        return "Suara Gajah.mp3"

class Kuda(Hewan):
    def suara(self):
        return "Suara Kuda.mp3"

class Sapi(Hewan):
    def suara(self):
        return "Suara Sapi.mp3"

class Singa(Hewan):
    def suara(self):
        return "Suara Singa.mp3"

# Membuat objek dari setiap kelas
hewan1 = Kucing()
hewan2 = Anjing()
hewan3 = Kelelawar()
hewan4 = Burung()
hewan5 = Kambing()
hewan6 = Gajah()
hewan7 = Kuda()
hewan8 = Sapi()
hewan9 = Singa()

# Inisialisasi Pygame mixer
pygame.mixer.init()

# Memanggil metode suara() dan memutar file MP3-nya
for hewan in [hewan1, hewan2, hewan3, hewan4, hewan5, hewan6, hewan7, hewan8, hewan9]:
    suara_file = hewan.suara()
    pygame.mixer.music.load(suara_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
