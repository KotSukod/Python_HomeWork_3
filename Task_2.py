# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

numbers = [1,2,3,4,5]
i = 0
k = len(numbers) - 1
result = list()
while i <= k:
    result.append(numbers[i] * numbers[k])
    print(result)
    i += 1
    k -= 1