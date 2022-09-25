from main import all_contact
import json
import csv


def write_json():
    contacts = all_contact()
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)


def write_csv():
    contacts = all_contact()
    csv_col = ['id', 'first_name', 'last_name', 'phone_number']

    with open('contacts.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_col)
        writer.writeheader()
        for data in contacts:
            writer.writerow(data)






