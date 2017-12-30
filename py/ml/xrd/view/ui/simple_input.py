# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_input.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Input(object):
    def setupUi(self, Input):
        Input.setObjectName("Input")
        Input.resize(459, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Input.sizePolicy().hasHeightForWidth())
        Input.setSizePolicy(sizePolicy)
        self.buttonBox = QtWidgets.QDialogButtonBox(Input)
        self.buttonBox.setGeometry(QtCore.QRect(80, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.input_box = QtWidgets.QPlainTextEdit(Input)
        self.input_box.setGeometry(QtCore.QRect(20, 90, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_box.setFont(font)
        self.input_box.setPlainText("")
        self.input_box.setObjectName("input_box")
        self.infomation = QtWidgets.QLabel(Input)
        self.infomation.setGeometry(QtCore.QRect(20, 30, 421, 41))
        self.infomation.setObjectName("infomation")

        self.buttonBox.accepted.connect(Input.accept)
        self.buttonBox.rejected.connect(Input.reject)
        self.input_box.textChanged.connect(Input.textChanged)
