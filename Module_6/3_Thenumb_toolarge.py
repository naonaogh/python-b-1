number = int(input('Введите число: '))
summ = 0
while number!=0:
    beck = number % 10
    summ += 1
    number //=10
print('Сумма:',summ)