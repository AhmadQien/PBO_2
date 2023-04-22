try:
    nama = input("Masukkan nama: ")
    umur = int(input("Masukkan umur: "))
except EOFError:
    print("Tidak ada input yang diberikan!")