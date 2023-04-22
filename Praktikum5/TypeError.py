def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

numbers = [10, 20, "30", 40, 50]
try:
    average = calculate_average(numbers)
except TypeError:
    print("Terjadi kesalahan tipe data, pastikan semua elemen dalam list adalah angka!")