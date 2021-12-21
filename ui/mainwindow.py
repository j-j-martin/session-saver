# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 365)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filedialog = QtWidgets.QPushButton(self.centralWidget)
        self.filedialog.setObjectName("filedialog")
        self.horizontalLayout_2.addWidget(self.filedialog)
        self.deleteFilesButton = QtWidgets.QPushButton(self.centralWidget)
        self.deleteFilesButton.setObjectName("deleteFilesButton")
        self.horizontalLayout_2.addWidget(self.deleteFilesButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.deleteUrlsButton = QtWidgets.QPushButton(self.centralWidget)
        self.deleteUrlsButton.setObjectName("deleteUrlsButton")
        self.horizontalLayout_2.addWidget(self.deleteUrlsButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileBox = QtWidgets.QTextEdit(self.centralWidget)
        self.fileBox.setObjectName("fileBox")
        self.horizontalLayout.addWidget(self.fileBox)
        self.urlBox = QtWidgets.QTextEdit(self.centralWidget)
        self.urlBox.setObjectName("urlBox")
        self.horizontalLayout.addWidget(self.urlBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.selectButton = QtWidgets.QPushButton(self.centralWidget)
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "Speichern"))
        self.filedialog.setText(_translate("MainWindow", "Dokumente Hinzufügen"))
        self.deleteFilesButton.setText(_translate("MainWindow", "Dokumente entfernen"))
        self.label.setText(_translate("MainWindow", "Url hinzufügen"))
        self.deleteUrlsButton.setText(_translate("MainWindow", "Urls entfernen"))
        self.selectButton.setText(_translate("MainWindow", "Session Wiederherstellen"))
