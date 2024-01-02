def slojenie(number):
    summ = 0
    for i in str(number):
        m = int(i) % 10
        summ += m
    print('Сумма цифр:', summ)

def maximum(number):
    l = []
    for i in str(number):
        m = int(i) % 10
        l.append(m)
    print('Максимальная цифра:', max(l))

def minimum(number):
    l = []
    for i in str(number):
        m = int(i) % 10
        l.append(m)
    print('Минимальная цифра:', min(l))

while True:
    number = int(input('Введите число: '))
    deistvie = int(input('Введите действие: 1 - сложение цифр числа, 2 - максимальная цифра, 3 - минимальная цифра '))
    if deistvie == 1:
        slojenie(number)
    elif deistvie == 2:
        maximum(number)
    elif deistvie == 3:
        minimum(number)
    else:
        print('Ошибка ввода!')




