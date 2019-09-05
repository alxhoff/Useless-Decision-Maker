# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(100, 100, 100, 100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelStartButton = QLabelClickable(self.widget)
        self.labelStartButton.setText("")
        self.labelStartButton.setPixmap(QtGui.QPixmap("icon/start.png"))
        self.labelStartButton.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStartButton.setObjectName("labelStartButton")
        self.horizontalLayout.addWidget(self.labelStartButton)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionPreferenes = QtWidgets.QAction(MainWindow)
        self.actionPreferenes.setObjectName("actionPreferenes")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionPreferenes.setText(_translate("MainWindow", "Preferences"))
from qlabelclickable import QLabelClickable
