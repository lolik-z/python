#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

namberQu = input('Введите номер четверти: ')
namberQu = int(namberQu)
if namberQu == 1:
    print(f'1 -> x>0, y>0')
elif namberQu == 2:
    print(f'2 -> x<0, y>0')
elif namberQu == 3:
    print(f'3 -> x<0, y<0')
elif namberQu == 4:
    print(f'4 -> x>0, y<0')
else:
    print('Введен некорректный номер четверти')