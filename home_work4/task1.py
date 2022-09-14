while True:
    print("При d = 0.001, π = 3.141.")
    d = input("Задайте точность d:\n>> ")
    num = float(input("Введите число:\n>> "))
    f = len(d[2:])
    print(f'Округлил до {f} знаков после запятой = {num:.{f}f}')
    stop = input("Повторить операцию (y|n)?\n>> ")
    if stop.lower() == 'n':
        print("--------")
        break
