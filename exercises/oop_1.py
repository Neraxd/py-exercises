# Create a class Book with attributes: title, author, year.
# Create two book objects and print their details.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print_info(self):
        print(f"name : {self.title}\nauthor : {self.author}\n year: {self.year}\n")


book1 = Book("python programming langauge", "Jack Mcnaughty", 2001)
book2 = Book("go programming langauge", "Jack NotMcnaughty", 2012)


book1.print_info()
Book.print_info(book2)
