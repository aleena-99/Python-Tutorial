class Person:
    def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

person1 = Person("John", 30, 50000)
person2 = Person("Emma", 28, 60000)

print(person1.display())
print(person2.display())
