import random
def EquationRandom(size):
    koef = {}
    for i in range(size + 1):
        koef[i] = random.randint(0, 100)
    equation = ''
    for i in range(size, -1, -1):
        if koef[i] != 0:
            if koef[i] == 1:
                if i == 1:
                    equation += f'x + '
                elif i == 0:
                    equation += f'1 '
                else:
                    equation += f'x**{i} + '
            else:
                if i == 1:
                    equation += f'{koef[i]}*x + '
                elif i == 0:
                    equation += f'{koef[i]} '
                else:
                    equation += f'{koef[i]}*x**{i} + '
    if koef[0] == 0:
        equation = equation[:-2]
    if equation != '':
        equation = equation + '= 0'
    return equation
def EquationRead(fileName):
    f = open(fileName, 'r')
    equation1 = f.read()
    f.close()
    equation1 = equation1.replace(' ', '')
    equation1 = equation1[:-2].split('+')
    equation1 = equation1[::-1]
    koef = {}
    a = 0
    j = 0
    for i in range(len(equation1)): # теперь надо пробегать по каждому члену и индекс коеффициента копить
       equation = equation1[i]
       if equation == 'x':
          koef[0 + a] = 0
          koef[1 + a] = 1
          j = 2
       elif len(equation.split('*')) == 1:
          koef[0 + a] = equation
          j = 1
       else:
          if len(equation.split('**')) == 1:
             koef[0 + a] = equation.split('*x')[0]
             j = 2
          elif len(equation.split('*x**')) == 2:
             k = a
             while k < int(equation.split('x**')[1]):
                koef[k] = 0
                k += 1
             koef[k] = equation.split('*x**')[0]
             j = k + 1
          else:
             k = a
             while k < int(equation.split('x**')[1]):
                koef[k] = 0
                k += 1
             koef[k] = 1
             j = k + 1
       a = j
    return koef
def Equation(dictionary):
    koef = dictionary
    equation = ''
    for i in reversed(koef):
       try:
            if koef[i] != 0:
                if koef[i] == 1:
                    if i == 1:
                        equation += f'x + '
                    elif i == 0:
                        equation += f'1 '
                    else:
                        equation += f'x**{i} + '
                else:
                    if i == 1:
                        equation += f'{koef[i]}*x + '
                    elif i == 0:
                        equation += f'{koef[i]} '
                    else:
                        equation += f'{koef[i]}*x**{i} + '
       except KeyError: print('Ошибка')
    if koef[0] == 0:
        equation = equation[:-2]
    if equation != '':
        equation = equation + '= 0'
    return equation