
def fib(n: int):
    """Последовательность Фибоначчи."""
    a = 0
    b = 1
    list_fib = []
    for __ in range(n + 1):
        list_fib.append(a)
        a, b = b, a + b
    return list_fib


def nega_fib(n: int):
    """Последовательность Фибоначчи отрицательные числа"""
    a = 0
    b = 1
    list_fib = []
    for __ in range(-(n + 1), 0, 1):
        list_fib.append(a)
        a, b = b, a - b
    return list_fib


def main():
    num = int(input("Введите число: "))
    f = fib(num)
    nf = nega_fib(num)
    for i in nf:
        f.insert(0, i)
    f.remove(0)
    return f


if __name__ == '__main__':
    print(main())
