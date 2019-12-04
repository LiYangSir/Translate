# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translate.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 30, -1, 30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.translate_in = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.translate_in.setFont(font)
        self.translate_in.setObjectName("translate_in")
        self.horizontalLayout_2.addWidget(self.translate_in)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.translate_out = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.translate_out.setFont(font)
        self.translate_out.setReadOnly(True)
        self.translate_out.setObjectName("translate_out")
        self.horizontalLayout_2.addWidget(self.translate_out)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.translate_button.setFont(font)
        self.translate_button.setObjectName("translate_button")
        self.horizontalLayout_3.addWidget(self.translate_button, 0, QtCore.Qt.AlignLeft)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.copy_text_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_text_button.sizePolicy().hasHeightForWidth())
        self.copy_text_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.copy_text_button.setFont(font)
        self.copy_text_button.setObjectName("copy_text_button")
        self.horizontalLayout_3.addWidget(self.copy_text_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(4, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 938, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.translate_button.clicked.connect(MainWindow.translateText)
        self.copy_text_button.clicked.connect(MainWindow.copy_text)
        self.translate_in.textChanged.connect(MainWindow.translateText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translate"))
        self.label.setText(_translate("MainWindow", "Tea·Urn翻译"))
        self.translate_in.setPlaceholderText(_translate("MainWindow", "请输入要查询的英文或者中文，句子单词均可！"))
        self.translate_button.setText(_translate("MainWindow", "翻译"))
        self.copy_text_button.setText(_translate("MainWindow", "复制"))