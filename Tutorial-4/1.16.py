class Book:
    def _init_(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        return f"Title: {self.title}, Author: {self.author}, Cost: {self.cost}"

book = Book("Python Programming", "Guido van Rossum", 50)
print(book.print_details())
