print('Начался восьмичасовой рабочий день. ')
workingday = 0
hour = 0
wife1 = 0
while hour <= 8:
    hour += 1
    print (hour,'-й час')
    zadacha = int(input('Сколько задач решит Влад?'))
    workingday += zadacha
    wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет):'))
    wife1 += wife
print('Рабочий день закончился. Всего выполнено задач:', workingday)
if wife >= 1:
    print('Нужно зайти в магазин.')

