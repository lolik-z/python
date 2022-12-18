# 1. Напишите программу вычисления арифметического выражения заданного
# строкой.Используйте операции +, -, /, *.приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;
str1 = '1 - 2 * 3 ='
str1 = str1.replace(' ', '')
print(str1)
n = 0
i = 0
result = []
while i < range(len(str)):
    if str1[i] == '*':
        s = str(int(str1[i-1])*int(str1[i+1]))
        result[n] = result.append(s)
        n += 1
        i += 1
    elif str1[i] != '/':
        s = result.append(int(str1[i-1])/int(str1[i+1]))
        result[n] = result.append(s)
        n += 1
        i += 1
    else:
        result = result.append(str1[i])
        n += 1
        i += 1
print(result)
# for i in range(len(result)):
#     if result[i] != '+':
#         s = result.append(int(str[i - 1]) + int(str[i + 1]))
#     elif result[i] != '-':
#         s = result.append(int(str[i - 1]) + int(str[i + 1]))
#     else:
#         result1 = result1.append(result[i])
#
#
#
# my_dict = {}
# for key in result:
#     result = result.get(key, 0)
#     my_dict[key] = value


    # if str[i] == '*':
    #     n = i
    #     result.append(int(str[i-1])*int(str[i+1]))
# str1 = str.split('-')

print(n, result)