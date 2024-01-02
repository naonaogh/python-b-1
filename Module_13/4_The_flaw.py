def count_numbers(n):
 return len(n)

def change_number(n):
 sn = str(n)
 swap = sn[-1] + sn[1:-1] + sn[0]
 return int(swap)

def main():
 first_n = input("Введите первое число(трехзначное): ")
 second_n = input("Введите второе число(четырехзначное): ")
 if count_numbers(first_n) == 3:
     print('Изменённое первое число:', change_number(first_n))
 if count_numbers(second_n) == 4:
     print('Изменённое второе число:', change_number(second_n))

main()