#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
#и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#x=34; y=-30 -> 4
#x=2; y=4 -> 1
#x=-34; y=-30 -> 3

coords = input('Введите координаты точки через пробел: ')
coords = coords.split(' ')
if int(coords[0])>0 and int(coords[1])>0:
    print(f'x={coords[0]}; y={coords[1]} -> 1')
elif int(coords[0])<0 and int(coords[1])>0:
    print(f'x={coords[0]}; y={coords[1]} -> 2')
elif int(coords[0])<0 and int(coords[1])<0:
    print(f'x={coords[0]}; y={coords[1]} -> 3')
elif int(coords[0])>0 and int(coords[1])<0:
    print(f'x={coords[0]}; y={coords[1]} -> 4')
else:
    print('Введены некорректные координаты')
