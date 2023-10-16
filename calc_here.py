def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def exp(a, b):
    return a ** b

def percent(a, b):
  return a * (b / 100)


def operation():
    op = input('Выберите операцию: + (сложение), - (вычитание), * (умножение), / (деление), ** (возведение в степень), \n% (для вычисления процента от числа)')
    return op


def calculator():
    print(f'Учтите, что при вычислении процента второе число это и есть процент который вы хотите вычислить от первого числа')

    first_number = int(input('Введите первое число '))
    second_number = int(input('Введите второе число '))
    op = operation()
    if op == '+':
        print(summ(first_number, second_number))
    elif op == '-':
        print(diff(first_number, second_number))
    elif op == '*':
        print(multiple(first_number, second_number))
    elif op == '/':
        print(division(first_number, second_number))
    elif op == '**':
        print(exp(first_number, second_number))
    elif op == '%':
        print(percent(first_number, second_number))
    else:
        print('Эту операцию калькулятор не поддерживает')


