def is_even(number: int) -> bool:
    """
    Перевірка чи є число парним без використання ділення.
    """
    return (number & 1) == 0


if __name__ == "__main__":
    assert is_even(2494563894038**2) == True, 'Test1'
    assert is_even(1056897**2) == False, 'Test2'
    assert is_even(24945638940387**3) == False, 'Test3'
    print('Ok')