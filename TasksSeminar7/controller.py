import model
import view
import parser
import expression

def input_first():
    while True:
        try:
            exp = view.input_expression()
            exp = parser.pars_str_ex(exp)
            if len(exp) == 0:
                view.log_err()
            elif len(exp) == 1:
                try:
                    number = int(exp[0])
                    model.set_first(number)
                    break
                except:
                    view.log_err()
            else:
                try:
                    s = parser.pars_str_ex_print(exp)
                    number = expression.calc_expression(exp)
                    model.set_first(number)
                    view.print_culc_exp(f'{s} {number}')
                    break
                except:
                    view.log_err()
        except:
            view.log_err()

def input_second():
    while True:
        try:
            exp = view.input_expression()
            exp = parser.pars_str_ex(exp)
            if len(exp) == 0:
                view.log_err()
            elif len(exp) == 1:
                try:
                    number = int(exp[0])
                    if model.get_operation() == '/' and number == 0:
                        view.print_division_by_zero()
                    else:
                        model.set_second(number)
                        break
                    break
                except:
                    view.log_err()
            else:
                try:
                    s = parser.pars_str_ex_print(exp)
                    number = expression.calc_expression(exp)
                    if model.get_operation() == '/' and number == 0:
                        view.print_division_by_zero()
                    else:
                        model.set_second(number)
                        view.print_culc_exp(f'{s} {number}')
                        break
                    break
                except:
                    view.log_err()
        except:
            view.log_err()

def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplicstion()
    elif oper == '/':
        model.division()

    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())

def start():
    print('Старт')
    input_first()
    while True:
        input_operation()
        if model.get_operation() == '=':
            view.log_off()
            break
        input_second()
        solution()
