n = int(input("Введите количество чисел: "))
user_numbers = [int(input(f"Введите число #{i + 1}: ")) for i in range(n)]

max_sum = 0
max_num = 0

for num in user_numbers:
    current_sum = 0
    for digit in str(num):
        current_sum += int(digit)
    if current_sum > max_sum:
        max_sum = current_sum
        max_num = num

print(max_num, max_sum)

