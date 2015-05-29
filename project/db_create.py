__author__ = 'jonathan'

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    c = connection.cursor()

    c.execute("""CREATE TABLE tasks(
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            priority INTEGER NOT NULL,
            status INTEGER NOT NULL)
    """)

    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Complete Flask taskapp", "05/31/15", 10, 1)'
    )
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Complete Django tutorial", "05/30/15", 8, 1)'
    )
