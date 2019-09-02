import sqlite3
from Decision import Decision


class SDLHelper:

    def __init__(self, database_name):
        self.database_name = database_name

        self.conn = sqlite3.connect(str(database_name))
        self.cursor = self.conn.cursor()

    def add_table(self)
