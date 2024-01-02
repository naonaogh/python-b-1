a = int(input('Введите число a '))
b = int(input('Введите число b '))
summ = 0
sred = 0
for spi in range(a, b+1):
    if spi % 3 == 0:
        sred += 1
        summ = summ + spi

sredSumm = summ/sred
print(sredSumm)