try:
    hasil = 0.1 + 0.2
    print(hasil)
    hasil = 1.0 / 0.0
    print(hasil)
except ZeroDivisionError:
    print("Tidak dapat melakukan pembagian dengan nol!")
except OverflowError:
    print("Hasil operasi terlalu besar untuk direpresentasikan sebagai bilangan desimal!")
except FloatingPointError:
    print("Terjadi kesalahan pada operasi bilangan desimal!")

    