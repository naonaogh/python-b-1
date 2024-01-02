x = int(input('Введите сумму вклада X '))
p = int(input('Введите проценты P '))
y = int(input('Вклад через время Y '))
years = 0
while x < y:
  x *= 1 + p / 100
  x = int(100 * x) / 100
  years += 1
print('Понадобится ', years, 'лет.')
