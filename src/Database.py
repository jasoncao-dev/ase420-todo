import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            task TEXT NOT NULL,
            tag TEXT
        )
        '''
        self.conn.execute(sql)
        self.conn.commit()

    def add_task(self, date, start_time, end_time, task, tag=None):
        sql = '''
        INSERT INTO tasks (date, start_time, end_time, task, tag)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.conn.execute(sql, (date, start_time, end_time, task, tag))
        self.conn.commit()

    def query_tasks(self, date=None, task=None, tag=None):
        sql = 'SELECT date, start_time, end_time, task, COALESCE(tag, "") FROM tasks WHERE 1=1'
        params = ()
        if date:
            sql += ' AND date = ?'
            params += (date,)
        if task:
            sql += ' AND task = ?'
            params += (task,)
        if tag:
            sql += ' AND tag = ?'
            params += (tag,)

        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        return cursor.fetchall()

    def generate_report(self, from_date, to_date):
        query = 'SELECT * FROM tasks WHERE date BETWEEN ? AND ?;'
        cursor = self.conn.cursor()
        cursor.execute(query, (from_date, to_date))
        return cursor.fetchall()

    def get_priority_tasks(self):
        query = """SELECT task, SUM(strftime('%s', end_time) - strftime('%s', start_time)) as total_time
                   FROM tasks GROUP BY task ORDER BY total_time DESC;"""
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()