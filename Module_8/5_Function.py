start = int(input('Введите начало отрезка: '))
fnsh = int(input('Введите конец отрезка: '))
shag = int(input('Введите шаг: '))
for x in range(fnsh, start-1, shag):
    y = x**3 + 2*x**2 - 4*x + 1
    print(f'В точке {x} функция равна {y}')