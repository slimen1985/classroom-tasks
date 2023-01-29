import csv

sniffer = csv.Sniffer()
dialect = None

with open('data/undefined_dialect.csv', "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open('data/undefined_dialect.csv', "r") as file:
    content = file.read()
    dialect = sniffer.sniff(content)

print(dialect.delimiter, dialect.quotechar, dialect.quoting)


with open('data/undefined_dialect.csv', "r") as file:
    reader = csv.reader(file, dialect=dialect)

    for row in reader:
        print(row)