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

def operation():
  op = input('Выберите операцию: +(сложение), -(вычитание), *(умножение), /(деление), **(возведение в степень)')
  return op

def calculator():
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
  else:
    print('Эту операцию калькулятор не поддерживает')

