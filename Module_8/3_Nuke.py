reverse_timer = int(input('Ввести количество минут разогрева '))
for timer in range(reverse_timer, -1, -1):
    que = int(input('Ваша еда готова? Да, еда готова - 1, Нет - 0 '))
    if que == 1:
        print(f'Ваша еда готова, можете забрать, осталось {timer-1} минут ')
        break
    timer -= 1
    if timer == 0:
        print('Ваша еда готова, осторожно горячo!')
        break