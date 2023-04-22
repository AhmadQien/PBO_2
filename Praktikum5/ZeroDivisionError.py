def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
    return a / b

try:
    x = 10
    y = divide(x, 0)
except ZeroDivisionError:
    print("Terjadi kesalahan pembagian dengan nol!")
    