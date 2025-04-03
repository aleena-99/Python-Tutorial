class Complex:
    def _init_(self, real, imag):
        self.real = real
        self.imag = imag

    def _add_(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def _str_(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(1, 4)
c3 = c1 + c2

print(c3)
