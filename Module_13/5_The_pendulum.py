numb1 = float(input('Введите начальную амплитуду: '))
numb2 = float(input('Введите амплитуду остановки: '))

kolKol = 0
while numb1 > numb2:
    numb1 *= 0.916
    kolKol += 1

print(f'Маятник считается остановившимся через {kolKol} колебаний')


