N = int(input('Введите N: '))
print(f'При N = {N} элементы выражения будут равны:')
summ = 0
mass = []
for n in range(0, N):
    print(n)
    elem = (-1) ** n * (1/2**n)
    mass.append(elem)
    mass.append('+')
    summ += elem
    print(f'(-1) ** {n} * (1/2**{n}) = {elem}')
print('Сумма равна: ')
print('s = ', *mass, '=', summ)

