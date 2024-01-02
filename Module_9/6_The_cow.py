korownik = input('Введите строку из десяти символов a и b   ')
sumMilk = 0
for i in range(len(korownik)):
    if korownik[i] == 'b':
        sumMilk += (i + 1) * 2

print("Получено молока за день:", sumMilk, "литров")
