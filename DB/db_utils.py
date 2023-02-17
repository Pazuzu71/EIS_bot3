import os
import sqlite3


class database:
    
    def __init__(self, database='database.db'):
        self.cursor = None
        self.is_connected = False
        self.connecting = None
        self.database = database
        self.connect()

    def connect(self):
        try:
            self.connecting = sqlite3.connect(self.database)
            self.is_connected = True
            self.cursor = self.connecting.cursor()
            print('Successful connecting!')
        except sqlite3.Error or sqlite3.OperationalError as e:
            self.is_connected = False
            print(f'the error {e} occurred')

    def disconnect(self):
        self.connecting.commit()
        self.connecting.close()
        self.is_connected = False
        print('Successful disconnection!')


if __name__ == '__main__':
    db = database()
    db.disconnect()
