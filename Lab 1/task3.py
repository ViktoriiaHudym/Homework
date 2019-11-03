import re
def function(x):
    return bool(re.match('^[-+]{0,1}\d+$', x))
def function_input():
    x = input('Enter x: ')
    while not function(x):
        x = input('Enter x again: ')
    x = int(x)
    if x<=7:
        return(3*x-9)
    else:
        return(1/(x**2-4))
print('F(x)=', function_input())