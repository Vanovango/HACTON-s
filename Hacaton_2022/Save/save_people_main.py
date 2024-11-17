from PyQt5 import QtCore, QtGui, QtWidgets


class Main_save_WIND(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 617)
        font = QtGui.QFont()
        font.setPointSize(36)
        Dialog.setFont(font)
        Dialog.setStyleSheet("color: rgb(163, 201, 254);\n"
                             "background-color: rgb(61, 72, 131);\n"
                             "border-radius: 30px")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-60, 130, 891, 241))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 291, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 380, 181, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(163, 201, 254);\n"
                                      "font: 22pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(100, 109, 156);\n"
                                      "border-radius: 30px;\n"
                                      "border: 2px solid rgb(111, 132, 238);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Fill out the form to add yourself to the database"))
        self.label_2.setText(_translate("Dialog", "Hello!"))
        self.pushButton.setText(_translate("Dialog", "fill it!"))
