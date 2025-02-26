import sqlite3
import os

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('interactions.db')
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                prompt TEXT,
                response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_interaction(self, user_id, prompt, response):
        self.conn.execute('''
            INSERT INTO interactions (user_id, prompt, response)
            VALUES (?, ?, ?)
        ''', (user_id, prompt, response))
        self.conn.commit()

    def close(self):
        self.conn.close()