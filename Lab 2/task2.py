import re
def number(N):
    return bool(re.match('^[-+]*\d+$', N))
def number_input():
    N = input('Введіть N: ')
    while not number(N):
        N = input("Помилка! Введіть N знову: ")
    n = 1
    N = int(N)
    while n*n<=N:
        print(n*n)
        n=n+1
number_input()