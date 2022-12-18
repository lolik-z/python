# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
import random

my_list = [random.randint(0,30) for _ in range(10)]

print(my_list)
new_list = []
for i in range(len(my_list)):
    result = []
    max = my_list[i]
    result.append(my_list[i])
    for j in range(i+1, len(my_list)):
        if my_list[j] > max:
            result.append((my_list[j]))
            max = my_list[j]
    if len(result) > 1:
        new_list.append(result)
max = []
for i in new_list:
    if len(i) > len(max):
        max = i

print(new_list)
print(len(max))