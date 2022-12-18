# s = '24+145* 56'
def pars_str_ex(s):
    i = 0
    ex = []
    s = s.replace(' ', '')
    while i < len(s):
        arg = ''
        while True:
            if i < len(s):
                if s[i] in '1234567890':
                    arg = arg + s[i]
                    i += 1
                else:
                    break
            else:
                break
        ex.append(arg)
        if i < len(s):
            if s[i] not in '+-/*' and i < len(s):
                raise ValueError
            else:
                ex.append(s[i])
                i += 1
        else:
            break
    for i in range(len(ex)):
        if ex[i].isdigit():
            ex[i] = int(ex[i])
    return ex
# st = pars_str_ex(s)

def pars_str_ex_print(s):
    str = ''
    for i in range(len(s)):
        str = f'{str}{s[i]} '
    str = str +'='
    return str

# print(pars_str_ex(s))
# print(pars_str_ex_print(st))