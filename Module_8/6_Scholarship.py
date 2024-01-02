educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
month = 0
summ = 0
for i in range(1, 11):
    month += 1
    debt = expenses - educational_grant
    print(f'{month}. Месяц траты', round(expenses, 2), 'не хватает', round(debt, 2))
    summ += debt
    expenses += ((expenses*3)/100)
print('Нужно попросить у родителей', round(summ, 2), 'рублей')