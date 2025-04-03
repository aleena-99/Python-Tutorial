class Student:
    def _init_(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def computeTotal(self):
        return self.mark1 + self.mark2

    def printDetails(self):
        return f"Roll No: {self.rollno}, Total Marks: {self.computeTotal()}"

student = Student(101, 85, 90)
print(student.printDetails())
