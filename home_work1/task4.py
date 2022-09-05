def get_values(values):
    if values == 1:
        return (f'{values} четверть - x > 0; y > 0')
    if values == 2:
        return (f'{values} четверть - x < 0; y > 0')
    if values == 3:
        return (f'{values} четверть - x < 0; y <0')
    if values == 4:
        return (f'{values} четверть - x > 0; y < 0')
        


def main():
    values = int(input("Введите номер четверти: "))
    print(get_values(values))


if __name__ == '__main__':
    main()