# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import sys
sys.path.append('../')
import Functions4 as F

while True:
   try:
      size = int(input('Введите максимальную степень: '))
      break
   except:
      print('Ошибка! Требуется ввести натуральное число!')

equ = F.EquationRandom(size)

# print(equ)
f = open('text.txt', 'w')
f.write(equ)
f.close()