import re
def number(a):
    return bool(re.match('^[-+]*\d+$', a))
def number(b):
    return bool(re.match('^[-+]*\d+$', b))
def number_input():
    a = input('Enter a: ')
    while not number(a):
        a = input("Enter again a: ")
    b = input("Enter b: ")
    while not number(b):
        b = input("Enter again b: ")
    a = int(a)
    b = int(b)
    if a>b:
        return(a, a)
    elif b>a:
        return(b, b)
    else:
        return(0, 0)
print(number_input())