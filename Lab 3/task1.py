import re

def findwords(words):
    return bool(re.findall('[A-Za-zА-Яа-яіІїЇьЙйЩщ ]+\s*', words))

def findnum(num):
    return bool(re.match('^[0-9]{1,}$', num))

def getdata():
    symb = input('Яким символом доповнюємо слова? ')
    sep = input('Роздільник між словами у вашому рядку: ')
    words = input('Введіть рядок слів: ')
    while not findwords(words):
        words = input('Введіть слова знову: ')
    num = input('Введіть максимальну кількість символів у слові: ')
    while not findnum(num):
        num = input('Введіть число знову: ')
    return main(symb,sep,words,num)

def main(symb,sep,words,num):
    num = int(num)
    symb = str(symb)
    sep = str(sep)
    words2 = []
    if sep in words:
        for word in words.split(sep):
            if len(word)<num:
                words2.append(word+(symb)*(num - len(word)))
            else:
                words2.append(word)
        return (', '.join(list(words2)))
    else:
        print('Не знайдено заданого роздільника!')
        return getdata()

print('Отриманий рядок: ', getdata())