import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

import data_base


class Save_Resume(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(950, 800)
        dialog.setStyleSheet("background-color: rgb(61, 72, 131);")
        self.lineEdit_full_name = QtWidgets.QLineEdit(dialog)
        self.lineEdit_full_name.setGeometry(QtCore.QRect(20, 10, 281, 71))
        self.lineEdit_full_name.setStyleSheet("border: 2px solid rgb(85, 85, 255);\n"
                                              "border-radius: 20px;\n"
                                              "background-color: rgb(203, 210, 255)\n"
                                              " \n"
                                              "")
        self.lineEdit_full_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.lineEdit_date_of_birth = QtWidgets.QLineEdit(dialog)
        self.lineEdit_date_of_birth.setGeometry(QtCore.QRect(340, 10, 281, 71))
        self.lineEdit_date_of_birth.setStyleSheet("border: 2px solid rgb(85, 85, 255);\n"
                                                  "border-radius: 20px;\n"
                                                  "background-color: rgb(203, 210, 255)\n"
                                                  " ")
        self.lineEdit_date_of_birth.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_date_of_birth.setObjectName("lineEdit_date_of_birth")
        self.lineEdit_phone_number = QtWidgets.QLineEdit(dialog)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(650, 10, 281, 71))
        self.lineEdit_phone_number.setStyleSheet("border: 2px solid rgb(85, 85, 255);\n"
                                                 "border-radius: 20px;\n"
                                                 "background-color: rgb(203, 210, 255)\n"
                                                 " ")
        self.lineEdit_phone_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")
        self.btn_back = QtWidgets.QPushButton(dialog)
        self.btn_back.setGeometry(QtCore.QRect(640, 710, 271, 81))
        self.btn_back.setStyleSheet("color: rgb(163, 201, 254);\n"
                                    "font: 22pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(100, 109, 156);\n"
                                    "border-radius: 30px;\n"
                                    "border: 2px solid rgb(111, 132, 238);")
        self.btn_back.setObjectName("btn_back")
        self.textEdit_input_resume = QtWidgets.QTextEdit(dialog)
        self.textEdit_input_resume.setGeometry(QtCore.QRect(20, 90, 911, 611))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.textEdit_input_resume.setFont(font)
        self.textEdit_input_resume.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_input_resume.setStyleSheet("border: 2px solid rgb(85, 85, 255);\n"
                                                 "border-radius: 20px;\n"
                                                 "background-color: rgb(203, 210, 255)\n"
                                                 " ")
        self.textEdit_input_resume.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_input_resume.setObjectName("textEdit_input_resume")
        self.btn_save = QtWidgets.QPushButton(dialog)
        self.btn_save.setGeometry(QtCore.QRect(40, 710, 271, 81))
        self.btn_save.setStyleSheet("color: rgb(163, 201, 254);\n"
                                    "font: 22pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(100, 109, 156);\n"
                                    "border-radius: 30px;\n"
                                    "border: 2px solid rgb(111, 132, 238);")
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

        # Подключение к бд
        self.db = sqlite3.connect("C:\\Users\\voyte\\Desktop\\Python Progects\\Hacaton\\_resume.db")
        self.cursor = self.db.cursor()

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.lineEdit_full_name.setPlaceholderText(_translate("dialog", "full name"))
        self.lineEdit_date_of_birth.setPlaceholderText(_translate("dialog", "date of birth "))
        self.lineEdit_phone_number.setPlaceholderText(_translate("dialog", "phone number"))
        self.btn_back.setText(_translate("dialog", "back"))
        self.btn_save.setText(_translate("dialog", "save"))

    def save_info(self):

        resume = self.textEdit_input_resume.toPlainText()
        name = self.lineEdit_full_name.text()
        date_of_birth = self.lineEdit_date_of_birth.text()
        phone = self.lineEdit_phone_number.text()

        data_base.input_resume_in_bd(self.cursor, self.db, name, date_of_birth, phone, resume)

        data_base.show_data_in_bd(self.cursor)

        self.db.commit()
        self.db.close()
