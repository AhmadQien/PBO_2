dictionary = {"satu": 1, "dua": 2, "tiga": 3}

def get_value(key):
    if key not in dictionary:
        raise KeyError("Key {} tidak ditemukan pada dictionary!".format(key))
    return dictionary[key]

try:
    value = get_value("empat")
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")