
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

        self.dummy_data()

        self.refresh_question_list()

    def dummy_data(self):
        self.sql_helper.add_question("test question 1", "option 1", "option 2")
        self.sql_helper.add_question("test question 2", "option 3", "option 4")

    def add_option_button(self):
        dialog = AddOptionDialog(self.tmp_question)
        dialog.exec_()

    def add_question_button(self):
        print("Added")

    def clear_button(self):
        print("Cleared")

    def decide_button(self):
        pass

    def delete_button(self):
        pass

    def refresh_question_list(self):
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
        item = QStandardItem(option)

        self.option_list.append(option)
        self.listWidgetOptions.addItem(option)

        self.lineEditOption.clear()

    def accept(self):
        self.question.options = self.option_list
        super(AddOptionDialog, self).accept()

    def reject(self):
        super(AddOptionDialog, self).reject()


app = QApplication(sys.argv)
program_ui = ProgramUI()
sys.exit(app.exec_())
