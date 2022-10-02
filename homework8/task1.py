
def to_dict(lst: list) -> dict:
    """Преобразует список в словарь"""
    return {i: i for i in lst}


def show_res(res: dict) -> None:
    """Выводит словарь в консоль"""
    print(res)


def main() -> None:
    show_res(to_dict([1, 2, 3, 4, 5]))
    show_res(to_dict(['one', ('two', 2), (4, 1)]))


if __name__ == '__main__':
    main()
