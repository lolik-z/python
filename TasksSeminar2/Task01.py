# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


namber = input('Введите число: ')
sumNumber = 0
try:
    for i in namber:
        if i != '.' and i != ',':

                sumNumber = sumNumber + int(i)
    print(f'{namber} -> {sumNumber}')
except:
    print('Ошибка! Требовалось ввести число!')