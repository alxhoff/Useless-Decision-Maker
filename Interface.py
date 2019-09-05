
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import StartScreen
import QuestionScreen
import AddOptionDialog

from DatabaseHelper import SQLHelper


class ProgramUI:

    def __init__(self):

        self.start_screen = StartScreen()
        self.question_screen = QuestionScreen()
        self.add_option_dialog = AddOptionDialog()
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

        self.question_list_model = QStandardItemModel(self.listViewQuestions)
        self.listViewQuestions.setModel(self.question_list_model)
        self.question_list = []
        self.refresh_question_list()

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
        dialog = AddOptionDialog()
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
            item = QStandardItem(question.string)
            self.question_list_model.appendRow(item)

        self.listViewQuestions.show()


class AddOptionDialog(QDialog, AddOptionDialog.Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButtonAddOption.clicked.connect(self.add_button)

    def add_button(self):
        pass


app = QApplication(sys.argv)
program_ui = ProgramUI()
sys.exit(app.exec_())
