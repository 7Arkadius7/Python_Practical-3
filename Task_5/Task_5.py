# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).


n = int(input('Пожалуйста, введите длинну списка Фибоначи:'))

fib = [1,1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

fib_nego = [1,-1]
for i, elem in enumerate(fib,2):
    if i%2!=0:
        fib_nego.append(elem*(-1))
    else:
        fib_nego.append(elem)
   
fib_nego.reverse()
fib_nego.append(0)
print(fib_nego + fib)