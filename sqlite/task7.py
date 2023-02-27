import sqlite3


def create_db(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
        task_id INTEGER PRIMARY KEY,
        task_name TEXT,
        task_description TEXT,
        task_status TEXT
    )""")
    conn.commit()
    return conn


def select_all(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    return c.fetchall()


def select_task(conn, task_id):
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE task_id=?", (task_id))
    return c.fetchone()
