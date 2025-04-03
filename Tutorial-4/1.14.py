class Mobile:
    def _init_(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        return f"Company: {self.company}, Model: {self.model}, Price: {self.price}"

mobile = Mobile("Samsung", "S21", 1000)
print(mobile.display_details())
