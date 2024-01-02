def test():
    number = int(input('Введите число: '))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print('Вы ввели 0')

def positive():
    print('number positive')

def negative():
    print('number negative')

test()