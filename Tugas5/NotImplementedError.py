class Animal:
    def make_sound(self):
        raise NotImplementedError("Metode make_sound belum diimplementasikan!")

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    pass

my_cat = Cat()
my_dog = Dog()

print(my_cat.make_sound())  # Output: Meow

try:
    print(my_dog.make_sound())
except NotImplementedError as e:
    print(e)  # Output: Metode make_sound belum diimplementasikan!
