class Car:
    def _init_(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        return self.price

car1 = Car("Toyota", 2022, 20000)
car2 = Car("Honda", 2023, 22000)

print(car1.cost())
print(car2.cost())
