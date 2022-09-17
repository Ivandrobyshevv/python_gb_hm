PATH_READ_FILE = 'text'
PATH_ENCODING_FILE = 'result_code'


def write_code(code):
    string = ''
    for key, value in code.items():
        string += str(value) + key
    with open(PATH_ENCODING_FILE, 'w') as file:
        file.write(string)


def coding(path):
    count_letter = dict()
    with open(path) as f:
        date = f.read()
    for letter in date:
        count_letter[letter] = count_letter.setdefault(letter, 0) + 1

    write_code(count_letter)


def encoding(path):
    with open(path, 'r') as file:
        date = file.read()

    print(date)
    words = [(date[i], date[i + 1]) for i in range(0, len(date) - 1, 2)]
    for num, litter in words:
        print(litter * int(num), end='')


def main():
    coding(PATH_READ_FILE)
    encoding(PATH_ENCODING_FILE)


if __name__ == '__main__':
    main()
