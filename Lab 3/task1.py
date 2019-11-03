import re

def findwords(words):
    return bool(re.findall('[A-Za-zА-Яа-яіІїЇьЙйЩщ ]+\s*', words))

def findnum(num):
    return bool(re.match('^[0-9]{1,}$', num))

def getdata():
    words = input('Введіть ваші слова через пробіл: ')
    while not findwords(words):
        words = input('Введіть слова знову: ')
    num = input('Введіть максимальне число символів: ')
    while not findnum(num):
        num = input('Введіть число знову: ')
    num = int(num)
    words2 = []
    for word in words.split( ):
        if len(word)<num:
           words2.append(word+'*'*(num - len(word)))
        else:
            words2.append(word)
    return (','.join(list(words2)))

print("Результат: ", getdata())