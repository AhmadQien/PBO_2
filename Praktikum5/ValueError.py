try:
    angka = int("123.45")
except ValueError:
    print("Terjadi kesalahan konversi nilai ke dalam tipe data yang diinginkan!")
    
try:
    angka = int("123abc")
except ValueError:
    print("Terjadi kesalahan konversi nilai ke dalam tipe data yang diinginkan!")