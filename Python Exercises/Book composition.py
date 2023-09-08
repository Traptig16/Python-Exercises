class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")
        print(f"Nationality: {self.author.nationality}")

author1 = Author('Valmiki ji', "Indian")
book1 = Book("Ramayan", author1)
book1.details()
