while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        operation = input("Введіть операцію (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Помилка: ділення на нуль!")
            result = num1 / num2
        else:
            print("Неправильна операція!")
            continue

        print("Результат:", result)

    except ValueError:
        print("Будь ласка, введіть числа.")
    except ZeroDivisionError as error:
        print(error)

    choice = input("Бажаєте продовжити роботу? (y/n): ")
    if choice.lower() != 'y':
        break