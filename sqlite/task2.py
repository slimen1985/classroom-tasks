import sqlite3


class RowSET:
    def __init__(self):
        self.rows = set()

    def step(self, value):
        self.rows.add(value)

    def finalize(self):
        return ';'.join(self.rows)


with sqlite3.connect(':memory:') as conn:
    conn.create_aggregate('row_set', 1, RowSET)

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
    ('Jack', 'Shepard'),
    ('Desmond', 'Jones')
    """)

    row = cursor.execute('SELECT row_set(fname) FROM users').fetchall()
    print(row)