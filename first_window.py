from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from table import Table
from solution import Solution


def negation_change(var):
    """Changing how the variable we use with negation looks like

    !<var> -> <var>̅
    """
    if var[1] == 'X':
        return 'X̅'
    if var[1] == 'Y':
        return 'Y̅'
    if var[1] == 'Z':
        return 'Z̅'


def tuple_to_string(tup):
    """Converting nested tuples representing conjunctors to a string"""
    str = '\n'
    if len(tup) == 1:
        for conjuctor in tup[0]:
            for var in conjuctor:
                if len(var) == 2:
                    str += negation_change(var)
                else:
                    str += var
            if conjuctor != tup[0][-1]:
                str += '  V  '
    else:
        for mdnf in tup:
            for conjuctor in mdnf:
                for var in conjuctor:
                    if len(var) == 2:
                        str += negation_change(var)
                    else:
                        str += var
                if conjuctor != mdnf[-1]:
                    str += '  V  '
            str += '\n'
    return str


class Ui_FirstWindow(object):

    def __init__(self, t, s, function):
        self.t = t
        self.s = s
        self.function = function

    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.setFixedSize(600, 680)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setEnabled(True)
        self.table.setGeometry(QtCore.QRect(46, 110, 507, 328))
        self.table.setStyleSheet("")
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(8)

        for i in range(8):
            item = QtWidgets.QTableWidgetItem()
            self.table.setVerticalHeaderItem(i, item)

        for i in range(4):
            item = QtWidgets.QTableWidgetItem()
            self.table.setHorizontalHeaderItem(i, item)

        for i in range(8):
            for j in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                self.table.setItem(i, j, item)

        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(55, 23, 490, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_1.setFont(font)
        self.text_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_1.setStyleSheet("")
        self.text_1.setScaledContents(False)
        self.text_1.setAlignment(QtCore.Qt.AlignCenter)
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(19, 460, 562, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_2.setFont(font)
        self.text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.text_2.setObjectName("text_2")
        self.radio_button_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_1.setGeometry(QtCore.QRect(180, 570, 20, 20))
        self.radio_button_1.setText("")
        self.radio_button_1.setObjectName("radio_button_1")
        self.radio_button_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_2.setGeometry(QtCore.QRect(420, 570, 20, 20))
        self.radio_button_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radio_button_2.setText("")
        self.radio_button_2.setObjectName("radio_button_2")
        self.push_button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_ok.setGeometry(QtCore.QRect(232, 610, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_ok.setFont(font)
        self.push_button_ok.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"border-radius: 25px;\n"
"")
        self.push_button_ok.setObjectName("push_button_ok")
        self.text_radio_button_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_radio_button_1.setGeometry(QtCore.QRect(178, 550, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_radio_button_1.setFont(font)
        self.text_radio_button_1.setAlignment(QtCore.Qt.AlignCenter)
        self.text_radio_button_1.setObjectName("text_radio_button_1")
        self.text_radio_button_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_radio_button_2.setGeometry(QtCore.QRect(418, 550, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_radio_button_2.setFont(font)
        self.text_radio_button_2.setAlignment(QtCore.Qt.AlignCenter)
        self.text_radio_button_2.setObjectName("text_radio_button_2")
        self.label_text_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_text_1.setGeometry(QtCore.QRect(51, 10, 502, 131))
        self.label_text_1.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.label_text_1.setText("")
        self.label_text_1.setObjectName("label_text_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(46, 110, 5, 328))
        self.label_2.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 110, 101, 328))
        self.label_3.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"border-radius: 30px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(19, 110, 101, 328))
        self.label_1.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"border-radius: 30px;")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_text_2.setGeometry(QtCore.QRect(10, 445, 580, 70))
        self.label_text_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;\n"
"")
        self.label_text_2.setText("")
        self.label_text_2.setObjectName("label_text_2")
        self.label_radio_button_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_radio_button_1.setGeometry(QtCore.QRect(160, 540, 55, 61))
        self.label_radio_button_1.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius: 20px;")
        self.label_radio_button_1.setText("")
        self.label_radio_button_1.setObjectName("label_radio_button_1")
        self.label_radio_button_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_radio_button_2.setGeometry(QtCore.QRect(400, 540, 55, 61))
        self.label_radio_button_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius: 20px;")
        self.label_radio_button_2.setText("")
        self.label_radio_button_2.setObjectName("label_radio_button_2")
        self.label_radio_button_2.raise_()
        self.label_radio_button_1.raise_()
        self.label_text_2.raise_()
        self.label_1.raise_()
        self.label_3.raise_()
        self.label_text_1.raise_()
        self.table.raise_()
        self.text_1.raise_()
        self.text_2.raise_()
        self.radio_button_1.raise_()
        self.radio_button_2.raise_()
        self.push_button_ok.raise_()
        self.text_radio_button_1.raise_()
        self.text_radio_button_2.raise_()
        self.label_2.raise_()
        FirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "Minimal DNF"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("FirstWindow", "X"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("FirstWindow", "Y"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("FirstWindow", "Z"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("FirstWindow", "A"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)

        num = 7
        for i in range(8):
            bin_num = bin(num)[2:]
            bin_num = '0' * (3 - len(bin_num)) + bin_num
            for j in range(3):
                item = self.table.item(i, j)
                item.setText(_translate("FirstWindow", bin_num[j]))
            item = self.table.item(i, 3)
            item.setText(_translate("FirstWindow", "1"))
            num -= 1

        self.table.setSortingEnabled(__sortingEnabled)
        self.text_1.setText(_translate("FirstWindow", "Найдите минимальную ДНФ для функции,\n"
" заданной таблицей:"))
        self.text_2.setText(_translate("FirstWindow", "Сколько минимальных ДНФ имеет эта функция?"))
        self.push_button_ok.setText(_translate("FirstWindow", "Ок"))
        self.text_radio_button_1.setText(_translate("FirstWindow", "1"))
        self.text_radio_button_2.setText(_translate("FirstWindow", "2"))

        # Filling table
        for i in range(2 ** self.t.arg_cnt):
            item = self.table.item(i, 3)
            item.setText(_translate("MainWindow", str(self.t.table[i][1])))

        self.add_functionality()

    def add_functionality(self):
        self.push_button_ok.clicked.connect(lambda: self.check_mdnf_count(self.function))

    def check_mdnf_count(self, function):
        if self.radio_button_1.isChecked():
            if len(self.s.minimal_dnf) == 1:
                function()
            else:
                self.wrong_mdnf_count()

        if self.radio_button_2.isChecked():
            if len(self.s.minimal_dnf) == 2:
                function()
            else:
                self.wrong_mdnf_count()

    def wrong_mdnf_count(self):
        error = QMessageBox()
        error.setWindowTitle('Неверный ответ')
        error.setText('Вы выбрали неверное количество минимальных ДНФ функции')
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        error.setDefaultButton(QMessageBox.Close)

        if len(self.s.minimal_dnf) == 1:
            error.setInformativeText(f'Функция, заданная этой таблицей, имеет 1 минимальную ДНФ')
            error.setDetailedText(f'Минимальная ДНФ: {tuple_to_string(self.s.minimal_dnf)}')
        else:
            error.setInformativeText(f'Функция, заданная этой таблицей, имеет 2 минимальных ДНФ')
            error.setDetailedText(f'Минимальные ДНФ: {tuple_to_string(self.s.minimal_dnf)}')

        error.buttonClicked.connect(self.close_button_pressed)

        error.exec_()

        # Если человек получил доступ к ответу, обновляем таблицу
        self.t = Table()
        self.s = Solution(self.t)

        # Refilling table
        for i in range(2 ** self.t.arg_cnt):
            item = self.table.item(i, 3)
            item.setData(QtCore.Qt.EditRole, QtCore.QVariant(str(self.t.table[i][1])))

    def close_button_pressed(self, button):
        if button.text() == 'Close':
            QApplication.quit()
