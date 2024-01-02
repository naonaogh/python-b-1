import random
random.number = random.randint(-100, 100)
numb = random.number
zadach = 0
popit = 0
while zadach != numb:
    zadach1 = int(input('Введите число '))
    zadach = zadach1
    if zadach>numb:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
        popit += 1
    if zadach<numb:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
        popit += 1
print('Вы угадали! Число попыток:', popit)