#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

len_list = int(input('Пожалуйста, введите размер списка'))
list = []

[list.append(int(input(f'Пожалуйста, введите значение элемента [{i}]: '))) for i in range(len_list)]
print(list)

final_list = []
for i in range(len_list//2):
    final_list.append(list[i]*list[-1-i])
if len_list%2==1:
    final_list.append(list[len_list//2]**2)

print(final_list)