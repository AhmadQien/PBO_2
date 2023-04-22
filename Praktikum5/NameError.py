try:
    nama = "Gilang"
    print(nama)
except NameError:
    print("Variabel yang diminta belum didefinisikan!")
    
try:
    print(nama)
except NameError:
    print("Variabel yang diminta belum didefinisikan!")