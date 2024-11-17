import data_base
from PyQt5 import QtCore, QtGui, QtWidgets


class Task_wind(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(860, 750)
        Dialog.setStyleSheet("color: rgb(163, 201, 254);\n"
                             "background-color: rgb(61, 72, 131);\n"
                             "border-radius: 30px rgb(203, 210, 255)")
        self.textEdit_enter_task = QtWidgets.QTextEdit(Dialog)
        self.textEdit_enter_task.setGeometry(QtCore.QRect(40, 150, 800, 380))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.textEdit_enter_task.setFont(font)
        self.textEdit_enter_task.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_enter_task.setStyleSheet("color: rgb(0,0,0);\n"
                                               "border: 2px solid rgb(85, 85, 255);\n"
                                               "border-radius: 20px;\n"
                                               "background-color: rgb(203, 210, 255)\n"
                                               " ")
        self.textEdit_enter_task.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_enter_task.setObjectName("textEdit_enter_task")
        self.top_label = QtWidgets.QLabel(Dialog)
        self.top_label.setGeometry(QtCore.QRect(230, 30, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet("font-color: rgb(132, 186, 254)")
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_label.setObjectName("top_label")
        self.pushButton_create_team = QtWidgets.QPushButton(Dialog)
        self.pushButton_create_team.setGeometry(QtCore.QRect(300, 630, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_create_team.setFont(font)
        self.pushButton_create_team.setStyleSheet("color: rgb(163, 201, 254);\n"
                                                  "font: 22pt \"MS Shell Dlg 2\";\n"
                                                  "background-color: rgb(100, 109, 156);\n"
                                                  "border-radius: 30px;\n"
                                                  "border: 2px solid rgb(111, 132, 238);")
        self.pushButton_create_team.setObjectName("pushButton_create_team")
        self.lineEdit_number_of_people = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_number_of_people.setGeometry(QtCore.QRect(320, 550, 231, 51))
        self.lineEdit_number_of_people.setStyleSheet("    border: 2px solid rgb(85, 85, 255);\n"
                                                     "    border-radius: 20px;\n"
                                                     "    background-color: rgb(114, 118, 143)\n"
                                                     "\n"
                                                     "")
        self.lineEdit_number_of_people.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_number_of_people.setObjectName("lineEdit_number_of_people")
        self.textEdit_enter_task.raise_()
        self.pushButton_create_team.raise_()
        self.lineEdit_number_of_people.raise_()
        self.top_label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.top_label.setText(_translate("Dialog", "Enter the assigned task"))
        self.pushButton_create_team.setText(_translate("Dialog", "create team"))
        self.lineEdit_number_of_people.setPlaceholderText(_translate("Dialog", "number of people in the team"))

    def sort_list(self):
        task = self.textEdit_enter_task.toPlainText()
        main_skil = data_base.find_skil_for_task(task)
        print(main_skil)
