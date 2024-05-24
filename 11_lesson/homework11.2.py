from typing import Generator


def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    """
    Генерція числа кубів, починаючи від 2 до вказаної величини.
    """
    assert end >= 2, "End must be 2 or greater"

    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1


if __name__ == "__main__":
    from inspect import isgenerator

    gen = generate_cube_numbers(1)
    assert isgenerator(gen) == True, 'Test0'
    assert list(generate_cube_numbers(10)) == [8], 'Test1'
    assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test2'
    assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], 'Test3'
    print('Ok')
