def maximum_of_two(n, m):
    maxim = max(n,m)
    return maxim

def maximum_of_three(maxim, p):
    if maxim>p:
        print(maxim)
    else:
        print(p)


maxim = 0
numberOne = float(input('Введите первое число для сравнения: '))
numberTwo = float(input('Введите второе число для сравнения: '))
numberThree = float(input('Введите третье число для сравнения: '))
maximum_of_two(numberOne, numberTwo)
maximum_of_three(maxim, numberThree)