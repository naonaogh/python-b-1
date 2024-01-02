numb = float(input("введите число: "))
res = 0

def small(numb):
    count = 0
    while numb < 1:
        numb *= 10
        count += 1
    res = f"{round(numb, count)} * 10 ** {count*(-1)}"
    return res

def biq(numb):
    count = 0
    while numb > 10:
        numb /= 10
        count += 1
    res = f"{numb} * 10 ** {count}"
    return res


if numb < 1: print (f"Формат плавающей точки: {small(numb)}")
if numb > 1: print(f"формат плавающей точки: {biq(numb)}")

