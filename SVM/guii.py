#!/usr/bin/env python3

"""
GUI for liver prediction.
"""
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt, QLine

import liver


class Menu(QWidget):

    def __init__(self) -> None:
        super(Menu, self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/health.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # header 1
        self.header1 = QLabel("LIVER CLASSIFICATION\n SUPPORT VECTOR MACHINE")
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

        # btn_predict
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
        self.v1_box.addWidget(self.img_cover)
        self.h2.addWidget(self.btn_exit)
        self.h2.addWidget(self.btn_predict)
        self.v1_box.addLayout(self.h2)
        self.final_hbox.addLayout(self.v1_box)
        self.setLayout(self.final_hbox)


class Liver(QWidget):

    def __init__(self) -> None:
        super(Liver, self).__init__()
        self.model_details = QLabel("Fill details and press submit to see details.")
        self.results = QLabel(" ")
        self.sub_head = QLabel("Patient's Details")
        self.cover = QLabel("KLASIFIKASI PENYAKIT LIVER\nMUHAMMAD FAJRI INSANI\n4516210028")
        self.sub_head.setFont(QFont("Times", 24, weight=QFont.Bold))
        self.cover.setAlignment(Qt.AlignCenter)
        self.cover.setFont(QFont("Times", 24, weight=QFont.Bold))
        self.report_subhead = QLabel("About")
        self.details = QLabel(
            "Sistem ini dirancang menggunakan Algoritma Support Vector Machine classifier.\nDengan Hasil Akurasi: 73%\nData yang digunakan diambil dari website Kaggle.com.")

        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()

        self.t1 = QLabel("Total Proteins:")
        self.t1.setFont(QFont("Times", 12, weight=QFont.Bold))
        self.t2 = QLabel("Albumin:")
        self.t2.setFont(QFont("Times", 12, weight=QFont.Bold))
        self.t3 = QLabel("Albumin_and_Globulin_Ratio:")
        self.t3.setFont(QFont("Times", 12, weight=QFont.Bold))

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
        self.submit.setFont(QFont("Times", 12, weight=QFont.Bold))
        self.submit.setStyleSheet("color:blue;")

        self.clbtn = QPushButton("HAPUS")
        self.clbtn.setFixedWidth(100)
        self.clbtn.setFixedHeight(50)
        self.clbtn.setFont(QFont("Times", 12, weight=QFont.Bold))
        self.clbtn.setStyleSheet("color:red;")

        self.exit = QPushButton("EXIT")
        self.exit.setFixedWidth(100)
        self.exit.setFixedHeight(50)
        self.exit.setFont(QFont("Times", 12, weight=QFont.Bold))
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
            "Sistem ini dirancang menggunakan Algoritma Support Vector Machine classifier.\nDengan Hasil Akurasi: 73%\nData yang digunakan diambil dari website Kaggle.com ")
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
            "Sistem ini dirancang menggunakan Algoritma Support Vector Machine classifier.\nDengan Hasil Akurasi: 73%\nData yang digunakan diambil dari website Kaggle.com .")
        self.details.setText(
            "Total Protein: {} \nAlbumin: {}\nAlbumin_and_Globulin_Ratio: {}".format(
                self.l1.text(), self.l2.text(), self.l3.text()))

        if output == 0:
            self.results.setText(
                "Hasil diagnosa menyatakan pasien menderita penyakit liver.\nSegera melakukan perawatan di rumah sakit.")
        else:
            self.results.setText("Hasil diagnosa menyatakan pasien tidak menderita penyakit liver.")
        self.results.setFont(QFont("Arial", 14, weight=QFont.Bold))

    def mwindow(self) -> None:
        """ window features are set here and application is loaded into display"""
        self.setFixedSize(898, 422)
        self.setWindowTitle("Liver Classification")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/health.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a_window = Liver()
    a_window.mwindow()
    sys.exit(app.exec_())
