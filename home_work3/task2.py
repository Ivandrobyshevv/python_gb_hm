from random import randint


def product_pairs_numbers(numbers: list):
    """Находит произведение пар чисел списка."""
    list_total = []
    start = 0
    end = len(numbers) - 1

    while start <= end:
        list_total.append(numbers[start] * numbers[end])
        start += 1
        end -= 1
    print_result(list_total, comment="Сумма пар числе:")


def print_result(result: list | int, comment: str = ''):
    """Принт полученного результата"""
    print(comment, result)


def main():
    numbers = [randint(-10, 10) for i in range(int(input("Введите размер массива: ")))]
    print_result(numbers, comment='Начальный массив:')
    product_pairs_numbers(numbers)


if __name__ == '__main__':
    main()
