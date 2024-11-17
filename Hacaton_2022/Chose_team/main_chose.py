import sys

from PyQt5 import QtWidgets

from table_condidates import Table
from task_form import Task_wind
from visit_wind import Start_wind

app = QtWidgets.QApplication(sys.argv)
Start = QtWidgets.QDialog()
main = Start_wind()
main.setupUi(Start)
Start.show()


def open_task_wind():
    global Task
    Task = QtWidgets.QDialog()
    task_form = Task_wind()
    task_form.setupUi(Task)
    Task.show()
    Start.close()

    task_form.pushButton_create_team.clicked.connect(show_candidates)


def show_candidates():
    global Candidates
    Candidates = QtWidgets.QDialog()
    table_cond = Table()
    table_cond.setupUi(Candidates)
    Candidates.show()
    Task.close()

    table_cond.append_data()
    table_cond.show_sorted_data()


def open_list():
    global Candidates
    Candidates = QtWidgets.QDialog()
    table_cond = Table()
    table_cond.setupUi(Candidates)
    Candidates.show()
    Start.close()

    table_cond.append_data()
    table_cond.show_un_sort_data()


main.btn_add_task.clicked.connect(open_task_wind)
main.btn_show_list.clicked.connect(open_list)

sys.exit(app.exec_())
