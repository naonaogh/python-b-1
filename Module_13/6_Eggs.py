def dangerLev(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10

def safeDep(D):
    left = 0
    right = 4
    while right - left > D:
        mid = (left + right) / 2
        dl = dangerLev(mid)
        if dl > 0:
            left = mid
        else:
            right = mid

    return (left + right) / 2

D = float(input("Введите максимально допустимый уровень опасности: "))
sd = safeDep(D)

print(f"Приблизительная глубина безопасной кладки: {sd} м")
 