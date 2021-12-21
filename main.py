#########################################################################################################
#                       This Program saves urls and filepaths for later use.                            #
#               Files can be selected by pressing the fileButton, which opens a filedialog.             #
#                       Urls can be copied into the url-box, one url per line.                          #
#                   Later, Files and Urls are opened by pressing the sessionbutton.                     #
#########################################################################################################

import sys
from qtpy import QtWidgets
import subprocess
import webbrowser
from ui.mainwindow import Ui_MainWindow
#from ui.extendedStyles import extendStyles



###########################################################

class MainWindow(QtWidgets.QMainWindow):

### Constructor ###
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ### Styles ###
        self.ui.centralWidget.setStyleSheet("background-color:#666666")
        self.ui.saveButton.setStyleSheet("background-color:#2f2f2f; color:#e1e1e1")
        self.ui.filedialog.setStyleSheet("background-color:#2f2f2f; color:#e1e1e1")
        self.ui.deleteFilesButton.setStyleSheet("background-color:#2f2f2f; color:#e1e1e1")
        self.ui.deleteUrlsButton.setStyleSheet("background-color:#2f2f2f; color:#e1e1e1")
        self.ui.label.setStyleSheet("color:#e1e1e1")
        self.ui.fileBox.setStyleSheet("background-color:#2f2f2f; color:#e1e1e1")
        self.ui.urlBox.setStyleSheet("background-color:#2f2f2f; color:#e1e1e1")
        self.ui.selectButton.setStyleSheet("background-color:#2f2f2f; color:#e1e1e1")
        ##############

        self.setWindowTitle("Session Saver")
        self.ui.statusBar.hide()
        self.ui.mainToolBar.hide()

        self.ui.filedialog.clicked.connect(self.openFileDialog)
        self.ui.saveButton.clicked.connect(self.onSave)
        self.ui.selectButton.clicked.connect(self.onSelect)
        self.ui.deleteFilesButton.clicked.connect(self.onDeleteFiles)
        self.ui.deleteUrlsButton.clicked.connect(self.onDeleteUrls)

        with open("sessionfiles.txt", "r") as file:
            for line in file:
                self.ui.fileBox.append(line.strip())

        with open("session_urls.txt", "r") as file:
            for line in file:
                self.ui.urlBox.append(line.strip())





### Functions ###
    def onSelect(self):
        # Opens sessionfiles.txt and opens each file written in it. One file per line.
        with open("sessionfiles.txt", "r") as file:
            for line in file:
                subprocess.Popen(line.strip(), shell = True)

        # Opens session_urls.txt and opens each url written in it. One url per line.
        with open("session_urls.txt", "r") as file:
            for line in file:
                webbrowser.open_new_tab(line.strip())

    # Saves filepaths and urls txt files "sessionfiles.txt" and "session_urls.txt".
    def onSave(self):
        with open("sessionfiles.txt", "w", newline="") as file:
            file.write(self.ui.fileBox.toPlainText())

        with open("session_urls.txt", "w", newline = "") as file:
            file.write(self.ui.urlBox.toPlainText())

    def onDeleteFiles(self):
        self.ui.fileBox.clear()

    def onDeleteUrls(self):
        self.ui.urlBox.clear()

    def openFileDialog(self):
        filenames = QtWidgets.QFileDialog.getOpenFileNames(self, "Select File", "C:/Users/Jermaine/Documents/")
        for file in filenames[0]:
            self.ui.fileBox.append(file)


###########################################################

app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")

window = MainWindow()
window.show()

sys.exit(app.exec_())