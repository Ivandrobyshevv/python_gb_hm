def delete_abv(text):
    result = list()
    count = 0
    for line in text:
        for word in line.split():
            if 'абв' not in word:
                result.append(word)
            else:
                print(f'Удаленно слово: {word}')
                count += 1
    string = '\n'.join(result)
    return string


def get_text():
    with open('content "абв"', 'r', encoding='utf-8') as f:
        text = f.readlines()
    return text


def main():
    text = get_text()
    result = delete_abv(text)
    with open('result', 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == '__main__':
    main()
