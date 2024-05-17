def is_even(digit: int) -> bool:
    """ Перевіка чи є число парним. """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

if __name__ == "__main__":
    print(is_even(2))
    print(is_even(5))
    print(is_even(0))