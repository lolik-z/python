# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
while True:
   try:
      n = int(input('Введите число элементов в списке N: '))
      break
   except:
      print('Ошибка! Требуется ввести целое число!')
my_list = []
for i in range(n):
    my_list.append(randint(0, 10))
new_list = []
sum = 0
for i in range(1, len(my_list), 2):
   a = my_list[i]
   sum+=a
   new_list.append(str(a))
print1 = ','.join(new_list)
print(f'{my_list} -> на нечётных позициях элементы {print1}, ответ: {sum}')
