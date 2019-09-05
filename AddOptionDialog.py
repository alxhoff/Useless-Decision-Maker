# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_option_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 293)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelOption = QtWidgets.QLabel(Dialog)
        self.labelOption.setObjectName("labelOption")
        self.horizontalLayout.addWidget(self.labelOption)
        self.lineEditOption = QtWidgets.QLineEdit(Dialog)
        self.lineEditOption.setText("")
        self.lineEditOption.setObjectName("lineEditOption")
        self.horizontalLayout.addWidget(self.lineEditOption)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonAddOption = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddOption.setObjectName("pushButtonAddOption")
        self.horizontalLayout_2.addWidget(self.pushButtonAddOption)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listViewOptions = QtWidgets.QListView(Dialog)
        self.listViewOptions.setObjectName("listViewOptions")
        self.verticalLayout.addWidget(self.listViewOptions)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelTitle.setText(_translate("Dialog", "Add Question Options"))
        self.labelOption.setText(_translate("Dialog", "Option:"))
        self.lineEditOption.setPlaceholderText(_translate("Dialog", " Add option text"))
        self.pushButtonAddOption.setText(_translate("Dialog", "Add"))
