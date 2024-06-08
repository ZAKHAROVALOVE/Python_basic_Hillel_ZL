class Fraction:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        numerator = self.a * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other: 'Fraction') -> bool:
        return (self.a * other.b) == (other.a * self.b)

    def __gt__(self, other: 'Fraction') -> bool:
        return (self.a * other.b) > (other.a * self.b)

    def __lt__(self, other: 'Fraction') -> bool:
        return (self.a * other.b) < (other.a * self.b)

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"

if __name__ == "__main__":
    f_a = Fraction(2, 3)
    f_b = Fraction(3, 6)
    f_c = f_b + f_a
    assert str(f_c) == 'Fraction: 21, 18'
    f_d = f_b * f_a
    assert str(f_d) == 'Fraction: 6, 18'
    f_e = f_a - f_b
    assert str(f_e) == 'Fraction: 3, 18'

    assert f_d < f_c  # True
    assert f_d > f_e  # True
    assert f_a != f_b  # True
    f_1 = Fraction(2, 4)
    f_2 = Fraction(3, 6)
    assert f_1 == f_2  # True
    print('OK')
