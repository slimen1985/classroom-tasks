import sqlite3


def t_upper(id_: int, raw_text: str) -> str:
    return f"{id_}: {raw_text.upper()}"


try:
    with sqlite3.connect(':memory:') as conn:
        conn.create_function('upper', 2, t_upper)

        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE users(id, fname)
        """)
        cursor.execute("""
            INSERT INTO users(id, fname) VALUES
            (1, 'Mike'), (2, 'Nick'), (3, 'Alex')
        """)
        row = cursor.execute('SELECT id, upper(id, fname) FROM users').fetchall()
        print(row)
except sqlite3.Error as error:
    print("Unexpected error {}".format(error))

