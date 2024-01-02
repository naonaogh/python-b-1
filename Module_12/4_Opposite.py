def naoborot(number):
    print('Число наоборот:', number[::-1])

number = str(int(input('Введите число: ')))
if int(number) > 0:
    naoborot(number)
elif number == 0:
    print("Программа завершена!")
else:
    print('Введите положительное число')
