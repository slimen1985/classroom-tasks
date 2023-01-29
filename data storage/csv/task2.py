import csv

with open('data/example.csv', "r") as file:
    reader = csv.DictReader(file)

    # Преобразует строки csv в словарь
    # Значения можно обрабатывать через ключ
    for row in reader:
        print(int(row.get('price')))

