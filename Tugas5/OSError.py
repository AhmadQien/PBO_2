import os
try:
    with open("file.txt") as file:
        data = file.read()
except OSError as e:
    print(e) 
    