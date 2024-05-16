def add_one(some_list: list) -> list:
    """
    Increment the number represented by a list of digits by one.

    Args:
        some_list: A list of integers representing digits of a number.

    Returns:
        A list of integers representing digits of the incremented number.
    """
    num = int(''.join(map(str, some_list))) + 1
    result_list = [int(digit) for digit in str(num)]
    return result_list


if __name__ == "__main__":
    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
    assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
    assert add_one([0]) == [1], 'Test3'
    assert add_one([9]) == [1, 0], 'Test4'
    print("ОК")