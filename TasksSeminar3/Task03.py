# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import sys
sys.path.append('../')
import Functions as F

my_list = [1.1, 1.2, 3.1, 50, 10.01]
my_list1 = []
for i in range(len(my_list)):
    if my_list[i]%10 != 0:
        my_list1.append(float('0.'+ str(my_list[i]).split('.')[1]))

result = F.MaxList(my_list1) - F.MinList(my_list1)
print(f'{my_list}  => {F.MaxList(my_list1)} - {F.MinList(my_list1)} = {result}')