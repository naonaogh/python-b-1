name = input("Введите текст: ")
res = max(list(map(len, name.split())))
print("Самое длинное слово : " + str(res) + " буквы")