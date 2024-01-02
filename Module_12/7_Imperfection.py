def rock_paper_scissors():
  import random
  game1 = ['камень', 'ножницы', 'бумага']
  random_place = random.choice(game1)
  simb = input('Введите камень, ножницы, бумага ')
  if (random_place == 'камень') and (simb == 'камень'):
    print('Ничья!')
  elif (random_place == 'камень') and (simb == 'ножницы'):
    print('Проиграл!')
  elif (random_place == 'камень') and (simb == 'бумага'):
    print('Выиграл!')
  elif (random_place == 'ножницы') and (simb == 'камень'):
    print('Выиграл!')
  elif (random_place == 'ножницы') and (simb == 'ножницы'):
    print('Ничья!')
  elif (random_place == 'ножницы') and (simb == 'бумага'):
    print('Проиграл!')
  elif (random_place == 'бумага') and (simb == 'камень'):
    print('Проиграл!')
  elif (random_place == 'бумага') and (simb == 'ножницы'):
    print('Выиграл!')
  elif (random_place == 'бумага') and (simb == 'бумага'):
    print('Ничья!')


def guess_the_number():
  import random
  random.number = random.randint(-100, 100)
  numb = random.number
  zadach = 0
  popit = 0
  while zadach != numb:
    zadach1 = int(input('Введите число '))
    zadach = zadach1
    if zadach > numb:
      print('Число больше, чем нужно. Попробуйте ещё раз!')
      popit += 1
    if zadach < numb:
      print('Число меньше, чем нужно. Попробуйте ещё раз!')
      popit += 1
  print('Вы угадали! Число попыток:', popit)

def mainMenu():
  games = int(input('Введите номер игры: 1-Камень, ножницы, бумага 2-угадай число '))
  if games == 1:
    rock_paper_scissors()
  elif games == 2:
    guess_the_number()
  else:
    print('Введите число заново!')


mainMenu()