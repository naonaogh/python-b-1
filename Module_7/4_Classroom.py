quantity = int(input('Введите количество детей в классе '))
three = 0
four = 0
five = 0
for i in range(0, quantity):
    ots = int(input('Введите оценку '))
    match ots:
        case 3: three += 1
        case 4: four += 1
        case 5: five += 1
        case _: print('Вы написали ошибочную оценку ')

print('Троек в классе:', three, 'Четверок в классе:', four, 'Пятерок в классе:', five)