# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input("Введите число: "))
ls = list()
ls1 = list()
ls.append(0)
ls.append(1)
i = 2 
while i <= number:
    ls.append(-(ls[i - 1]) + ls[i - 2])
    i += 1
for j in reversed(ls):
    ls1.append(j)
K = 1
while K <= number:
    ls1.append(ls1[i - 1] + ls1[i - 2])
    K += 1
    i += 1
for i in ls1:
    print(i, end = ', ')
    
