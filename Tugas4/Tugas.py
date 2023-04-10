class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Manga:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.chapters = []
    
    def add_chapter(self, chapter):
        self.chapters.append(chapter)
    
    def get_info(self):
        print(f"Manga Title: {self.title}")
        print(f"Author: {self.author.name}")
        print(f"Email: {self.author.email}")
        print(f"Chapters: {len(self.chapters)}")

class Chapter:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def get_info(self):
        print(f"Chapter Title: {self.title}")
        print(f"Pages: {self.pages}")

# membuat objek author
author1 = Author("Ucok Saipudin", "Ucok.udin@gmail.com")

# membuat objek manga
manga1 = Manga("Pemburu Koruptor", author1)

# membuat objek chapter
chapter1 = Chapter("Chapter 1: Intro", 45)
chapter2 = Chapter("Chapter 10: List", 30)

# menambahkan chapter ke dalam manga
manga1.add_chapter(chapter1)
manga1.add_chapter(chapter2)

# menampilkan informasi manga
manga1.get_info()

# menampilkan informasi chapter
chapter1.get_info()