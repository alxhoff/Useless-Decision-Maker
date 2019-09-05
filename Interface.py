import random
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import StartScreen
import QuestionScreen
import AddOptionDialog

from DatabaseHelper import SQLHelper
from Question import Question


class ProgramUI:

    def __init__(self):

        random.seed(time.time())

        self.start_screen = StartScreen()
        self.question_screen = QuestionScreen()
        self.start_screen.show()

        # Connect start button to slot
        self.start_screen.labelStartButton.clicked.connect(self.StartScreenFinished)

    def StartScreenFinished(self):
        self.start_screen.close()
        self.question_screen.show()


class StartScreen(QMainWindow, StartScreen.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)


class QuestionScreen(QMainWindow, QuestionScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.sql_helper = SQLHelper('decisions.db')

        self.question_list = []
        self.refresh_question_list()

        self.tmp_question = Question(None, "")

        # Buttons
        self.pushButtonAdd.clicked.connect(self.add_question_button)
        self.pushButtonAddOptions.clicked.connect(self.add_option_button)
        self.pushButtonClear.clicked.connect(self.clear_button)
        self.pushButtonDelete.clicked.connect(self.delete_button)
        self.pushButtonDecide.clicked.connect(self.decide_button)
        self.pushButtonModify.clicked.connect(self.modify_button)

        #  self.dummy_data()

        self.refresh_question_list()

    def dummy_data(self):
        self.sql_helper.add_question("test question 1", "option 1", "option 2")
        self.sql_helper.add_question("test question 2", "option 3", "option 4")

    def add_option_button(self):
        dialog = AddOptionDialog(self.tmp_question)
        self.listWidgetOptions.clear()
        if dialog.exec_() == QDialog.Accepted:
            for option in self.tmp_question.options:
                self.listWidgetOptions.addItem(option)

    def add_question_button(self):
        self.tmp_question.string = self.lineEditQuestion.text()
        if self.tmp_question.string == "":
            QMessageBox.warning(self, "Missing parameter", "Please add a valid decision question!")
            return

        if len(self.tmp_question.options) < 2:
            QMessageBox.warning(self, "Missing parameter", "You need more options!")
            return

        self.sql_helper.add_question_object(self.tmp_question)
        self.tmp_question = Question(None, "")

        self.lineEditQuestion.clear()
        self.listWidgetOptions.clear()

        self.refresh_question_list()
        self.lineEditQuestion.setFocus()

    def clear_button(self):
        self.tmp_question.clear()
        while self.listWidgetOptions.count() > 0:
            self.listWidgetOptions.takeItem(0)
        self.lineEditQuestion.clear()
        self.lineEditQuestion.setFocus()

    def decide_button(self):
        row = self.listWidgetQuestions.selectedIndexes()
        if(row):
            row_index = row[0].row()
            question = self.question_list[row_index]
            option_index = random.randint(0, len(question.options) - 1)
            option = question.options[option_index]
            reply = "Decision: \n\n{}".format(option)
            QMessageBox.question(self, question.string, reply, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

    def delete_button(self):
        row = self.listWidgetQuestions.selectedIndexes()
        if(row):
            row_index = row[0].row()
            question = self.question_list[row_index]
            self.sql_helper.remove_question_string(question.string)
            del self.question_list[row_index]
            self.listWidgetQuestions.takeItem(row_index)
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

    def modify_button(self):
        pass

    def refresh_question_list(self):
        self.listWidgetQuestions.clear()
        self.question_list = self.sql_helper.get_all_questions()

        for question in self.question_list:
            self.listWidgetQuestions.addItem(question.string)

        self.listWidgetQuestions.show()


class AddOptionDialog(QDialog, AddOptionDialog.Ui_Dialog):

    def __init__(self, question, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        for option in question.options:
            self.listWidgetOptions.addItem(option)

        self.question = question

        self.pushButtonAddOption.clicked.connect(self.add_button)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.option_list = []

    def add_button(self):
        option = self.lineEditOption.text()
        if option:
            item = QStandardItem(option)

            self.option_list.append(option)
            self.listWidgetOptions.addItem(option)

            self.lineEditOption.clear()
            self.lineEditOption.setFocus()
        else:
            QMessageBox.warning(self, "Missing parameter", "Please add a valid decision option!")

    def accept(self):
        self.question.options = self.option_list
        super(AddOptionDialog, self).accept()

    def reject(self):
        super(AddOptionDialog, self).reject()


app = QApplication(sys.argv)
program_ui = ProgramUI()
sys.exit(app.exec_())
