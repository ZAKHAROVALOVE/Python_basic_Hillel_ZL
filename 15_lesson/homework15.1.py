class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> int:
        return self.width * self.height

    def __eq__(self, other: 'Rectangle') -> bool:
        return self.get_square() == other.get_square()

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __mul__(self, n: float) -> 'Rectangle':
        new_width = int(self.width * n ** 0.5)
        new_height = int(self.height * n ** 0.5)
        return Rectangle(new_width, new_height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def area(self) -> int:
        return self.width * self.height

if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)

    assert r1.get_square() == 8, 'Test 1 Failed'
    assert r2.get_square() == 18, 'Test 2 Failed'

    r3 = r1 + r2
    assert r3.get_square() == (2+3) * (4+6), 'Test 3 Failed'

    r4 = r1 * 4
    assert r4.get_square() == 2 * 4 * 4, 'Test 4 Failed'

    assert r2 == Rectangle(3, 6), 'Test 5 Failed'

    print("All tests passed successfully!")

