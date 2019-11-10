import re
def temperature(temp):
    return bool(re.match('^[+-]{0,1}\d+(\.){0,1}\d*$', temp))

def celsius_input():
    temp = input('Введіть температуру в градусах Цельсія: ')
    while not temperature(temp):
        temp = input('Спробуйте знову: ')
    return float(temp)+273.15

def fahrenheit_input():
    temp = input('Введіть температуру в Фаренгейтах: ')
    while not temperature(temp):
        temp = input('Спробуйте знову: ')
    return (float(temp)-273.5)

def what_temp():
    run = input('Оберіть дію (1-перетворення з C у F, 2-перетворення з F у C): ')
    if run=='1':
        return celsius_input()
    elif run=='2':
        return fahrenheit_input()
    else:
        return what_temp()

print(what_temp())