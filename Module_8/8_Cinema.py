girls = int(input('Введите количество девочек: '))
boys = int(input('Введите количество мальчиков: '))
answer = ''
if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения.')
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girls - k):
        answer += 'BG'
else:
    k = girls - boys
    for gbg in range(k):
        answer += 'GBG'
    for gb in range(boys - k):
        answer += 'GB'
        print('Ответ:', answer)

