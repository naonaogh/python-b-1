
razm = int(input('Укажите размер файла для скачивания: '))
skor = int(input('Какова скорость вашего соединения: '))
download = 0
times = 0
while download < razm:
    times += 1
    download = download + skor
    if download > razm:
        download = razm
    proc = round((download/razm)*100)
    print(f'Прошло {times} сек. Скачано {download} из 123 Мб ({proc}%) ')
