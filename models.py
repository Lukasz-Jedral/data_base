import sqlite3

class Database:
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    '''encapsulated specific quaries'''

    def del_table(self,table_name):
        sql = f'DELETE FROM {table_name}'
        return self.query(sql,())

    def del_book(self,book_id):
        sql = f"DELETE from books WHERE id = ?"
        return self.query(sql,(book_id,))

    def update(self, table_name, id, **kwargs):
        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        values += (id,)

        sql = f''' UPDATE {table_name} SET {parameters} WHERE id = ?'''
        return self.query(sql,(values))