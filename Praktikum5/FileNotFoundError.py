try:
    with open("AhmadQien.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File tidak ditemukan!")