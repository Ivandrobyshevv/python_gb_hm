from db import *
from f_write import *


def create_phonebook():
    """Добавление контакта в телефонную книгу"""
    last_name, first_name, phone_number = input('Введите фамилию, имя и номер (разделяя пробелом): ').split()

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
    """
    while True:
        print('Поиск по полям (имя, фамилия, номер телефона)\n(Ведите значение или q что бы выйти)')
        value_search = input(">> ").title()
        if value_search == 'Q':
            break
        else:
            contact_dict = list()
            result = get_contact(value_search)
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
                print("Упс, контакт с такой такими данными не найдет, проверь правильность данных")


def update(contact_dict, contact_id):
    for dictionary in contact_dict:
        if contact_id == dictionary['id']:
            main_dictionary = dictionary
            update_dict = dict()
            keys = ['first_name', 'last_name', 'phone_number']
            values = [input(f'Изменить поле {keys[i]}: ') for i in range(len(keys))]
            for key, value in zip(keys, values):
                if value == '':
                    update_dict[key] = main_dictionary[key]
                else:
                    update_dict[key] = value

            update_contact(contact_id, update_dict)


def update_or_delete(contact_dict):
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


def distribution(value):
    """Распределение"""
    if value == '1':
        create_phonebook()
    if value == '2':
        for values in all_contact():
            print(values)
    if value == '3':
        contact_dict = contact_search()
        if contact_dict:
            for values in contact_dict:
                print(values)
            update_or_delete(contact_dict)

    if value == '4':
        write_json()
    if value == '5':
        write_csv()


def main():
    """Главная функция"""
    while True:
        print(
            '\tТелефонная книга'
            '\n1 - Добавить контакт\n2 - Все контакты\n3 - Поиск контакта\n4 - Выгрузить в JSON\n5 - Выгрузить в CSV')
        print("Для выхода введите 'q'")
        temp = input('>> ')
        if temp.lower() == 'q':
            break
        distribution(temp)


if __name__ == '__main__':
    main()
