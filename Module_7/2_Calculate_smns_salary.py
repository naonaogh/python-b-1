summ = 0
sred = 0
for sred in range(12):
    salary = int(input('Введите зарплату сотрудника за месяц: '))
    sred += 1
    summ = summ + salary
salSred = summ/sred
print(salSred)