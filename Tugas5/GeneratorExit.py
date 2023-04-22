def generator():
    try:
        for i in range(5):
            yield i
    except GeneratorExit:
        print("Generator telah dihentikan dengan panggilan close()!")
    finally:
        print("Generator selesai dijalankan.")

gen = generator()
for i in gen:
    print(i)
    if i == 2:
        gen.close()