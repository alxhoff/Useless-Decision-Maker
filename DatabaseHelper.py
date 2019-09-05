import sqlite3
import hashlib

from enum import Enum

from Question import Question


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

        self.init_questions_table()
        self.init_options_table()

    def init_connection(self, database_name):
        conn = None
        try:
            conn = sqlite3.connect(str(database_name))
        except Error as e:
            print(e)

        return conn

    def init_questions_table(self):
        sql = "CREATE TABLE IF NOT EXISTS questions(question_id INTEGER PRIMARY KEY AUTOINCREMENT, string TEXT)"
        self.cursor.execute(sql)
        self.conn.commit()

    def init_options_table(self):
        sql = "CREATE TABLE IF NOT EXISTS options(question_id INTEGER, string TEXT)"
        self.cursor.execute(sql)
        self.conn.commit()

    def add_question_object(self, question):
        q_id = self.add_question_string(question.string)
        for option in question.options:
            self.add_question_option(q_id, option)
        self.conn.commit()

    def add_question(self, question, *options):
        q_id = self.add_question_string(question)
        for option in options:
            self.add_question_option(q_id, option)
        self.conn.commit()

    def add_question_string(self, question):
        sql = "INSERT INTO questions(string) VALUES('{}')".format(question)
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.lastrowid

    def add_question_option(self, question_id, option):
        sql = "INSERT INTO options(question_id, string) VALUES ({}, '{}')".format(question_id, option)
        self.cursor.execute(sql)
        self.conn.commit()

    def query_all_questions(self):
        sql = "SELECT * FROM 'questions'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_all_question_ids(self):
        questions = self.query_all_questions()
        ret = []
        for question in questions:
            ret.append(question[0])

        return ret

    def get_question(self, q_id):
        sql = "SELECT * FROM questions WHERE question_id={}".format(q_id)
        self.cursor.execute(sql)
        question = self.cursor.fetchall()
        if question:
            ret = Question(question[0][0], question[0][1])

            sql = "SELECT * FROM options WHERE question_id={}".format(q_id)
            self.cursor.execute(sql)
            options = self.cursor.fetchall()

            for option in options:
                ret.options.append(option[1])

            return ret

    def get_question_string(self, string):
        sql = "SELECT * FROM questions WHERE string='{}'".format(string)
        self.cursor.execute(sql)
        question = self.cursor.fetchall()
        if question:
            return self.get_question(question[0][0])

    def remove_question_string(self, string):
        question = self.get_question_string(string)
        if question:
            sql = "DELETE FROM questions WHERE string='{}'".format(question.string)
            self.cursor.execute(sql)
            for option in question.options:
                sql = "DELETE FROM options WHERE string='{}'".format(option)
            self.conn.commit()

    def get_all_questions(self):
        ret = []
        ids = self.get_all_question_ids()
        for q_id in ids:
            question = self.get_question(q_id)
            if question:
                ret.append(question)

        return ret
