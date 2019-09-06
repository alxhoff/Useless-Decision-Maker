import random
import time
import sys
import fnmatch

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import StartScreen
import QuestionScreen
import AddOptionDialog
import EditOptionDialog

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

        self.search_list = []

        # Buttons
        self.pushButtonAdd.clicked.connect(self.add_question_button)
        self.pushButtonAddOptions.clicked.connect(self.add_option_button)
        self.pushButtonClear.clicked.connect(self.clear_button)
        self.pushButtonDelete.clicked.connect(self.delete_button)
        self.pushButtonDecide.clicked.connect(self.decide_button)
        self.pushButtonModify.clicked.connect(self.modify_button)

        # Search Input
        self.lineEditSearch.textChanged.connect(self.search)

        self.refresh_question_list()

    def search(self):
        search_string = self.lineEditSearch.text()
        if not search_string:
                # Show original
            self.refresh_question_list()
        else:
            self.clearQuestionList()
            for question in self.question_list:
                if fnmatch.fnmatch(question.string, "*{}*".format(search_string)):
                    self.listWidgetQuestions.addItem(question.string)

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
        self.clearQuestionList()
        self.lineEditQuestion.clear()
        self.lineEditQuestion.setFocus()

    def clearQuestionList(self):
        while self.listWidgetQuestions.count() > 0:
            self.listWidgetQuestions.takeItem(0)

    def decide_button(self):
        row = self.listWidgetQuestions.selectedIndexes()
        if(row):
            question_string = self.listWidgetQuestions.currentItem().text()
            question = self.sql_helper.get_question_string(question_string)
            option_index = random.randint(0, len(question.options) - 1)
            option = question.options[option_index].string
            reply = "Decision: \n\n{}".format(option)
            QMessageBox.question(self, question.string, reply, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

    def delete_button(self):
        row = self.listWidgetQuestions.selectedIndexes()
        if(row):
            question_string = self.listWidgetQuestions.currentItem().text()
            self.sql_helper.remove_question_string(question_string)
            self.refresh_question_list()
            self.search()
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

    def modify_button(self):
        row = self.listWidgetQuestions.selectedIndexes()
        if (row):
            question_string = self.listWidgetQuestions.currentItem().text()
            question = self.sql_helper.get_question_string(question_string)
            dialog = EditOptionDialog(question, self.sql_helper)
            if dialog.exec_() == QDialog.Accepted:
                self.refresh_question_list()
                self.search()
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

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


class EditOptionDialog(QDialog, EditOptionDialog.Ui_Dialog):
    def __init__(self, question, sql_helper, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.sql_helper = sql_helper
        self.question = question
        self.lineEditDecision.setText(question.string)
        self.option_labels = []
        self.option_line_edits = []
        for i, option in enumerate(question.options):
            self.option_labels.append(QLabel("Option {}:".format(i)))
            self.option_line_edits.append(QLineEdit())
            self.option_line_edits[i].setText(question.options[i].string)

            HLayout = QHBoxLayout()
            HLayout.addWidget(self.option_labels[i])
            HLayout.addWidget(self.option_line_edits[i])

            self.verticalLayoutOptions.addLayout(HLayout)

    def accept(self):
        self.sql_helper.update_question(self.question.id, self.lineEditDecision.text())
        for i, option in enumerate(self.question.options):
            self.sql_helper.update_option(option.id, self.option_line_edits[i].text())
        super(EditOptionDialog, self).accept()

    def reject(self):
        super(EditOptionDialog, self).reject()


app = QApplication(sys.argv)
program_ui = ProgramUI()
sys.exit(app.exec_())
