import string, random


class Person:
    borrow_limit = 5

    def __init__(self, name):
        self._name = name
        self._unique_id = "".join(random.sample(string.digits, k=5))

    def represention(self):
        print(f"Name : {self._name}\nUnique ID : {self._unique_id}")


class Member(Person):
    number_of_books_borrowed = 0

    def __init__(self, name):
        super().__init__(name)
        self.__books = []

    def borrow_book(self, book):
        if book.is_available and Member.number_of_books_borrowed <= Member.borrow_limit:
            self.__books.append(book)
            Member.number_of_books_borrowed += 1
            book.is_available = False
        else:
            print("You are not allowed to borrow this book")

    def return_book(self, book):
        self.__books.remove(book)
        book.is_available = True


class Librarian(Person):

    def __init__(self, name):
        super().__init__(name)
        self.__employee_id = "EP" + "".join(random.sample(string.digits, k=10))

    def add_book_into_library(self, book, library):
        library.add_book(book)

    def remove_book_from_library(self, book, library):
        library.remove_book(book)


class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__unique_id = "BK" + "".join(random.sample(string.digits, k=10))
        self._is_available = True

    def mark_as_borrowd(self):
        if self._is_available:
            print(
                "The book has been returned to the library (or it was here at the first point)! "
            )
        elif self._is_available == False:
            print("the book has been borrowed by someone!")

    def represention(self):
        print(
            f"title : {self.__title}\nauthor : {self.__author}\n ID : {self.__unique_id}"
        )

    @property
    def is_available(self):
        return self._is_available

    @property
    def unique_id(self):
        return self.__unique_id

    @property
    def title(self):
        return self.__title


class Library:
    book_counter = 0

    def __init__(self):
        self.__all_books = []
        self.__all_members = []

    def add_book(self, book):
        if book in self.__all_books:
            print("book is already there!")
        else:
            self.__all_books.append(book)
            Library.book_counter += 1

    def remove_book(self, book):
        if book in self.__all_books:
            self.__all_books.remove(book)
            book_counter -= 1
        else:
            print("not found!")

    def register_member(self, member):
        if member in self.__all_members:
            print("member is already here ! ")
        else:
            self.__all_members.append(member)

    def find_book(self, key):
        for book in self.__all_books:
            if book.title == key or book.unique_id == key:
                print(f"{book.title} by {book.unique_id} found!")

    def list_books(self):
        if len(self.__all_books) < 1:
            print("no book yet! ")
        else:
            for num, book in enumerate(self.__all_books, 1):
                print(f"{num}. {book.title} ({book.unique_id}) found!\n")

    @staticmethod
    def rules_of_library():
        print(f"1. No eating , Drinking\n2. No stealing lol")


lib1 = Library()
lib1.rules_of_library()
book1 = Book("12 years a salve", "adam driver")
librarian1 = Librarian("ahmed")
librarian1.add_book_into_library(book1, lib1)
lib1.list_books()
