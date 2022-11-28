# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.
while True:
   try:
      n = int(input('Введите число элементов в списке N : '))
      break
   except:
      print('Ошибка! Требуется ввести целое число!')
my_list = []
sumList = 0
for i in range(1, n+1):
   my_list.append(round((1+1/i)**i, 3))
   sumList +=(1+1/i)**i
print(f'{my_list}, сумма элементов {round(sumList, 3)}')

