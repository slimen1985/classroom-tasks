import csv

with open('data/output.csv', "w") as file:
    # Экранирование символов, которые могут нарушить парсинг
    quoting = csv.QUOTE_MINIMAL
    writer = csv.writer(file, quoting=quoting)
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])
