kol = int(input('Введите количество карточек:'))
mass = []
mass1 = []
for mist in range(1, kol+1):
    mass.append(mist)
for i in range(1, kol):
    ost = int(input('Введите номер оставшейся карточки:'))
    mass1.append(ost)
    diff = list(set(mass) - set(mass1))


print('Номер пропавшей карточки', *diff)