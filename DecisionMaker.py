import random
import time
import sys
import fnmatch

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import StartScreen
import DecisionScreen
import AddOptionDialog
import EditOptionDialog

from DatabaseHelper import SQLHelper
from Decision import Decision


class ProgramUI:

    def __init__(self):

        random.seed(time.time())

        self.start_screen = StartScreen()
        self.decision_screen = DecisionScreen()
        self.start_screen.show()

        # Connect start button to slot
        self.start_screen.labelStartButton.clicked.connect(self.StartScreenFinished)

    def StartScreenFinished(self):
        self.start_screen.close()
        self.decision_screen.show()


class StartScreen(QMainWindow, StartScreen.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)


class DecisionScreen(QMainWindow, DecisionScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.sql_helper = SQLHelper('decisions.db')

        self.decision_list = []
        self.refresh_decision_list()

        self.tmp_decision = Decision(None, "")

        self.search_list = []

        # Buttons
        self.pushButtonAdd.clicked.connect(self.add_decision_button)
        self.pushButtonAddOptions.clicked.connect(self.add_option_button)
        self.pushButtonClear.clicked.connect(self.clear_button)
        self.pushButtonDelete.clicked.connect(self.delete_button)
        self.pushButtonDecide.clicked.connect(self.decide_button)
        self.pushButtonModify.clicked.connect(self.modify_button)

        # Search Input
        self.lineEditSearch.textChanged.connect(self.search)

        self.refresh_decision_list()

    def search(self):
        search_string = self.lineEditSearch.text()
        if not search_string:
                # Show original
            self.refresh_decision_list()
        else:
            self.clearDecisionList()
            for decision in self.decision_list:
                if fnmatch.fnmatch(decision.string, "*{}*".format(search_string)):
                    self.listWidgetDecisions.addItem(decision.string)

    def add_option_button(self):
        dialog = AddOptionDialog(self.tmp_decision)
        self.listWidgetOptions.clear()
        if dialog.exec_() == QDialog.Accepted:
            for option in self.tmp_decision.options:
                self.listWidgetOptions.addItem(option)

    def add_decision_button(self):
        self.tmp_decision.string = self.lineEditDecision.text()
        if self.tmp_decision.string == "":
            QMessageBox.warning(self, "Missing parameter", "Please add a valid decision decision!")
            return

        if len(self.tmp_decision.options) < 2:
            QMessageBox.warning(self, "Missing parameter", "You need more options!")
            return

        self.sql_helper.add_decision_object(self.tmp_decision)
        self.tmp_decision = Decision(None, "")

        self.lineEditDecision.clear()
        self.listWidgetOptions.clear()

        self.refresh_decision_list()
        self.lineEditDecision.setFocus()

    def clear_button(self):
        self.tmp_decision.clear()
        self.clearDecisionList()
        self.lineEditDecision.clear()
        self.lineEditDecision.setFocus()

    def clearDecisionList(self):
        while self.listWidgetDecisions.count() > 0:
            self.listWidgetDecisions.takeItem(0)

    def decide_button(self):
        row = self.listWidgetDecisions.selectedIndexes()
        if(row):
            decision_string = self.listWidgetDecisions.currentItem().text()
            decision = self.sql_helper.get_decision_string(decision_string)
            option_index = random.randint(0, len(decision.options) - 1)
            option = decision.options[option_index].string
            reply = "Decision: \n\n{}".format(option)
            QMessageBox.question(self, decision.string, reply, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

    def delete_button(self):
        row = self.listWidgetDecisions.selectedIndexes()
        if(row):
            decision_string = self.listWidgetDecisions.currentItem().text()
            self.sql_helper.remove_decision_string(decision_string)
            self.refresh_decision_list()
            self.search()
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

    def modify_button(self):
        row = self.listWidgetDecisions.selectedIndexes()
        if (row):
            decision_string = self.listWidgetDecisions.currentItem().text()
            decision = self.sql_helper.get_decision_string(decision_string)
            dialog = EditOptionDialog(decision, self.sql_helper)
            if dialog.exec_() == QDialog.Accepted:
                self.refresh_decision_list()
                self.search()
        else:
            QMessageBox.warning(self, "", "Decision must be selected first", QMessageBox.Ok)

    def refresh_decision_list(self):
        self.listWidgetDecisions.clear()
        self.decision_list = self.sql_helper.get_all_decisions()

        for decision in self.decision_list:
            self.listWidgetDecisions.addItem(decision.string)

        self.listWidgetDecisions.show()


class AddOptionDialog(QDialog, AddOptionDialog.Ui_Dialog):

    def __init__(self, decision, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        for option in decision.options:
            self.listWidgetOptions.addItem(option)

        self.decision = decision

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
        self.decision.options = self.option_list
        super(AddOptionDialog, self).accept()

    def reject(self):
        super(AddOptionDialog, self).reject()


class EditOptionDialog(QDialog, EditOptionDialog.Ui_Dialog):
    def __init__(self, decision, sql_helper, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.sql_helper = sql_helper
        self.decision = decision
        self.lineEditDecision.setText(decision.string)
        self.option_labels = []
        self.option_line_edits = []
        for i, option in enumerate(decision.options):
            self.option_labels.append(QLabel("Option {}:".format(i)))
            self.option_line_edits.append(QLineEdit())
            self.option_line_edits[i].setText(decision.options[i].string)

            HLayout = QHBoxLayout()
            HLayout.addWidget(self.option_labels[i])
            HLayout.addWidget(self.option_line_edits[i])

            self.verticalLayoutOptions.addLayout(HLayout)

    def accept(self):
        self.sql_helper.update_decision(self.decision.id, self.lineEditDecision.text())
        for i, option in enumerate(self.decision.options):
            self.sql_helper.update_option(option.id, self.option_line_edits[i].text())
        super(EditOptionDialog, self).accept()

    def reject(self):
        super(EditOptionDialog, self).reject()


app = QApplication(sys.argv)
program_ui = ProgramUI()
sys.exit(app.exec_())
