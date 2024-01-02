for num in range(10, 100):
    first = num%10
    sec = num//10
    muiti = first*sec
    step = muiti*3
    if (step<100) and (step == num):
        print(step)