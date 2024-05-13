def common_elements():
    multiples_of_3 = [num for num in range(0, 100) if num % 3 == 0]
    multiples_of_5 = [num for num in range(0, 100) if num % 5 == 0]
    set_multiples_of_3 = set(multiples_of_3)
    set_multiples_of_5 = set(multiples_of_5)
    common_elements_set = set_multiples_of_3.intersection(set_multiples_of_5)
    return common_elements_set
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
