from PyQt5 import QtCore, QtGui, QtWidgets


class Start_wind(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(737, 570)
        Dialog.setStyleSheet("color: rgb(163, 201, 254);\n"
"background-color: rgb(61, 72, 131);\n"
"border-radius: 30px")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 501, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_show_list = QtWidgets.QPushButton(Dialog)
        self.btn_show_list.setGeometry(QtCore.QRect(370, 340, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_show_list.setFont(font)
        self.btn_show_list.setStyleSheet("color: rgb(163, 201, 254);\n"
"background-color: rgb(100, 109, 156);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(111, 132, 238);")
        self.btn_show_list.setObjectName("pushButton_2")
        self.btn_add_task = QtWidgets.QPushButton(Dialog)
        self.btn_add_task.setGeometry(QtCore.QRect(160, 340, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add_task.setFont(font)
        self.btn_add_task.setStyleSheet("color: rgb(163, 201, 254);\n"
"background-color: rgb(100, 109, 156);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(111, 132, 238);")
        self.btn_add_task.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CT v0.1"))
        self.label_2.setText(_translate("Dialog", "Create your team!"))
        self.label_3.setText(_translate("Dialog", "v0.1"))
        self.btn_show_list.setText(_translate("Dialog", "Show list"))
        self.btn_add_task.setText(_translate("Dialog", "Add task"))




