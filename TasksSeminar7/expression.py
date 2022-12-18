# list = [23, '+', 23, '*',23, '+',23, '+',333]
# print(list)
def calc_expression(list):
    result = 0
    while len(list) != 1:
        i = 0
        while ('*' in list or '/' in list) and i < len(list):
            if list[i] == '*':
                result = list[i-1] * int(list[i+1])
                list.pop(i)
                list.pop(i)
                list[i-1] = result
                i -= 1
            elif list[i] == '/':
                result = list[i-1] / int(list[i+1])
                list.pop(i)
                list.pop(i)
                list[i-1] = result
                i -= 1
            i += 1

        while ('+' in list or '-' in list) and i < len(list):
            if list[i] == '+':
                result = list[i - 1] + int(list[i + 1])
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i -= 1
            elif list[i] == '-':
                result = list[i - 1] - int(list[i + 1])
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i -= 1
            i += 1
    return result

# list = calc_expression(list)
# print(list)