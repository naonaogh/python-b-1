text = int(input('Введите высоту пирамиды: '))
c = 0
d = -1
a = '#'
b = ' '
for number in range(text):
    print(number)
    print(text)
    d += 2
    c = text - number - 1
    print(c * b, d * a)