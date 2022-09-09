from random import uniform


def fractional_difference(numbers: list):
    """Разница между максимальным и минимальным значением дробной части элементов:"""
    list_frac = [(i % 1) for i in numbers]
    result = max(list_frac) - min(list_frac)
    print_result(round(result, 2),
                 comment="Разница между максимальным и минимальным значением дробной части элементов:")


def print_result(result: list | int, comment: str = ''):
    """Принт полученного результата"""
    print(comment, result)


def main():
    numbers = [round(uniform(-10, 10), 2) for i in range(int(input("Введите размер массива: ")))]
    print_result(numbers, comment='Начальный массив:')
    fractional_difference(numbers)


if __name__ == '__main__':
    main()
