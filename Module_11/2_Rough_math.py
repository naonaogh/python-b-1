import math

num = int(input('Введите кол-во чисел: '))
while num>0:
    nbr = float(input('Введите число: '))
    if nbr > 0:
        nbr = math.ceil(nbr)
        print(nbr)
        nbr = math.log(nbr)
    elif nbr < 0:
        nbr = int(nbr)
        print(nbr)
        nbr = math.exp(nbr)
    num -= 1
    print(nbr)

