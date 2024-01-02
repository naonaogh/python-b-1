spisok = []
for put in range(10):
    numberDebt = int(input('Введите номер присвоенный человеку: '))
    spisok.append(numberDebt)
chet = 0
for i in spisok:
    if (i%2 == 0) and (i > 0):
        chet += 1

print(chet)
