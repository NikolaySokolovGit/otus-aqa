import mariadb

from config import config


class MariaDB:
    def __init__(self):
        self.connection = mariadb.connect(**config['db'])
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()
