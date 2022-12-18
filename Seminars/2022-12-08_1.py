# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
ounput_list = []
# count = 0
# for i in range(len(input_list)):
#     if input_list.count(input_list[i]) == 1:
#         ounput_list.append(input_list[i])
# print(ounput_list)

my_dict = {}
for key in my_list:
    value = my_dict.get(key, 0) + 1
    my_dict[key] = value

new_list = []
for key, value in my_dict.items():
    if value == 1:
        new_list.append(key)
print(f'{my_list} - > {new_list}')
