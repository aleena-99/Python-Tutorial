class Rectangle:
    def _init_(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

rectangle = Rectangle(5, 4, 0, 0)
print(rectangle.area())
print(rectangle.perimeter())
