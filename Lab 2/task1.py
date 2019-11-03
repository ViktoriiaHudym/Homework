import re
def number(n):
    return bool(re.match('^[-+]*\d+$', n))
def number(x):
    return bool(re.match('^[+-]{0,1}\d+(\.){0,1}\d*$', x))
def number_input():
    n = input('Введіть n: ')
    while not number(n):
        n = input("Помилка! Введіть n знову: ")
    x = input("Введіть x: ")
    while not number(x):
        x = input("Помилка! Введіть x знову: ")
    n = int(n)
    x = float(x)
    return(sum(((x - i) / i**2) for i in range(1, n+1)))
print("Отримана сума:", number_input())
