import sys

from PyQt5 import QtWidgets

from save_people_main import Main_save_WIND
from save_person import Save_Resume

app = QtWidgets.QApplication(sys.argv)
Start_wind = QtWidgets.QDialog()
main = Main_save_WIND()
main.setupUi(Start_wind)
Start_wind.show()


def open_resume_field():
    global Resume
    Resume = QtWidgets.QDialog()
    form = Save_Resume()
    form.setupUi(Resume)
    Resume.show()
    Start_wind.close()

    def go_back():
        Start_wind.show()
        Resume.close()

    def push_btn_save():
        form.save_info()
        Start_wind.show()
        Resume.close()

    form.btn_back.clicked.connect(go_back)
    form.btn_save.clicked.connect(push_btn_save)


main.pushButton.clicked.connect(open_resume_field)

sys.exit(app.exec_())
