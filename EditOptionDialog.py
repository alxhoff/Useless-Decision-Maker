# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/edit_option.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelDecision = QtWidgets.QLabel(Dialog)
        self.labelDecision.setObjectName("labelDecision")
        self.horizontalLayout.addWidget(self.labelDecision)
        self.lineEditDecision = QtWidgets.QLineEdit(Dialog)
        self.lineEditDecision.setObjectName("lineEditDecision")
        self.horizontalLayout.addWidget(self.lineEditDecision)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditOption = QtWidgets.QLineEdit(Dialog)
        self.lineEditOption.setObjectName("lineEditOption")
        self.horizontalLayout_2.addWidget(self.lineEditOption)
        self.pushButtonAddOption = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddOption.setObjectName("pushButtonAddOption")
        self.horizontalLayout_2.addWidget(self.pushButtonAddOption)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutOptions = QtWidgets.QVBoxLayout()
        self.verticalLayoutOptions.setObjectName("verticalLayoutOptions")
        self.verticalLayout.addLayout(self.verticalLayoutOptions)
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
        self.label.setText(_translate("Dialog", "Edit Decision"))
        self.labelDecision.setText(_translate("Dialog", "Decision:"))
        self.label_2.setText(_translate("Dialog", "New Option:"))
        self.lineEditOption.setPlaceholderText(_translate("Dialog", "Add new option here"))
        self.pushButtonAddOption.setText(_translate("Dialog", "Add"))
