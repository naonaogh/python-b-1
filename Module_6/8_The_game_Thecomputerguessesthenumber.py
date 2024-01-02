start = 0
finish = 101
while True:
    N = (start + finish) // 2
    print(f'Твое число больше, меньше или равно {N}?')
    answer = int(input('1-больше, 2-меньше, 3-равно '))
    if answer == 3:
        break
    elif answer == 2:
        finish = N
    elif answer == 1:
        start = N
print('Компьютер победил')