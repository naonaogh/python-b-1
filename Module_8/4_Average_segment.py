a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
summ = 0
sred = 0
for numb in range(a, b+1):
    if numb % c == 0:
        summ += numb
        sred += 1
print(summ/sred)
