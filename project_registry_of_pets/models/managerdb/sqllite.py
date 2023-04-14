import sqlite3


class SQLite:
    def __init__(self, file='sqlite.db'):
        self._file = file
    
    def __enter__(self):
        self.conn = sqlite3.connect(self._file)
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
