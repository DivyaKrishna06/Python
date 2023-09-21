class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return ComplexNumber(real_diff, imag_diff)

    def __mul__(self, other):
        real_prod = self.real * other.real - self.imag * other.imag
        imag_prod = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_prod, imag_prod)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

# Create some complex numbers
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

# Test operator overloading
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c1 + c2 = {c3}")
print(f"c1 - c2 = {c4}")
print(f"c1 * c2 = {c5}")
print(f"c1 == c2: {c1 == c2}")
print(f"c1 != c2: {c1 != c2}")