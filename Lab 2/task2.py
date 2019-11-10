import re

def number(N):
    return bool(re.match('^[-+]*\d+$', N))

def power(p):
    return bool(re.match('^[-+]*\d+$', p))

def input_func():
    N = input('Введіть N (обмеження): ')
    while not number(N):
        N = input("Помилка! Введіть N знову: ")
    p = input('Числа якого степеня необхідно вивести на екран? ')
    while not power(p):
        p = input("Помилка! Введіть N знову: ")
    return main(N,p)

def main(N,p):
    n = 1
    N = int(N)
    p = int(p)
    while n**p<=N:
        print(n**p)
        n=n+1

input_func()