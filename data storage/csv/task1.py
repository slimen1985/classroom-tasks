import csv

# Открываем файл на чтение
with open('data/example.csv', "r") as file:
    reader = csv.reader(file)
    print("Lines num", reader.line_num)
    print("Dialect", reader.dialect) # диалект устанавливает правила парсинга

    # Считываем файл построчно
    for row in reader:
        print(row)
        print("Lines num", reader.line_num)
