debt = int(input('Введите количество должников: '))
summ = 0
for dolg in range(0, debt+1, 5):
    print(f'Должник с номером {dolg}')
    skolko = int(input('Сколько должны? '))
    summ += skolko

print(f'Общая сумма долга: {summ}')
