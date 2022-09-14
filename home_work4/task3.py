from random import randint


def get_list_numbers(size):
    numbers = [randint(-size - 1, size + 1) for i in range(size)]
    return numbers


def get_exclusive_items(numbers):
    return list(set(numbers))


def main():
    """Главная функция"""
    while True:
        size = int(input("Введите размер массива: "))
        numbers = get_list_numbers(size)
        print(f'Начальный массив: {numbers}')
        exclusive_numbers = get_exclusive_items(numbers)
        print(f'Неповторяющиеся элементы: {exclusive_numbers}')
        stop = input("Повторить операцию (y|n)?\n>> ")
        if stop.lower() == 'n':
            print("--------")
            break


if __name__ == '__main__':
    main()
