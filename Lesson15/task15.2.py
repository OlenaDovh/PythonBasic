"""
Створіть клас «Правильний дріб»
та реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів цього класу.
"""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __add__(self, other):
        denom = self.denominator
        numer1 = self.numerator
        numer2 = other.numerator
        if self.denominator != other.denominator:
            denom = self.denominator  * other.denominator
            numer1 *= other.denominator
            numer2 *= self.denominator
        return Fraction(numer1 + numer2, denom)

    def __sub__(self, other):
        denom = self.denominator
        numer1 = self.numerator
        numer2 = other.numerator
        if self.denominator != other.denominator:
            denom = self.denominator * other.denominator
            numer1 *= other.denominator
            numer2 *= self.denominator
        return Fraction(numer1 - numer2, denom)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __str__(self):
        return f"Fraction: {self.numerator}, {self.denominator}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
print(f_d)
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
print(f_e)
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')