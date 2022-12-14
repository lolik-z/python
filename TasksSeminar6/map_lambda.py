#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
#в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
#Пример:
#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21
import math

def calc(op, x1, y1, x2, y2):
    return op(x1, y1, x2, y2)

# coords1 = input('Введите координаты первой точки через пробел: ')
# coords1 = coords1.split(' ')
# coords2 = input('Введите координаты второй точки через пробел: ')
# coords2 = coords2.split(' ')
try:
    ###### map ######
    coords1 = list(map(int, input('Введите координаты первой точки через пробел: ').split()))
    coords2 = list(map(int, input('Введите координаты второй точки через пробел: ').split()))
    print(coords1, coords2)
    # s = math.sqrt((int(coords2[0])-int(coords1[0]))**2 + (int(coords2[1])-int(coords1[1]))**2)
    ###### lambda ######
    s = calc(lambda x1, y1, x2, y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2), int(coords1[0]), int(coords1[1]),
             int(coords2[0]), int(coords2[1]))
    s = str(s)
    s = s.split('.')
    print(f'A ({coords1[0]},{coords1[1]}); B ({coords2[0]},{coords2[1]}) -> {s[0]}.{s[1][0:2]}')
except:
    print('Введены некорректные координаты')
    print()