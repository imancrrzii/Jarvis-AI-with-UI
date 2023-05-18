from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisMainGUI(object):
    def setupUi(self, JarvisMainGUI):
        JarvisMainGUI.setObjectName('Widget')
        JarvisMainGUI.resize(1280, 640)
        JarvisMainGUI.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.codingLabel = QtWidgets.QLabel(JarvisMainGUI)
        self.codingLabel.setGeometry(QtCore.QRect(0, 0, 291, 171))
        self.codingLabel.setStyleSheet("border:none;\n"
                                       "border-radius: 200px;\n"
                                       "background: transparent;")
        self.codingLabel.setText("")
        self.codingLabel.setPixmap(QtGui.QPixmap(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\B.G_Template_1.gif"))
        self.codingLabel.setScaledContents(True)
        self.codingLabel.setObjectName("codingLabel")

        self.ironmanLabel = QtWidgets.QLabel(JarvisMainGUI)
        self.ironmanLabel.setGeometry(QtCore.QRect(920, -20, 491, 761))
        self.ironmanLabel.setStyleSheet("border-radius: 200px;\n"
                                        "background: transparent;")
        self.ironmanLabel.setText("")
        self.ironmanLabel.setPixmap(QtGui.QPixmap(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\ironman-portrait.webp"))
        self.ironmanLabel.setScaledContents(True)
        self.ironmanLabel.setObjectName("ironmanLabel")

        self.arcLabel = QtWidgets.QLabel(JarvisMainGUI)
        self.arcLabel.setGeometry(QtCore.QRect(420, 80, 411, 391))
        self.arcLabel.setStyleSheet("border-radius: 200px;\n"
                                    "background: transparent;")
        self.arcLabel.setText("")
        self.arcLabel.setPixmap(QtGui.QPixmap(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\techcircle.gif"))
        self.arcLabel.setScaledContents(True)
        self.arcLabel.setObjectName("arcLabel")

        self.frame = QtWidgets.QFrame(JarvisMainGUI)
        self.frame.setGeometry(QtCore.QRect(10, 480, 1251, 231))
        self.frame.setStyleSheet("background:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.terminalInputBox = QtWidgets.QLineEdit(self.frame)
        self.terminalInputBox.setGeometry(QtCore.QRect(0, 200, 1101, 31))
        self.terminalInputBox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                            "background: transparent;\n"
                                            "font: 13pt \"Karisma\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-style: solid;\n"
                                            "border-width: 3px 3px 3px 3px;\n"
                                            "padding-left:5px;")
        self.terminalInputBox.setText("")
        self.terminalInputBox.setObjectName("terminalInputBox")

        self.enterButton = QtWidgets.QPushButton(self.frame)
        self.enterButton.setGeometry(QtCore.QRect(1020, 200, 71, 31))
        self.enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterButton.setStyleSheet("border-image: url(D:/python programs/TUGAS AKHIR/GUI files-20230328T090529Z-001/GUI files//enter.png);\n"
                                       "border-color: rgb(255, 255, 255);\n"
                                       "background-color: transparent;\n"
                                       "border-style: solid;\n"
                                       "border-left: 5px;\n"
                                       "")
        self.enterButton.setText("")
        self.enterButton.setFlat(False)
        self.enterButton.setObjectName("enterButton")

        self.terminalOutputBox = QtWidgets.QPlainTextEdit(self.frame)
        self.terminalOutputBox.setGeometry(QtCore.QRect(0, 0, 1101, 200))
        self.terminalOutputBox.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.terminalOutputBox.setMouseTracking(True)
        self.terminalOutputBox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                             "background: transparent;\n"
                                             "font: bold 12pt \"Cambria\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-style: solid;\n"
                                             "border-width: 1px 1px 1px 1px;\n"
                                             "padding-left:5px;")
        self.terminalOutputBox.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.terminalOutputBox.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.terminalOutputBox.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.terminalOutputBox.setReadOnly(True)
        self.terminalOutputBox.setPlainText("")
        self.terminalOutputBox.setOverwriteMode(True)
        self.terminalOutputBox.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse
        )
        self.terminalOutputBox.setCenterOnScroll(True)
        self.terminalOutputBox.setObjectName("terminalOutputBox")

        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(1120, 160, 130, 71))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("border-image: url(D:/python programs/TUGAS AKHIR/GUI files-20230328T090529Z-001/GUI files/exit(with border).png);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "background-color: transparent;\n"
                                      "border-style: solid;\n"
                                      "border-width: 5px 5px 5px 5px;\n"
                                      "")
        self.exitButton.setText("")
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")

        self.terminalInputBox.raise_()
        self.terminalOutputBox.raise_()
        self.exitButton.raise_()
        self.enterButton.raise_()

        self.loadingLabel = QtWidgets.QLabel(JarvisMainGUI)
        self.loadingLabel.setGeometry(QtCore.QRect(50, 190, 271, 261))
        self.loadingLabel.setStyleSheet("border-radius: 200px;\n"
                                        "background: transparent;")
        self.loadingLabel.setText("")
        self.loadingLabel.setPixmap(QtGui.QPixmap(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\tech loading-cropped.gif"))
        self.loadingLabel.setScaledContents(True)
        self.loadingLabel.setObjectName("loadingLabel")

        self.listeningLabel = QtWidgets.QLabel(JarvisMainGUI)
        self.listeningLabel.setGeometry(QtCore.QRect(59, 180, 250, 290))
        self.listeningLabel.setStyleSheet("border-radius: 200px;\n"
                                          "background: transparent;")
        self.listeningLabel.setText("")
        self.listeningLabel.setPixmap(QtGui.QPixmap(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\listening.gif"))
        self.listeningLabel.setScaledContents(True)
        self.listeningLabel.setObjectName("listeningLabel")

        self.jarvisSpeakingLabel = QtWidgets.QLabel(JarvisMainGUI)
        self.jarvisSpeakingLabel.setGeometry(QtCore.QRect(30, 175, 311, 291))
        self.jarvisSpeakingLabel.setStyleSheet("border-radius: 200px;\n"
                                               "background: transparent;")
        self.jarvisSpeakingLabel.setText("")
        self.jarvisSpeakingLabel.setPixmap(QtGui.QPixmap(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\speaking.gif"))
        self.jarvisSpeakingLabel.setScaledContents(True)
        self.jarvisSpeakingLabel.setObjectName("jarvisSpeakingLabel")

        self.codingLabel.raise_()
        self.ironmanLabel.raise_()
        self.arcLabel.raise_()
        self.frame.raise_()
        self.loadingLabel.raise_()
        self.listeningLabel.raise_()
        self.jarvisSpeakingLabel.raise_()

        self.retranslateUi(JarvisMainGUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisMainGUI)

    def retranslateUi(self, JarvisMainGUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisMainGUI.setWindowTitle(
            _translate("JarvisMainGUI", "JarvisMainGUI"))
        self.terminalInputBox.setPlaceholderText(
            _translate("JarvisMainGUI", "Enter Your Command"))
        self.terminalOutputBox.setPlaceholderText(
            _translate("JarvisMainGUI", "Terminal output is here"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    JarvisMainGUI = QtWidgets.QWidget()
    ui = Ui_JarvisMainGUI()
    ui.setupUi(JarvisMainGUI)
    JarvisMainGUI.show()
    sys.exit(app.exec_())
