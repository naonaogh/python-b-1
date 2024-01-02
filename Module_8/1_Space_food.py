summ = 0
for grech in range(101, 1, -4):
    summ += 1
    if summ == 1: print(f'у тебя в запасе {grech} кг через {summ} месяц')
    if 1<summ<5:  print(f'у тебя в запасе {grech} кг через {summ} месяца')
    if summ>=5: print(f'у тебя в запасе {grech} кг через {summ} месяцев')