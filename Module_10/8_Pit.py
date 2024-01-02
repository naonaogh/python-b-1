dep = int(input('Введите глубину ямы: '))
for i in range(dep):
    for j in range(dep, dep-i-1, -1):
        print(j, end = '')
    poi = 2*(dep-i-1)
    print('.'*poi, end = '')
    for m in range(dep-i, dep +1):
        print(m, end='')
    print()

