class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 4)
print(rect.area())
