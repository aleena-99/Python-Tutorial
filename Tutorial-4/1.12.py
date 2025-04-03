class Student:
    def _init_(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def dataprint(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}"

student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

print(student1.dataprint())
print(student2.dataprint())
