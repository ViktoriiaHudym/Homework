import re
def number1(x):
    return bool(re.match('^[+-]?\d*(\.)?\d*$',x))

def number2(y):
    return bool(re.match('^[+-]?\d*(\.)?\d*$',y))

def function(n):
    return bool(re.match('^[1-4]{1}$',n))

def input_func():
    n = input('Оберіть дію (1-додавання, 2-віднімання, 3-множення, 4-ділення): ')
    while not function(n):
        n = input('Помилка! Спробуйте знову: ')
    x = input('Введіть перше число: ')
    while not number1(x):
        x = input('Помилка! Спробуйте знову: ')
    y = input('Введіть друге число: ')
    while not number2(y):
        y = input('Помилка! Спробуйте знову: ')
    return calculator(n,x,y)

def calculator(n,x,y):
    n = int(n)
    x = float(x)
    y = float(y)
    if n == 1:
        return x + y
    elif n == 2:
        return x - y
    elif n == 3:
        return x * y
    else:
        if y == 0:
            return 'На нуль ділити не можна!'
        else:
            return x / y

print('Результат: ',input_func())


