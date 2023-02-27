import sqlite3

try:
    conn = sqlite3.connect('IceCream.db')
    cursor = conn.cursor()
    print('Successfully connected')

    with open('script.sql', 'r') as file:
        sql_scrpt = file.read()

    cursor.executescript(sql_scrpt)
    print("Sqlite script executed successfully")
    cursor.close()

except sqlite3.Error as error:
    print('{}'.format(error))
finally:
    if conn:
        conn.close()
        print('sqlite connection close')

