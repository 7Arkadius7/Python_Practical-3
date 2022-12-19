# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = [1.1, 1.2, 3.1, 5, 10.01]

new_list = [i % 1 for i in list if isinstance(i, float)]
print(new_list)

print(round(max(new_list)-min(new_list),2))