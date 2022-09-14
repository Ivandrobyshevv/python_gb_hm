FILES = ['file1', 'file2']
RESULT_FILE = 'result_polynomial'


def read_pol(list_files):
    """Считывает 2 значения из файлов ['file1', 'file2']"""
    list_pol = list()
    for file in FILES:
        with open(file, 'r', encoding='utf-8') as f:
            date = f.read()
            list_pol.append(date)
    return list_pol


def convert_polynomial(list_pol):
    """Преобразует polynomial"""
    pol1, pol2 = list_pol
    pol_elem = pol1.replace('= 0', '').split() + pol2.replace('= 0', '').split()
    pol_elem = [i for i in pol_elem if i != '+']
    sum_dict = {}
    for elem in pol_elem:
        elem = elem.split('*')
        if len(elem) > 1:
            v, s = elem
            sum_dict[s] = sum_dict.setdefault(s, 0) + int(v)
        else:
            sum_dict['0'] = sum_dict.setdefault('0', 0) + int(elem[0])
    return sum_dict


def write_polynomial(sum_dict):
    """Запись в 'result_polynomial'"""
    string = ''
    for key, value in sum_dict.items():
        if key != '0':
            string += f'{str(value)}*{key}' + ' + '
        else:
            string += str(value) + ' = 0'
    with open(RESULT_FILE, 'a') as f:
        f.write(string)


def main():
    """Главная функция"""
    list_pol = read_pol(FILES)
    res_polynomial = convert_polynomial(list_pol)
    write_polynomial(res_polynomial)


if __name__ == '__main__':
    main()
