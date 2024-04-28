#Обчислення суми елементів із парними індексами [0-й, 2-й, 4-й ітд]
#Перемноження цієї суми на останній елемент вхідного масиву. Якщо масив порожній, повертається 0.
def multiply_sum_even_indices_last_element(arr):
    return sum(arr[::2]) * arr[-1] if arr else 0
print(multiply_sum_even_indices_last_element([0, 1, 7, 2, 4, 8])) # Виведе 88
print(multiply_sum_even_indices_last_element([1, 3, 5])) # Виведе 30
print(multiply_sum_even_indices_last_element([6])) # Виведе 36
print(multiply_sum_even_indices_last_element([])) # Виведе 0