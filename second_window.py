from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def string_to_set(s):
    """Converting a string to a set of sets
    At the first level of nesting MDNF, at the
    second - the conjunctors of each of the MDNF,
    at the last - variables
    """
    s = s.replace('X̅', '!X')
    s = s.replace('Y̅', '!Y')
    s = s.replace('Z̅', '!Z')
    s = s.replace('  V  ', ' ')
    s = s.split('\n')

    set_of_mdnfs = set()
    for mdnf in s:
        set_of_conjunctors = set()
        for conjuctor in mdnf.split():
            conj = set()
            i = 0
            while i < len(conjuctor):
                if conjuctor[i] == '!':
                    conj.add(conjuctor[i] + conjuctor[i + 1])
                    i += 2
                else:
                    conj.add(conjuctor[i])
                    i += 1
            set_of_conjunctors.add(frozenset(conj))
        set_of_mdnfs.add(frozenset(set_of_conjunctors))
    return set_of_mdnfs


def tuple_to_set(tup):
    """Converting a tuple to a set of sets
    At the first level of nesting MDNF, at the
    second - the conjunctors of each of the MDNF,
    at the last - variables
    """
    set_of_mdnfs = set()
    for mdnf in tup:
        set_of_conjunctors = set()
        for conjuctor in mdnf:
            conj = set()
            for var in conjuctor:
                conj.add(var)
            set_of_conjunctors.add(frozenset(conj))
        set_of_mdnfs.add(frozenset(set_of_conjunctors))
    return set_of_mdnfs


class Ui_SecondWindow(object):

    def __init__(self, t, s):
        self.t = t
        self.s = s

    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.setFixedSize(580, 660)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_button_back = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_back.setGeometry(QtCore.QRect(44, 560, 260, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_back.setFont(font)
        self.push_button_back.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                            "border-color: rgb(0, 0, 0);\n"
                                            "border-radius: 30px;")
        self.push_button_back.setObjectName("push_button_back")
        self.push_button_x = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_x.setGeometry(QtCore.QRect(44, 220, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_x.setFont(font)
        self.push_button_x.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                         "border-radius: 30px;")
        self.push_button_x.setObjectName("push_button_x")
        self.push_button_z = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_z.setGeometry(QtCore.QRect(312, 220, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_z.setFont(font)
        self.push_button_z.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                         "border-radius: 30px;")
        self.push_button_z.setObjectName("push_button_z")
        self.push_button_or = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_or.setGeometry(QtCore.QRect(446, 220, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_or.setFont(font)
        self.push_button_or.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                          "border-radius: 30px;")
        self.push_button_or.setObjectName("push_button_or")
        self.push_button_y = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_y.setGeometry(QtCore.QRect(178, 220, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_y.setFont(font)
        self.push_button_y.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                         "border-radius: 30px;")
        self.push_button_y.setObjectName("push_button_y")
        self.push_button_not_x = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_not_x.setGeometry(QtCore.QRect(44, 330, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_not_x.setFont(font)
        self.push_button_not_x.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                             "border-radius: 30px;")
        self.push_button_not_x.setObjectName("push_button_not_x")
        self.push_button_not_y = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_not_y.setGeometry(QtCore.QRect(178, 330, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_not_y.setFont(font)
        self.push_button_not_y.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                             "border-radius: 30px;")
        self.push_button_not_y.setObjectName("push_button_not_y")
        self.push_button_not_z = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_not_z.setGeometry(QtCore.QRect(312, 330, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_not_z.setFont(font)
        self.push_button_not_z.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                             "border-radius: 30px;")
        self.push_button_not_z.setObjectName("push_button_not_z")
        self.push_button_slash = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_slash.setGeometry(QtCore.QRect(446, 330, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_slash.setFont(font)
        self.push_button_slash.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                             "border-radius: 30px;")
        self.push_button_slash.setObjectName("push_button_slash")
        self.push_button_del = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_del.setGeometry(QtCore.QRect(446, 440, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_del.setFont(font)
        self.push_button_del.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                           "border-radius: 30px;")
        self.push_button_del.setObjectName("push_button_del")
        self.push_button_check_answer = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_check_answer.setGeometry(QtCore.QRect(44, 440, 358, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_check_answer.setFont(font)
        self.push_button_check_answer.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                                    "border-radius: 30px;")
        self.push_button_check_answer.setObjectName("push_button_check_answer")
        self.label_text_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_text_1.setGeometry(QtCore.QRect(35, 30, 510, 110))
        self.label_text_1.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                        "border-radius: 30px;")
        self.label_text_1.setText("")
        self.label_text_1.setObjectName("label_text_1")
        self.answer_line = QtWidgets.QLabel(self.centralwidget)
        self.answer_line.setGeometry(QtCore.QRect(35, 90, 510, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.answer_line.setFont(font)
        self.answer_line.setStyleSheet("background-color: rgb(193, 193, 193);\n"
                                       "border-radius: 30px;")
        self.answer_line.setText("")
        self.answer_line.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_line.setObjectName("answer_line")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(35, 30, 510, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("")
        self.text_1.setAlignment(QtCore.Qt.AlignCenter)
        self.text_1.setObjectName("text_1")
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.push_button_back.setText(_translate("SecondWindow", "Вернуться к таблице"))
        self.push_button_x.setText(_translate("SecondWindow", "X"))
        self.push_button_z.setText(_translate("SecondWindow", "Z"))
        self.push_button_or.setText(_translate("SecondWindow", "V"))
        self.push_button_y.setText(_translate("SecondWindow", "Y"))
        self.push_button_not_x.setText(_translate("SecondWindow", "X̅"))
        self.push_button_not_y.setText(_translate("SecondWindow", "Y̅"))
        self.push_button_not_z.setText(_translate("SecondWindow", "Z̅"))
        self.push_button_slash.setText(_translate("SecondWindow", "/"))
        self.push_button_del.setText(_translate("SecondWindow", "Del"))
        self.push_button_check_answer.setText(_translate("SecondWindow", "Проверить ответ"))
        self.text_1.setText(_translate("SecondWindow", "Введите минимальную ДНФ\n"
                                                       "Если их 2, введите вторую через знак \" / \""))

        self.add_functionality()

    def add_functionality(self):
        self.push_button_x.clicked.connect(lambda: self.write(self.push_button_x.text()))
        self.push_button_y.clicked.connect(lambda: self.write(self.push_button_y.text()))
        self.push_button_z.clicked.connect(lambda: self.write(self.push_button_z.text()))
        self.push_button_not_x.clicked.connect(lambda: self.write(self.push_button_not_x.text()))
        self.push_button_not_y.clicked.connect(lambda: self.write(self.push_button_not_y.text()))
        self.push_button_not_z.clicked.connect(lambda: self.write(self.push_button_not_z.text()))
        self.push_button_or.clicked.connect(lambda: self.write('  ' + self.push_button_or.text() + '  '))
        self.push_button_slash.clicked.connect(lambda: self.write('\n'))
        self.push_button_del.clicked.connect(lambda: self.delete_text())
        self.push_button_check_answer.clicked.connect(lambda: self.check_answer(self.answer_line.text()))

    def write(self, text):
        self.answer_line.setText(self.answer_line.text() + text)

    def delete_text(self):
        string = self.answer_line.text()
        if string == '':
            return
        if string.endswith('  V  '):
            string = string[:-5]
        elif string.endswith('X̅') or string.endswith('Y̅') or string.endswith('Z̅'):
            string = string[:-2]
        else:
            string = string[:-1]
        self.answer_line.setText(string)

    def check_answer(self, mdnf):
        answer_line_mdnf = string_to_set(mdnf)
        correct_mdnf = tuple_to_set(self.s.minimal_dnf)

        if answer_line_mdnf == correct_mdnf:
            self.correct_answer()
        else:
            self.wrong_answer()

    def correct_answer(self):
        msg = QMessageBox()
        msg.setWindowTitle('Верный ответ')
        msg.setText('Вы ввели все верные минимальные ДНФ.\n                  Экзамен сдан!')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        msg.buttonClicked.connect(self.close_program)
        msg.exec_()

    def wrong_answer(self):
        msg = QMessageBox()
        msg.setWindowTitle('Неверный ответ')
        msg.setText('Вы ошиблись в нахождении минимальных ДНФ.\nПопробуйте еще раз или завершите экзамен.')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        msg.buttonClicked.connect(self.close_program)
        msg.exec_()

    @staticmethod
    def close_program(button):
        if button.text() == 'Close':
            QApplication.quit()
