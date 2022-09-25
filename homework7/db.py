import sqlite3

connection = sqlite3.connect('phone_numbers.db')
cursor = connection.cursor()


def create_db():
    """Создание таблицы в базе данных"""
    cursor.execute("CREATE TABLE phonebook(first_name VARCHAR(15), last_name VARCHAR(15), phone_number VARCHAR(12))")


def table_exists():
    """Проверка есть ли таблицы в бд"""
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='phonebook' ''')
    if cursor.fetchone()[0] == 1:
        return True
    return False


def insert_movie(first_name, last_name, phone_number):
    """Добавление данных в бд"""
    cursor.execute(''' INSERT INTO phonebook (first_name, last_name, phone_number) VALUES(?, ?, ?) ''',
                   (first_name, last_name, phone_number))
    connection.commit()


def get_values():
    """Выбор всех контактов"""
    cursor.execute('''SELECT rowid, first_name, last_name, phone_number FROM phonebook''')
    data = []
    for row in cursor.fetchall():
        data.append(row)
    return data


def get_contact_first_name(value_search):
    """Поиск контакта в бд"""
    cursor.execute(
        f'SELECT rowid, first_name, last_name, phone_number FROM phonebook WHERE first_name  = "{value_search}" or last_name = "{value_search}" or phone_number = "{value_search}"')
    data = []
    for row in cursor.fetchall():
        data.append(row)
    return data


def update_contact(id_contact, update_dict):
    """Update значений"""
    for key in update_dict.keys():
        if type(update_dict[key]) == str:
            stmt = '''UPDATE phonebook SET {} = '{}' WHERE ROWID = {}'''.format(key, update_dict[key], id_contact)
        else:
            stmt = '''UPDATE phonebook SET {} = '{}' WHERE ROWID = {}'''.format(key, update_dict[key], id_contact)
        cursor.execute(stmt)
    connection.commit()


def delete_contact(contact_id):
    """Удаление"""
    cursor.execute("DELETE FROM phonebook WHERE rowid = ?;", [contact_id])
    connection.commit()
