import sys

try:
    x = sys.maxsize + 1
    print(x)
except OverflowError:
    print("Terjadi kesalahan overflow, angka terlalu besar untuk direpresentasikan!")
    