spis = int(input('Введите количество чисел: '))
summ = 0
f = 0
for numb in range(spis):
    nuberCod = int(input('Введите число: '))
    for i in range(2, nuberCod // 2):
        if (nuberCod % i) == 0:
            summ += 1
        else:
            summ = summ
        if summ == 0:
            f += 1
print('Количество простых чисел в последовательности: ', f)