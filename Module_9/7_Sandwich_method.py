word = input('Введите зашифрованое слово: ')
sum1 = ' '
sum2 = ' '
count = 0

for text in word:
    count += 1
    if (count % 2 == 1):
        sum1 += text
        print(sum1)
    else:
        sum2 = text + sum2
        print(sum2)

print('Расшифрованое слово', sum1 + sum2)