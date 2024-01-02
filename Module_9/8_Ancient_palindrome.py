for i in range(1000):
    a=input('Введите слово: ')
    a1=a[::-1]
    if a==a1:
        print('да, слово палиндром')
    else:
        print('нет, слово не палиндром')