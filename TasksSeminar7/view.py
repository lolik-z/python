def input_expression() -> str:
    enter = input('Введите целое число или выражение: ')
    return enter

def input_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию: ')

def print_to_console(value_text):
    print(value_text)

def log_off():
    print('До свидания!')

def log_err():
    print('Ошибка!')

def print_culc_exp(s):
    print(s)

def print_division_by_zero():
    print('На ноль делить нельзя!')