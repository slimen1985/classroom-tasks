import random
import sqlite3


class Chooser:

    def __init__(self):
       self.random_list = []

    def step(self, item):
        print('insert %d' % item)
        self.random_list.append(item)

    def finalize(self):
        return random.choice(self.random_list)


with sqlite3.connect(':memory:') as conn:
    conn.create_aggregate('choice', 1, Chooser)

    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE samples(id INTEGER)
    """)

    cur.executemany('INSERT INTO samples VALUES(?)', ((1,), (2,), (3,), (4,), (5,), (6,)))

    print('samples available: ')
    for i in cur.execute("SELECT * FROM samples"):
        print(i[0])

    for n in cur.execute("SELECT choice(id) FROM samples"):
        print(n[0])