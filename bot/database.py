import sqlite3
from config import DATABASE_FILE

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reports
            (id INTEGER PRIMARY KEY, user_id INTEGER, report TEXT)
        ''')
        self.conn.commit()

    def add_report(self, user_id, report):
        self.cursor.execute('INSERT INTO reports (user_id, report) VALUES (?, ?)', (user_id, report))
        self.conn.commit()

    def get_reports(self):
        self.cursor.execute('SELECT * FROM reports')
        return self.cursor.fetchall()
