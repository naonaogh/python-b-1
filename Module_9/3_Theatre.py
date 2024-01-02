row = int(input('Введите кол-во рядов: '))
mesto = int(input('Введите кол-во сидений в ряде: '))
interval = int(input('Введите кол-во метров между рядами: '))

print('\nСцена')
for i in range(row):
    print('='*mesto, '*'*interval,'='*mesto)

