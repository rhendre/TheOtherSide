# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ScreenUI/TheOtherSide_ConversationScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1519, 961)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ScreenUI\\../Images/The Other Side_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 80, 1251, 881))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../ScreenUI\\../../../Downloads/Conversation.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(21)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1080, 330, 351, 91))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser.setTabChangesFocus(True)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(660, 600, 181, 51))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser_2.setTabChangesFocus(True)
        self.textBrowser_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(750, 840, 311, 61))
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser_3.setTabChangesFocus(True)
        self.textBrowser_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(1280, 720, 181, 61))
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser_4.setTabChangesFocus(True)
        self.textBrowser_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(300, 660, 201, 71))
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser_5.setTabChangesFocus(True)
        self.textBrowser_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1390, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 110, 281, 851))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignVCenter)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 860, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1260, 10, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 70, 1581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 20, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ScreenUI\\../Images/directional-chevron-back-512.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 20, 961, 41))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setLineWidth(2)
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textEdit.setReadOnly(False)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setObjectName("textEdit")
        self.commandLinkButton.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        self.textBrowser_5.raise_()
        self.pushButton.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.line.raise_()
        self.textEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.textBrowser_2.anchorClicked['QUrl'].connect(self.listWidget.clearSelection)
        self.pushButton_3.clicked.connect(self.textBrowser.clear)
        self.pushButton_3.clicked.connect(self.textBrowser_2.clear)
        self.pushButton_3.clicked.connect(self.textBrowser_4.clear)
        self.pushButton_3.clicked.connect(self.textBrowser_3.clear)
        self.pushButton_3.clicked.connect(self.textBrowser_5.clear)
        self.pushButton_2.clicked.connect(self.listWidget.clearSelection)
        self.commandLinkButton.clicked.connect(self.commandLinkButton.showMenu)
        self.textBrowser.highlighted['QString'].connect(self.textEdit.insertPlainText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Question"))
        self.textBrowser_2.setPlaceholderText(_translate("MainWindow", "Option1"))
        self.textBrowser_3.setPlaceholderText(_translate("MainWindow", "Option2"))
        self.textBrowser_4.setPlaceholderText(_translate("MainWindow", "Option3"))
        self.textBrowser_5.setPlaceholderText(_translate("MainWindow", "Option4"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.listWidget.setSortingEnabled(True)
        self.label_2.setText(_translate("MainWindow", "Content List"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
