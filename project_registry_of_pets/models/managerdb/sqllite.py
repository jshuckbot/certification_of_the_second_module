import sqlite3


class SQLite:
    def __init__(self, file='sqlite.db'):
        self.file = file
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        # self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

# with SQLite('nursery.db') as cur:
#     print(cur.execute('SELECT * FROM camels;').fetchall()[0][1])