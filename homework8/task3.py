from collections import Counter


def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]).most_common(3))


def main():
    print(count_it('123456789012133288776655353535353441111'))
    print(count_it('1234567890121332887753441111'))
    print(count_it('999999999999999999'))


if __name__ == '__main__':
    main()
