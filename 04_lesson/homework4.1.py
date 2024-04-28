#Переміщення нулів у кінець списку
input_list = [0, 1, 0, 12, 3]
input_list.sort(key=lambda x: (x == 0, x))
print(input_list) #Виведе [1, 3, 12, 0, 0]
