import os
import sqlite3


class database_create:
    
    def __init__(self, sqlite3_db='database.db'):
        self.cursor = None
        self.is_connected = False
        self.connection = None
        self.sqlite3_db = sqlite3_db
        self.connect()
        self.create_tables()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.sqlite3_db)
            self.is_connected = True
            self.cursor = self.connection.cursor()
            print('Successful connecting!')
        except sqlite3.Error or sqlite3.OperationalError as e:
            self.is_connected = False
            print(f'the error {e} occurred')

    def disconnect(self):
        self.connection.commit()
        self.connection.close()
        self.is_connected = False
        print('Successful disconnection!')

    def create_tables(self):
        self.create_table_users()

    def create_table_users(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        user_id INTEGER,
        is_activated BOOLEAN DEFAULT ( False )
        );
        '''
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print('Table "Users" is successfully created!')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'the error {e} occurred')


if __name__ == '__main__':
    db = database_create()
    db.disconnect()
