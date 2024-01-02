def summa_n():
    n = int(input('Введите одно целое положительное число '))
    summ = 0
    for i in range(1, n+1):
        summ += n
    print('Сумма равна', summ)

summa_n()