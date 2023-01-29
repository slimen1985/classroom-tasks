import csv

# Создаем собственный диалект для записи файла в csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    delimiter = "|"
    quotechar = "*"
    lineterminator = "\n"

# регистрация диалекта
csv.register_dialect("test_dialect", dialect=CustomDialect)


with open('data/output.csv', 'w') as file:
    # Два варианта использования диалекта: 1) через имя диалекта, 2) через имя класса
    writer = csv.writer(file, dialect='test_dialect')
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])