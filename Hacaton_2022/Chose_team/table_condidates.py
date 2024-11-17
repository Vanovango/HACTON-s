import sqlite3

import data_base
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from task_form import Task_wind


class Table(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(861, 706)
        Dialog.setStyleSheet("color: rgb(163, 201, 254);\n"
                             "background-color: rgb(61, 72, 131);\n"
                             "border-radius: 30px")
        self.pushButto_show_button = QtWidgets.QPushButton(Dialog)
        self.pushButto_show_button.setGeometry(QtCore.QRect(250, 620, 381, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButto_show_button.setFont(font)
        self.pushButto_show_button.setStyleSheet("color: rgb(163, 201, 254);\n"
                                                 "font: 10pt \"MS Shell Dlg 2\";\n"
                                                 "background-color: rgb(100, 109, 156);\n"
                                                 "border-radius: 30px;\n"
                                                 "border: 2px solid rgb(111, 132, 238);")
        self.pushButto_show_button.setObjectName("pushButto_show_button")
        self.table_of_condidates = QtWidgets.QTableWidget(Dialog)
        self.table_of_condidates.setGeometry(QtCore.QRect(20, 20, 820, 580))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_of_condidates.setFont(font)
        self.table_of_condidates.setStyleSheet("color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(120, 131, 186);")
        self.table_of_condidates.setObjectName("table_of_condidates")

        # settings of table
        self.table_of_condidates.setColumnCount(16)
        self.table_of_condidates.setRowCount(0)
        self.table_of_condidates.setHorizontalHeaderLabels(
            ['ФИО', 'Дата рождения', 'Номер телефона', 'Программирование',
             'Физика', 'Математика', 'Инженерия', 'Юр. знания', 'Аналитика',
             'Организация работы', 'Коммуникабельность',
             'Самостоятельность', 'Стрессоустойчивость', 'Инициативность',
             'Физическая подготовка', 'Резюме'])

        self.table_of_condidates.setColumnWidth(0, 200)
        self.table_of_condidates.setColumnWidth(1, 100)
        self.table_of_condidates.setColumnWidth(2, 150)
        self.table_of_condidates.setColumnWidth(3, 150)
        self.table_of_condidates.setColumnWidth(9, 150)
        self.table_of_condidates.setColumnWidth(10, 150)
        self.table_of_condidates.setColumnWidth(11, 150)
        self.table_of_condidates.setColumnWidth(12, 150)
        self.table_of_condidates.setColumnWidth(14, 150)
        self.table_of_condidates.setColumnWidth(15, 500)

        # Подключение к бд
        self.db = sqlite3.connect("C:\\Users\\voyte\\Desktop\\Python Progects\\Hacaton\\_resume.db")
        self.cursor = self.db.cursor()

        self.data = []
        self.task_wind = Task_wind()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButto_show_button.setText(_translate("Dialog", "show the schedule of applicants"))

    def append_data(self):
        # Creating items of table

        for person_inf in data_base.show_data_in_bd(self.cursor):
            tmp = {
                'name': person_inf[0],
                'birth': person_inf[1],
                'phone': person_inf[2],
                'programming': person_inf[3],
                'physics': person_inf[4],
                'mathematics': person_inf[5],
                'engineer': person_inf[6],
                'lawyer': person_inf[7],
                'analytics': person_inf[8],
                'work_organization': person_inf[9],
                'sociability': person_inf[10],
                'independence': person_inf[11],
                'stress_resistance': person_inf[12],
                'initiative': person_inf[13],
                'physical_abilities': person_inf[14],
                'resume': person_inf[15]
            }

            self.data.append(tmp)

    def show_un_sort_data(self):

        for pice_of_data in self.data:
            row_index = self.table_of_condidates.rowCount()
            self.table_of_condidates.insertRow(row_index)

            self.table_of_condidates.setItem(row_index, 0, QTableWidgetItem(pice_of_data['name']))
            self.table_of_condidates.setItem(row_index, 1, QTableWidgetItem(pice_of_data['birth']))
            self.table_of_condidates.setItem(row_index, 2, QTableWidgetItem(pice_of_data['phone']))
            self.table_of_condidates.setItem(row_index, 3, QTableWidgetItem(pice_of_data['programming']))
            self.table_of_condidates.setItem(row_index, 4, QTableWidgetItem(pice_of_data['physics']))
            self.table_of_condidates.setItem(row_index, 5, QTableWidgetItem(pice_of_data['mathematics']))
            self.table_of_condidates.setItem(row_index, 6, QTableWidgetItem(pice_of_data['engineer']))
            self.table_of_condidates.setItem(row_index, 7, QTableWidgetItem(pice_of_data['lawyer']))
            self.table_of_condidates.setItem(row_index, 8, QTableWidgetItem(pice_of_data['analytics']))
            self.table_of_condidates.setItem(row_index, 9, QTableWidgetItem(pice_of_data['work_organization']))
            self.table_of_condidates.setItem(row_index, 10, QTableWidgetItem(pice_of_data['sociability']))
            self.table_of_condidates.setItem(row_index, 11, QTableWidgetItem(pice_of_data['independence']))
            self.table_of_condidates.setItem(row_index, 12, QTableWidgetItem(pice_of_data['stress_resistance']))
            self.table_of_condidates.setItem(row_index, 13, QTableWidgetItem(pice_of_data['initiative']))
            self.table_of_condidates.setItem(row_index, 14, QTableWidgetItem(pice_of_data['physical_abilities']))
            self.table_of_condidates.setItem(row_index, 15, QTableWidgetItem(pice_of_data['resume']))

    def show_sorted_data(self):
        self.task_wind.sort_list()
