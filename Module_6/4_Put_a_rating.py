summPlus = 0
summMinus = 0
estimation = range(-100, 101)
while estimation != 0 :
    estimation = int(input('Введите число: '))
    if (0<estimation<=100):
        summPlus += 1
    elif (-100<=estimation<0):
        summMinus += 1
print('Кол-во положительных чисел: ', summPlus)
print('Кол-во отрицательных чисел: ', summMinus)