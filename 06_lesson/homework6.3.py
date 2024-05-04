def multiply_digits(n):
    return eval('*'.join(str(n)))
user_input = int(input("Введіть число: "))
while user_input > 9:
    user_input = multiply_digits(user_input)
print("Результат:", user_input)