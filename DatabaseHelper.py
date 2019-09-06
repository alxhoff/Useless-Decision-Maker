import sqlite3
import hashlib

from enum import Enum

from Decision import Decision, Option


class SQLType(Enum):
    NULL = "null"
    INTEGER = "integer"
    REAL = "real"
    TEXT = "text"
    BLOB = 'blob'

    def __str__(self):
        return str(self.value)


class SQLHelper:

    def __init__(self, database_name):
        self.database_name = database_name

        self.conn = self.init_connection(database_name)
        self.cursor = self.conn.cursor()

        self.init_decisions_table()
        self.init_options_table()

    def init_connection(self, database_name):
        conn = None
        try:
            conn = sqlite3.connect(str(database_name))
        except Error as e:
            print(e)

        return conn

    def init_decisions_table(self):
        sql = """CREATE TABLE IF NOT EXISTS decisions(decision_id INTEGER
        PRIMARY KEY AUTOINCREMENT, string TEXT)"""
        self.cursor.execute(sql)
        self.conn.commit()

    def init_options_table(self):
        sql = """CREATE TABLE IF NOT EXISTS options(option_id INTEGER PRIMARY KEY,
        decision_id INTEGER, string TEXT)"""
        self.cursor.execute(sql)
        self.conn.commit()

    def add_decision_object(self, decision):
        q_id = self.add_decision_string(decision.string)
        for option in decision.options:
            self.add_decision_option(q_id, option)
        self.conn.commit()

    def add_decision(self, decision, *options):
        q_id = self.add_decision_string(decision)
        for option in options:
            self.add_decision_option(q_id, option)
        self.conn.commit()

    def add_decision_string(self, decision):
        sql = "INSERT INTO decisions(string) VALUES('{}')".format(decision)
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.lastrowid

    def add_decision_option(self, decision_id, option):
        sql = "INSERT INTO options(decision_id, string) VALUES ({}, '{}')".format(decision_id, option)
        self.cursor.execute(sql)
        self.conn.commit()

    def query_all_decisions(self):
        sql = "SELECT * FROM 'decisions'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def query_all_options(self, q_id):
        sql = "SELECT * FROM 'options' WHERE decision_id={}".format(q_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_all_decision_ids(self):
        decisions = self.query_all_decisions()
        ret = []
        for decision in decisions:
            ret.append(decision[0])

        return ret

    def get_all_option_ids(self, q_id):
        options = self.query_all_options(q_id)
        ret = []
        for option in options:
            ret.append(option[0])

    def get_decision(self, q_id):
        sql = "SELECT * FROM decisions WHERE decision_id={}".format(q_id)
        self.cursor.execute(sql)
        decision = self.cursor.fetchall()
        if decision:
            ret = Decision(decision[0][0], decision[0][1])

            sql = "SELECT * FROM options WHERE decision_id={}".format(q_id)
            self.cursor.execute(sql)
            options = self.cursor.fetchall()

            for option in options:
                ret.options.append(Option(option[1], option[0], option[2]))

            return ret

    def get_decision_string(self, string):
        sql = "SELECT * FROM decisions WHERE string='{}'".format(string)
        self.cursor.execute(sql)
        decision = self.cursor.fetchall()
        if decision:
            return self.get_decision(decision[0][0])

    def update_decision(self, q_id, string):
        sql = """UPDATE decisions SET string='{}' WHERE decision_id={}""".format(string, q_id)
        self.cursor.execute(sql)
        self.conn.commit()

    def update_option(self, o_id, string):
        sql = """UPDATE options SET string='{}' WHERE option_id={}""".format(string, o_id)
        self.cursor.execute(sql)
        self.conn.commit()

    def remove_decision_string(self, string):
        decision = self.get_decision_string(string)
        if decision:
            sql = "DELETE FROM decisions WHERE string='{}'".format(decision.string)
            self.cursor.execute(sql)
            for option in decision.options:
                sql = "DELETE FROM options WHERE string='{}'".format(option)
            self.conn.commit()

    def get_all_decisions(self):
        ret = []
        ids = self.get_all_decision_ids()
        for q_id in ids:
            decision = self.get_decision(q_id)
            if decision:
                ret.append(decision)

        return ret
