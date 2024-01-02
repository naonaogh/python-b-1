fraze = input('Введите текст: ')
summ = 0
for i in fraze:
    if i == '*' :
        summ += 1
        if summ == 1:
            print(f'Символ «*» стоит на позиции {fraze.index('*')+1}.')

