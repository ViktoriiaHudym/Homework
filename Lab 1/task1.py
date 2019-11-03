import re
def celsius(number):
    return bool(re.match('^[+-]{0,1}\d+(\.){0,1}\d*$', number))
def celsius_input():
    number = input('Введіть температуру в градусах Цельсія: ')
    while not celsius(number):
        number = input('Спробуйте знову: ')
    return(float(number)+273.15)

print('Температура в градусах Кельвіна:', celsius_input())