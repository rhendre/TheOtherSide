# Main Class for Backend Editor
# Has Instances of PollingScreen, Data Collection Screen, ShowCase Screen and Text Screen
# Ruchi_Hendre@2020
import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

from Editor.ConversationScreen import ConversationScreen
#from Editor.DataCollectionScreen import DataCollectionScreen
from Editor.PollingScreen import PollingScreen
from Editor.Screen1 import Screen1
from Editor.Screen2 import Screen2
from Editor.ShowCaseScreen import ShowCaseScreen
from Editor.UploadScreen import UploadScreen


def changeWindow(w1, w2):
    w1.close()
    w2.show()


def changeShowcaseWindow(w1, w2):
    w1.close()
    w2.listWidget.setEnabled(True)
    w2.Save.setEnabled(True)
    w2.Delete.setEnabled(True)
    w2.Upload.setEnabled(True)
    w2.CreateNewContent.setEnabled(True)
    w2.show()


#def changeDataCollectionScreen(w1, w2, template):
    #w2.canvas.axes.clear()
    #DataCollectionScreen.template = template
    #DataCollectionScreen.count = 0
    #w2.readFromJsonFile()
    #w1.hide()
    #w2.show()


def showWindow(w1, w2):
    w2.listWidget.setEnabled(False)
    w2.Save.setEnabled(False)
    w2.Delete.setEnabled(False)
    w2.Upload.setEnabled(False)
    w2.CreateNewContent.setEnabled(False)

    w1.setParent(w2)
    if w2.doubleClicked == 1:
        w1.loadImage(ShowCaseScreen.ImageFileName)
    else:
        w1.clearImage()

    if w2.doubleClicked == 1 or ShowCaseScreen.VideoFileName != '':
        w1.loadVideo(ShowCaseScreen.VideoFileName)
    elif ShowCaseScreen.VideoFileName != w2.VideoFileName:
        w1.clearVideo()
    elif ShowCaseScreen.VideoFileName == '' and w2.doubleClicked == 0:
        w1.clearVideo()


    w1.move(260, 140)

    w2.setWindowModality(QtCore.Qt.ApplicationModal)
    w1.show()


def labelText(self, MainWindow, value):
    if ShowCaseScreen.ImageFileName == "":
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Image is needed for the Showcase Template")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        x = msgBox.exec_()

    else:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Media Uploaded")
        msgBox.setWindowTitle("Success")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        x = msgBox.exec_()
        self.label_3.setText(str(value))
        MainWindow.close()

        self.listWidget.setEnabled(True)
        self.Save.setEnabled(True)
        self.Delete.setEnabled(True)
        self.Upload.setEnabled(True)
        self.CreateNewContent.setEnabled(True)
        self.show()


def main():
    path = os.path.dirname(sys.argv[0])
    print(os.path.dirname(sys.argv[0]))
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("QTextBrowser { background-color: white; border-radius: "
                      "10px;}")
    screen1 = Screen1()
    screen1.show()

    screen2 = Screen2()
    screen2DataCollection = Screen2()
    pollingScreen = PollingScreen()
    #DataCollectionScreen.template = "Polling"
    #dataCollectionScreen = DataCollectionScreen()
    showCaseScreen = ShowCaseScreen()
    uploadScreen = UploadScreen()
    conversationScreen = ConversationScreen()

    screen1.pushButton.clicked.connect(lambda: changeWindow(screen1, screen2))
    screen1.pushButton_2.clicked.connect(lambda: changeWindow(screen1, screen2DataCollection))

    #screen2DataCollection.pushButton_2.clicked.connect(
    #    lambda: changeDataCollectionScreen(screen2DataCollection, dataCollectionScreen, "Polling"))
   # screen2DataCollection.pushButton.clicked.connect(
       # lambda: changeDataCollectionScreen(screen2DataCollection, dataCollectionScreen, "Showcase"))
    #screen2DataCollection.pushButton_3.clicked.connect(
        #lambda: changeDataCollectionScreen(screen2DataCollection, dataCollectionScreen, "Text"))
    screen2.pushButton_2.clicked.connect(lambda: changeWindow(screen2, pollingScreen))
    screen2.pushButton.clicked.connect(lambda: changeWindow(screen2, showCaseScreen))
    screen2.commandLinkButton.clicked.connect(lambda: changeWindow(screen2, screen1))
    screen2DataCollection.commandLinkButton.clicked.connect(lambda: changeWindow(screen2, screen1))
    screen2.pushButton_3.clicked.connect(lambda: changeWindow(screen2, conversationScreen))

    pollingScreen.commandLinkButton.clicked.connect(lambda: changeWindow(pollingScreen, screen2))

    showCaseScreen.Upload.clicked.connect(lambda: showWindow(uploadScreen, showCaseScreen))

    uploadScreen.pushButton_3.clicked.connect(
        lambda: labelText(showCaseScreen, uploadScreen, UploadScreen.Video + "  " + UploadScreen.Image + "  uploaded"))

   # dataCollectionScreen.commandLinkButton.clicked.connect(lambda: changeWindow(dataCollectionScreen, screen1))

    conversationScreen.commandLinkButton.clicked.connect(lambda: changeWindow(conversationScreen, screen2))

    showCaseScreen.commandLinkButton.clicked.connect(lambda: changeWindow(showCaseScreen, screen2))

    uploadScreen.commandLinkButton.clicked.connect(lambda: changeShowcaseWindow(uploadScreen, showCaseScreen))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
