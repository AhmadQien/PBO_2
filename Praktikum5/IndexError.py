list_angka = [1, 2, 3]

def get_value(index):
    if index >= len(list_angka):
        raise IndexError("Index {} melebihi jumlah elemen dalam list!".format(index))
    return list_angka[index]

try:
    value = get_value(4)
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")