# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import sys
sys.path.append('../')
import Functions4 as F

while True:
   try:
      size = int(input('Введите максимальную степень первого многочлена: '))
      break
   except:
      print('Ошибка! Требуется ввести натуральное число!')
equ1 = F.EquationRandom(size)
f = open('text1.txt', 'w')
f.write(equ1)
f.close()

while True:
   try:
      size = int(input('Введите максимальную степень второго многочлена: '))
      break
   except:
      print('Ошибка! Требуется ввести натуральное число!')
equ2 = F.EquationRandom(size)
f = open('text2.txt', 'w')
f.write(equ2)
f.close()
#Записали в 2 файла многочлены

dict1 = F.EquationRead('text1.txt')
dict2 = F.EquationRead('text2.txt')   # Многочлены из файлов преобразовала в словари
a = (dict1, dict2)
resultdict = {}                                         #  результирующий словарь
for dictionary in a:                                    # пробегаем по списку словарей
  for key in dictionary:                                # пробегаем по ключам словаря
    try:
      resultdict[key] += int(dictionary[key])           # складываем значения
    except KeyError:                                    # если ключа еще нет - создаем
      resultdict[key] = int(dictionary[key])
print(equ1)
print(equ2)
print('Сумма:')
print(F.Equation(resultdict))                           # преобразуем словарь в многочлен
