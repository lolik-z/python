# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
from random import randint

my_list = ['rtet', 'rertrt', '3', 'rt', 'wetret']
print(my_list)
for i in range(len(my_list)):
    j = randint(0, len(my_list)-1)
    temp_lst = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp_lst
print(my_list)
