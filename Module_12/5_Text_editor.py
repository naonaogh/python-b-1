def count_letters(text, number, bukva):
    count = 0
    count2 = 0
    for i in text:
        if i == number:
            count += 1
        if i == bukva:
            count2 += 1
    print(f'Количество цифр {number}:', count)
    print(f'Количество букв {bukva}:', count2)

text = input('Введите текст: ')
number = str(int(input('Какую цифру ищем? ')))
bukva = input('Какую букву ищем? ')
count_letters(text, number, bukva)