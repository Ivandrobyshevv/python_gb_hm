def get_quarter(x, y):
    if x > 0 and y > 0:
        return f'x={x}; y={y} -> 1' 
    elif x < 0 and y > 0:
        return f'x={x}; y={y} -> 2' 
    elif x < 0 and y < 0:
        return f'x={x}; y={y} -> 3'
    else:
        return f'x={x}; y={y} -> 3'


def main():
    x = int(input('Введите значение X: '))
    y = int(input('Введите значение Y: '))
    print(get_quarter(x, y))


if __name__ == '__main__':
    main()