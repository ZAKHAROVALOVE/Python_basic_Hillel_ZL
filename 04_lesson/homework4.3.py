#Створення нового списоку з 3 елементів:
#перший, третій з початку і другий з кінця випадкового списку чисел
import random

random_count = random.randint(3, 10)
random_list = [random.randint(1, 10) for _ in range(random_count)]
print("Випадковий список чисел від 3 до 10:", random_list)

new_list = [random_list[0], random_list[2], random_list[-2]]
print("Новий список:", new_list)
#Виведе: Випадковий список чисел від 3 до 10: [5, 9, 3, 7, 9]
#Новий список: [5, 3, 7]