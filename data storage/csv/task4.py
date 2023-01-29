import csv

# используем словари для записи в csv файл DictWriter

quoting = csv.QUOTE_ALL


with open('data/output.csv', "w") as file:
    # Используем данные как словарь
    writer = csv.DictWriter(
        file,
        fieldnames=['fname', 'lname', 'age'],
        quoting=quoting
    )
    writer.writeheader() # записываем заголовки
    writer.writerow(
        {
            "fname": "vadim",
            "lname": "liubin",
            "age": 37
        }
    )
    writer.writerow(
        {
            "fname": "elena",
            "lname": "liubina",
            "age": 38
        }
    )

