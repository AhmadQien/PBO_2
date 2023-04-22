def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    print(factorial(10000))
except RecursionError:
    print("Terjadi kesalahan rekursi, maksimum kedalaman rekursi tercapai!")