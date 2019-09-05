from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox


class QLabelClickable(QLabel):

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
        print("Clicked")

    def mouseReleaseEvent(self, event):
        pass

    def mouseDoubleclickedkEvent(self, event):
        pass

    def performSingleclickedkAction(self):
        pass
