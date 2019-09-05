
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import StartScreen
import QuestionScreen


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
        print("response")


class StartScreen(QMainWindow, StartScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class QuestionScreen(QMainWindow, QuestionScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)
program_ui = ProgramUI()
app.exec_()
