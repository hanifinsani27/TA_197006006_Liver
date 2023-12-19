from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(970, 500)
        About.setMinimumSize(QtCore.QSize(970, 500))
        About.setMaximumSize(QtCore.QSize(970, 500))
        About.setBaseSize(QtCore.QSize(970, 500))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        About.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/health.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(About)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 930, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.About_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.About_2.setFont(font)
        self.About_2.setAlignment(QtCore.Qt.AlignCenter)
        self.About_2.setObjectName("About_2")
        self.verticalLayout.addWidget(self.About_2)
        self.p1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p1.setFont(font)
        self.p1.setTextFormat(QtCore.Qt.PlainText)
        self.p1.setAlignment(QtCore.Qt.AlignLeft)
        self.p1.setObjectName("p1")
        self.verticalLayout.addWidget(self.p1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.label.setFont(font)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")
        # self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(About)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(370, 410, 281, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

        self.pushButton.clicked.connect(lambda: self.back(About))

    def back(self, About):
        About.hide()

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.About_2.setText(_translate("About", "About"))
        self.p1.setText(_translate("About", "Aplikasi ini dibuat dengan modul PyQt5 dan "
                                            "bahasa pemrograman Python 3.9.\n"
                                            "IDE yang digunakan yaitu PyCharm 2022.2 Community Edition.\n"
                                            "Model yang digunakan yaitu Algoritma C5.0 dengan akurasi 76%. "))
        self.label_2.setStyleSheet("font-size: 15px;")
        self.label_2.setText(_translate("About", "Nama Pembuat : Muhammad Hanif Insani\n"
                                                 "NPM : 197006006\n"
                                                 "Prodi : Informatika\n"
                                                 "Fakultas : Teknik\n"
                                                 "Universitas Siliwangi"))
        self.pushButton.setText(_translate("About", "Kembali"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui_about = Ui_About()
    ui_about.setupUi(About)
    About.show()
    sys.exit(app.exec_())
