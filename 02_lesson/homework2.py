x = input("Please input some integer: ") # Нехай користувач надрукував 12345

# Конвертація введеного значення у ціле число
y = int(x)

# Виведення у зворотньому порядку кожної цифри числа у вигляді рядка. Виведе 54321
print("Result:", (y % 10) * 10000 + (y // 10 % 10) * 1000 + (y // 100 % 10) * 100 + (y // 1000 % 10) * 10 + (y // 10000))