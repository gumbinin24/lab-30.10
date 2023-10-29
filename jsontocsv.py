import csv
import json
import os


def json_2_csv(json_filename):
    if not os.path.exists(json_filename):
        print(f"Файл {json_filename} не найден.")
        return
    csv_filename = os.path.splitext(json_filename)[0] + '.csv'
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    main_key = list(data.keys())[0]
    if main_key not in data or not isinstance(data[main_key], list):
        return
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[main_key][0].keys())
        writer.writeheader()
        for row in data[main_key]:
            writer.writerow(row)
    print(f"Файл {csv_filename} успешно создан.")


if __name__ == "__main__":
    command = input("Введите команду вида: 'json2csv.py файл.json': \n")
    parts = command.split()
    if len(parts) != 2 or parts[0] != "jsontocsv.py":
        print("Введенные данные неправильного формата!")
    else:
        json_filename = parts[1]
        json_2_csv(json_filename)

# jsontocsv.py Sample-employee-JSON-data.json