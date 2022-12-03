# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
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
if len(my_list)%2 == 0:
    for i in range(int(len(my_list)/2)):
       new_list.append(my_list[i]*my_list[len(my_list)-1-i])
else:
    for i in range(int(len(my_list)/2)):
       new_list.append(my_list[i]*my_list[len(my_list)-1-i])
    new_list.append(my_list[int(len(my_list)/2)]**2)
print(f'{my_list} => {new_list}')