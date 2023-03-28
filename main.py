import sys
from PyQt5 import QtWidgets
from table import Table
from solution import Solution
from first_window import Ui_FirstWindow
from second_window import Ui_SecondWindow


t = Table()
s = Solution(t)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_FirstWindow(t, s, lambda: open_second_window())
ui.setupUi(MainWindow)
MainWindow.show()


def open_second_window():
    global SecondWindow
    SecondWindow = QtWidgets.QMainWindow()
    sw = Ui_SecondWindow(ui.t, ui.s)
    sw.setupUi(SecondWindow)
    MainWindow.close()
    SecondWindow.show()

    def return_to_first_window():
        SecondWindow.close()
        MainWindow.show()

    sw.push_button_back.clicked.connect(return_to_first_window)


sys.exit(app.exec_())
