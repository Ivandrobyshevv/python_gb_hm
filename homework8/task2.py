my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs) -> None:
    """Добавляет значения в словарь"""
    my_dict.update(kwargs)


def main() -> None:
    biggest_dict(zero=0, one=1, two=2, three=3, four=4, five=5)


if __name__ == '__main__':
    main()
    print(my_dict)
