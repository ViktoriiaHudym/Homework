import re
def number(a):
    return bool(re.match('^[-+]*\d+$', a))

def number(b):
    return bool(re.match('^[-+]*\d+$', b))

def number_input():
    a = input('Введіть ціле число a: ')
    while not number(a):
        a = input("Спробуте знову a: ")
    b = input("Введіть ціле число b: ")
    while not number(b):
        b = input("Спробуйте знову b: ")
    return main(a,b)

def main(a,b):
    a = int(a)
    b = int(b)
    if a>b:
        return(a, a)
    elif b>a:
        return(b, b)
    else:
        return(0, 0)

print('Отримана пара чисел:', number_input())