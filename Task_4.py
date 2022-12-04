# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input("Введите число: "))
print()
a = list()
while number > 0:
    a.append(number % 2) 
    number = int(number / 2)
for x in reversed(a):
    print(x, end = '')