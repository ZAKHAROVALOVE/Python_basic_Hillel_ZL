from typing import Union

def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    Знаходження різниці між найбільшим (максимум) і найменшим (мінімум) елементом
    Input: Змінна кількість аргументів як числа (int, float).
    Output:  Різниця між максимумом і мінімумом як число (int, float).
    """
    if not args:
        return 0
    max_value = max(args)
    min_value = min(args)
    return round(max_value - min_value, 2)


if __name__ == "__main__":
    assert difference(1, 2, 3) == 2, 'Test1'
    assert difference(5, -5) == 10, 'Test2'
    assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
    assert difference() == 0, 'Test4'
    print('OK')
