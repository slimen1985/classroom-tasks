import sqlite3


with sqlite3.connect(':memory:') as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            FNAME CHAR(20) NOT NULL,
            lname CHAR(20) NOT NULL)
        """)
    cursor.execute("""
    INSERT INTO users(fname, lname) VALUES
    ('John', 'Lock'),
    ('Jack', 'Shepard')
    """)

with open('dump.sql', 'w') as file:
    for line in conn.iterdump():
        file.write('%s\n' % line)
        print('{}\n'.format(line))



