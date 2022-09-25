from db import *
from f_write import *


def create_phonebook():
    """Добавление контакта в телефонную книгу"""
    first_name, last_name = input('Введите имя и фамилию (разделяя пробелом): ').split()
    phone_number = input('Введите номер телефона: ')

    if table_exists():
        insert_movie(first_name.title(), last_name.title(), phone_number)
    else:
        create_db()
        insert_movie(first_name.title(), last_name.title(), phone_number)


def all_contact():
    """
    Вывод всех контактов
    :return: dict
    """
    date = get_values()

    contact_dict = list()
    for values in date:
        rowid, lsat_name, first_name, number = values
        contact = {
            'id': rowid,
            'first_name': first_name,
            'last_name': lsat_name,
            'phone_number': number
        }
        contact_dict.append(contact)

    return contact_dict


def contact_search():
    """
    Поиск контакта по полям (first_name, last_name, phone_number)
    :return: dict
    """
    while True:
        print('Поиск по полям (имя, фамилия, номер телефона)\n(Ведите значение или q что бы выйти)')
        value_search = input(">>").title()
        if value_search == 'Q':
            return False
        else:
            contact_dict = list()
            result = get_contact_first_name(value_search)
            if result:
                for values in result:
                    rowid, lsat_name, first_name, number = values
                    contact = {
                        'id': rowid,
                        'first_name': first_name,
                        'last_name': lsat_name,
                        'phone_number': number
                    }
                    contact_dict.append(contact)
                return contact_dict
            else:
                print("Упс, контакт с такой такими данными не найдет, проверте коректность данных")


def update(contact_dict, contact_id):
    """
    Обновление полей контакта
    :param contact_dict: dict
    :return:
    """
    update_dict = dict()
    res = contact_dict[contact_id]
    keys = ['first_name', 'last_name', 'phone_number']
    values = [input(f'Изменить поле {keys[i]}: ') for i in range(len(keys))]

    for key, values in zip(keys, values):
        if values == '':
            update_dict[key] = res[key]
        else:
            update_dict[key] = values

    update_contact(contact_id, update_dict)


def main():
    while True:
        print(
            '\tТелефонная книга'
            '\n1 - Добавить контакт\n2 - Все контакты\n3 - Поиск контакта\n4 - Выгрузить в JSON\n5 - Выгрузить в CSV')
        print("Для выхода введите 'q'")
        temp = input('>> ')

        if temp.lower() == 'q':
            break

        if temp == '1':
            create_phonebook()

        if temp == '2':
            for values in all_contact():
                print(values)

        if temp == '3':
            contact_dict = contact_search()
            if contact_dict:
                for values in contact_dict:
                    print(values)
                while True:
                    res = input('1 - Изменит данные\n2 - Удалить контакт\n(Введите "q" что бы выйти)\n>> ')
                    if res == 'q':
                        break
                    elif res == '1':
                        contact_id = int(input("Введите id контакта: "))
                        update(contact_dict, contact_id)
                        break
                    elif res == '2':
                        contact_id = int(input("Введите id контакта: "))
                        delete_contact(contact_id)
                        break
                    else:
                        print(f'Не известное действие - {res}')
                        continue
            else:
                continue

        if temp == '4':
            write_json()

        if temp == '5':
            write_csv()


if __name__ == '__main__':
    main()
