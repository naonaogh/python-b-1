namb = int(input('Введите высоту: '))
namb2 = int(input('Введите ширину: '))
for stro in range(namb+1):
    for stolb in range(namb2+1):
        if (stolb == 0) or (stolb == namb2):
            print('|', end = '')
        elif (stro == 0) or (stro == namb):
            print('-', end='')
        else:
            print(' ', end = '')
    print()

        