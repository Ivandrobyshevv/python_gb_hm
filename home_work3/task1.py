from random import randint


def sum_odd_index(numbers: list):
    """Находит сумму элементов списка, стоящих на нечётной позиции."""
    odd_index = numbers[1::2]
    print_result(odd_index, comment="Нечетные индексы:")

    sum_values = sum(odd_index)
    print_result(sum_values, comment="Сумма:")


def print_result(result: list | int, comment: str = ''):
    """Принт полученного результата"""
    print(comment, result)


def main():
    numbers = [randint(-10, 10) for i in range(int(input("Введите размер массива: ")))]
    print_result(numbers, comment='Начальный массив:')
    sum_odd_index(numbers)


if __name__ == '__main__':
    main()
