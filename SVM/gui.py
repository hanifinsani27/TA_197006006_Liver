"""
GUI for liver prediction.
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont, QColor
from PyQt5.QtCore import Qt, QLine
from PyQt5.QtGui import QPixmap

import liver
from aboutUI import Ui_About
from user_guide import Ui_user_guide


class Menu(QWidget):

    def __init__(self) -> None:
        super(Menu, self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/health.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # header 1
        self.header1 = QLabel("LIVER CLASSIFICATION\n SUPPORT VECTOR MACHINE (RBF)")
        self.header1.setAlignment(Qt.AlignCenter)
        self.font1 = QFont()
        self.font1.setFamily("Times")
        self.font1.setPointSize(24)
        self.header1.setFont(self.font1)

        # gambar
        self.img_cover = QLabel("")
        self.img_cover.setAlignment(Qt.AlignCenter)
        self.img_cover.setObjectName("img_cover")
        self.img_cover.setPixmap(QtGui.QPixmap("img/insurance.png"))
        self.img_cover.setGeometry(QtCore.QRect(700, 190, 281, 121))

        # btn_predict
        self.btn_predict = QPushButton("START")
        self.btn_predict.setFixedWidth(160)
        self.btn_predict.setFixedHeight(41)
        self.fontpred = QFont()
        self.fontpred.setFamily("Calibri")
        self.fontpred.setPointSize(10)
        self.btn_predict.setFont(self.fontpred)
        self.btn_predict.move(100, 70)
        self.predicon = QtGui.QIcon()
        self.predicon.addPixmap(QtGui.QPixmap("img/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_predict.setIcon(self.predicon)
        self.btn_predict.setStyleSheet("QPushButton:hover { background-color: #FFE3BA; border: 1px solid #F89400; border-radius: 4px; }")

        # btn_exit
        self.btn_exit = QPushButton("EXIT")
        self.btn_exit.setFixedWidth(160)
        self.btn_exit.setFixedHeight(41)
        self.fontexit = QFont()
        self.fontexit.setFamily("Calibri")
        self.fontexit.setPointSize(10)
        self.btn_exit.setFont(self.fontpred)
        self.btn_exit.move(100, 70)
        self.exiticon = QtGui.QIcon()
        self.exiticon.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(self.exiticon)
        self.btn_exit.setStyleSheet("background-color: blue;")
        self.btn_exit.setStyleSheet("QPushButton:hover { background-color: #FFE3BA; border: 1px solid #F89400; border-radius: 4px; }")

        # btn_about
        self.btn_about = QPushButton("ABOUT")
        self.btn_about.setFixedWidth(160)
        self.btn_about.setFixedHeight(41)
        self.fontabout = QFont()
        self.fontabout.setFamily("Calibri")
        self.fontabout.setPointSize(10)
        self.btn_about.setFont(self.fontabout)
        self.btn_about.move(100, 70)
        self.abouticon = QtGui.QIcon()
        self.abouticon.addPixmap(QtGui.QPixmap("img/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(self.abouticon)
        self.btn_about.setStyleSheet("QPushButton:hover { background-color: #FFE3BA; border: 1px solid #F89400; border-radius: 4px; }")

        # btn_help
        self.btn_help = QPushButton("HELP")
        self.btn_help.setFixedWidth(160)
        self.btn_help.setFixedHeight(41)
        self.fonthelp = QFont()
        self.fonthelp.setFamily("Calibri")
        self.fonthelp.setPointSize(10)
        self.btn_help.setFont(self.fonthelp)
        self.btn_help.move(100, 70)
        self.helpicon = QtGui.QIcon()
        self.helpicon.addPixmap(QtGui.QPixmap("img/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(self.helpicon)
        self.btn_help.setStyleSheet("QPushButton:hover { background-color: #FFE3BA; border: 1px solid #F89400; border-radius: 4px; }")

        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h6 = QHBoxLayout()

        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.v3_box = QVBoxLayout()
        self.awal_hbox = QHBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.awalui()

    def awalui(self) -> None:
        self.v1_box.addWidget(self.header1)
        self.v1_box.setGeometry(QtCore.QRect())
        self.btn_predict.clicked.connect(Liver)
        self.btn_exit.clicked.connect(self.close)
        self.btn_about.clicked.connect(self.opnabout)
        self.btn_help.clicked.connect(self.opnhelp)
        self.v1_box.addWidget(self.img_cover)
        self.h2.addWidget(self.btn_predict)
        self.h2.addWidget(self.btn_about)
        self.h2.addWidget(self.btn_help)
        self.h2.addWidget(self.btn_exit)
        self.v1_box.addLayout(self.h2)
        self.final_hbox.addLayout(self.v1_box)
        self.setLayout(self.final_hbox)

    def mwindow(self) -> None:
        """ window features are set here and application is loaded into display"""
        self.setFixedSize(898, 422)
        self.setWindowTitle("Liver Classification")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/health.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.show()
        self.setStyleSheet("background: qradialgradient(cx: 0.5, cy: 0.5, fx: 0.5, fy: 0.5, radius: 1, stop: 0 ##DFDFDF, stop: 1 #FFA500);")

    def opnabout(self) -> None:
        self.About = QtWidgets.QWidget()
        self.ui_about = Ui_About()
        self.ui_about.setupUi(self.About)
        self.About.show()

    def opnhelp(self) -> None:
        self.user_guide = QtWidgets.QWidget()
        self.ui_guide = Ui_user_guide()
        self.ui_guide.setupUi(self.user_guide)
        self.user_guide.show()


class Liver(QWidget):

    def __init__(self) -> None:
        super(Liver, self).__init__()
        self.model_details = QLabel("Fill details and press submit to see details.")
        self.results = QLabel(" ")
        self.sub_head = QLabel("Patient's Details")
        self.cover = QLabel("KLASIFIKASI PENYAKIT LIVER\nMUHAMMAD HANIF INSANI\n197006006")
        self.sub_head.setFont(QFont("Roboto", 22, weight=QFont.Bold))
        self.cover.setAlignment(Qt.AlignCenter)
        self.cover.setFont(QFont("Roboto", 22, weight=QFont.Bold))
        self.report_subhead = QLabel("About")
        self.details = QLabel(
            "Sistem ini dirancang menggunakan Algoritma Support Vector Machine (RBF) classifier.\nDengan Hasil Akurasi: 76%\nData yang digunakan diambil dari website Kaggle.com.")

        # Buat QLabel untuk menampilkan gambar
        self.image_label = QLabel(self)
        pixmap = QPixmap("img/hearth1.png")  # Ganti dengan path ke gambar Anda
        self.image_label.setPixmap(pixmap)

        # Tentukan posisi atau letak gambar di sisi bawah kanan
        image_width = pixmap.width()
        image_height = pixmap.height()
        self.image_label.setGeometry(QtCore.QRect(580, 240, 281, 129))

        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()

        self.t1 = QLabel("Total Proteins:")
        self.t1.setFont(QFont("Roboto", 13, weight=QFont.Bold))
        self.t2 = QLabel("Albumin:")
        self.t2.setFont(QFont("Roboto", 13, weight=QFont.Bold))
        self.t3 = QLabel("Albumin_and_Globulin_Ratio:")
        self.t3.setFont(QFont("Roboto", 13, weight=QFont.Bold))

        self.r1 = QLabel("(0 - 9.6 g/L)")
        self.r2 = QLabel("(0 - 5.5 g/L)")
        self.r3 = QLabel("(0 - 2.8 g/L)")

        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h6 = QHBoxLayout()

        self.submit = QPushButton("SUBMIT")
        self.submit.setFixedWidth(100)
        self.submit.setFixedHeight(50)
        self.submit.setFont(QFont("Times", 11, weight=QFont.Bold))
        self.submit.setStyleSheet("color:blue;")

        self.clbtn = QPushButton("HAPUS")
        self.clbtn.setFixedWidth(100)
        self.clbtn.setFixedHeight(50)
        self.clbtn.setFont(QFont("font-family: Roboto", 11, weight=QFont.Bold))
        self.clbtn.setStyleSheet("color:red;")

        self.exit = QPushButton("KEMBALI")
        self.exit.setFixedWidth(100)
        self.exit.setFixedHeight(50)
        self.exit.setFont(QFont("Times", 11, weight=QFont.Bold))
        self.exit.setStyleSheet("color:red;")
        self.exit.move(100, 70)

        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.v3_box = QVBoxLayout()
        self.awal_hbox = QHBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.initui()


    def initui(self):
        """ The gui is created and widgets elements are set here """
        self.setFixedSize(898, 422)
        self.setWindowTitle("Liver Classification")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/health.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.show()
        self.show()
        self.v1_box.addWidget(self.sub_head)
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(5)
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())

        self.l1.setToolTip("0 - 9.6 g/L")
        self.l2.setToolTip("0 - 5.5 g/L")
        self.l3.setToolTip("0 - 2.8 g/L")

        self.l1.setFixedSize(50, 30)
        self.l2.setFixedSize(50, 30)
        self.l3.setFixedSize(50, 30)

        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)
        self.h1.addWidget(self.r1)
        self.v1_box.addLayout(self.h1)
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)
        self.h2.addWidget(self.r2)
        self.v1_box.addLayout(self.h2)
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)
        self.h3.addWidget(self.r3)
        self.v1_box.addLayout(self.h3)

        self.clbtn.clicked.connect(lambda: self.clfn())

        self.submit.clicked.connect(lambda: self.test_input())
        self.submit.setToolTip("Click to check if patient has liver disease")

        self.exit.clicked.connect(self.close)

        self.h6.addWidget(self.exit)
        self.h6.addWidget(self.clbtn)
        self.h6.addWidget(self.submit)
        self.v1_box.addLayout(self.h6)
        self.report_ui()
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacing(40)
        self.final_hbox.addLayout(self.v2_box)
        self.setLayout(self.final_hbox)
        self.show()

    def report_ui(self):
        self.v2_box.setSpacing(6)
        self.report_subhead.setAlignment(Qt.AlignCenter)
        self.report_subhead.setFont(QFont("Times", 24, weight=QFont.Bold))
        self.v2_box.addWidget(self.report_subhead)
        self.details.setFont(QFont("Arial", 14, weight=QFont.Bold))
        self.details.setAlignment(Qt.AlignLeft)
        self.details.setWordWrap(True)
        self.model_details.setWordWrap(True)
        self.v2_box.addWidget(self.details)
        self.results.setWordWrap(True)
        self.v2_box.addWidget(self.results)
        self.v2_box.addWidget(self.model_details)

    def clfn(self):
        """ clear all the text fields via clear button"""
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()

        self.report_subhead.setText("About")
        self.model_details.setText("Fill details and press submit to see details.")
        self.results.setText(" ")
        self.details.setText(
            "Sistem ini dirancang menggunakan Algoritma Support Vektor Machine (RBF) classifier.\nDengan Hasil Akurasi: 73%\nData yang digunakan diambil dari website Kaggle.com ")
        # print(self.frameGeometry().width())
        # print(self.frameGeometry().height())

    def test_input(self) -> None:
        """ test for liver"""
        my_dict = {"Total_Protiens": float(self.l1.text()), "Albumin": float(self.l2.text()),
                   "Albumin_and_Globulin_Ratio": float(self.l3.text())}
        output = liver.check_input(my_dict)
        # print(self.output)
        # self.setFixedSize(850, 342)
        self.report_subhead.setText("Reports")
        self.model_details.setText(
            "Sistem ini dirancang menggunakan Algoritma Support Vektor Machine (RBF) classifier.\nDengan Hasil Akurasi: 73%\nData yang digunakan diambil dari website Kaggle.com .")
        self.details.setText(
            "Total Protein: {} \nAlbumin: {}\nAlbumin_and_Globulin_Ratio: {}".format(
                self.l1.text(), self.l2.text(), self.l3.text()))

        if output == 0:
            self.results.setText(
                "Hasil diagnosa menyatakan pasien menderita penyakit liver.\nSegera melakukan perawatan di rumah sakit.")
        else:
            self.results.setText("Hasil diagnosa menyatakan pasien tidak menderita penyakit liver.")
        self.results.setFont(QFont("Arial", 14, weight=QFont.Bold))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a_window = Menu()
    a_window.mwindow()
    sys.exit(app.exec_())
