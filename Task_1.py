# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

numbers = [0,9,8,7,6,5,4,3,2,1]
i = 0
sum = 0
while i < len(numbers):
    if i % 2 != 0:
        sum = sum + numbers[i]
    i += 1
print(sum)