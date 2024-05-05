def multiply_digits(number):
    result = 1
    for digit in str(number):
        result *= int(digit)
    return result
user_input = int(input("Введіть число: "))
while user_input > 9:
    user_input = multiply_digits(user_input)
print("Результат:", user_input)