text = int(input('Введите высоту пирамиды: '))
d = 1
for number in range(text):
    space = text - number - 1
    print('   '*space, end = '')
    for i in range(number+1):
        print(d, end = '   ')
        d += 2
    print()


