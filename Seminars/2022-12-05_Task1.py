# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

path = r'result.txt'  # r - строка рассматривается вместе со спецсимволами
with open(path, 'r', encoding='UTF-8') as data:
    string = data.readline()

string = string.split()
print(string)
string = list(map(int,string))
print(string)
for i in range(1, len(string)):
    if string[i] - 1 != string[i - 1]:
        print(string[i - 1] + 1)
        break