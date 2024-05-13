def common_elements():
    multiples_of_3 = [num for num in range(1, 101) if num % 3 == 0]
    multiples_of_5 = [num for num in range(1, 101) if num % 5 == 0]
    common_elements_set = set(multiples_of_3).intersection(set(multiples_of_5))
    print("Числа кратні 3:", multiples_of_3)
    print("Числа кратні 5:", multiples_of_5)
    print("Перетин чисел:", common_elements_set)
    pass
common_elements()
