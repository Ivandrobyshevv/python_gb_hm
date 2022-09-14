from random import randint

FILE = 'task4/polynomial'

def get_polynomial(k: int):
    """Создает многочлен"""
    kef = []
    count = k - 1
    s = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹'
    }

    while count > 0:
        digit = randint(-10, 10)
        if digit != 0:
            kef.append(digit)
            count -= 1

    polynomial = ''

    for i in range(len(kef)):
        polynomial += str(kef[i]) + 'x'
        degree = ''

        for elem in list(str(len(kef) - i + 1)):
            degree += s.get(elem)
        polynomial += degree + ' '

    if k > 0 and k != 1:
        string = ' + '.join(polynomial.split()) + f' + {randint(-10, 10)}x + {randint(-10, 10)} = 0\n'
        write_polynomial(string)
    elif k == 1:
        string = f'{randint(-10, 10)}x + {randint(-10, 10)} = 0\n'
        write_polynomial(string)


def write_polynomial(string):
    """Записывает строку в polynomial.txt"""
    with open(FILE, 'a', encoding='utf-8') as f:
        f.write(string)


def main():
    """Главная функция"""
    k = int(input("Введите значения k: "))
    get_polynomial(k)


if __name__ == '__main__':
    main()
