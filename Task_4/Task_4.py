# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)

a = ""
n = int(input("Пожалуйста, введите число: "))
print()
while n != 0:
    a = str(n%2) + a
    n //=2
print(a)