# Form implementation generated from reading ui file 'mentor_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 550)
        Form.setMinimumSize(QtCore.QSize(860, 550))
        Form.setMaximumSize(QtCore.QSize(860, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/wehere_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.499773, y1:1, x2:0.5, y2:0.00568182, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 141))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pictures/mentor_menu.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(240, 12, 261, 101))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pictures/wehere_logo.ico"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(500, 40, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(71, 84, 88);")
        self.label_3.setObjectName("label_3")
        self.pushButton_mentor_all_app = QtWidgets.QPushButton(parent=Form)
        self.pushButton_mentor_all_app.setGeometry(QtCore.QRect(30, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_mentor_all_app.setFont(font)
        self.pushButton_mentor_all_app.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_mentor_all_app.setObjectName("pushButton_mentor_all_app")
        self.pushButton_mentor_exit = QtWidgets.QPushButton(parent=Form)
        self.pushButton_mentor_exit.setGeometry(QtCore.QRect(30, 480, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_mentor_exit.setFont(font)
        self.pushButton_mentor_exit.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_mentor_exit.setObjectName("pushButton_mentor_exit")
        self.lineEdit_mentor_username = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_mentor_username.setEnabled(True)
        self.lineEdit_mentor_username.setGeometry(QtCore.QRect(30, 170, 171, 31))
        self.lineEdit_mentor_username.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEdit_mentor_username.setStyleSheet("QLineEdit {\n"
"  border: 2px solid rgb(38, 38, 48);\n"
"  border-radius: 15px;\n"
"  color: #FFF;\n"
"  padding-left: 15px;\n"
"  background-color: rgb(36, 36, 36);\n"
" \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"\n"
" QLineEdit:focus  {\n"
"  border: 2px solid rgb(35, 218, 233);\n"
"  background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"   \n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_mentor_username.setText("")
        self.lineEdit_mentor_username.setObjectName("lineEdit_mentor_username")
        self.pushButton_mentor_preferences = QtWidgets.QPushButton(parent=Form)
        self.pushButton_mentor_preferences.setGeometry(QtCore.QRect(30, 390, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_mentor_preferences.setFont(font)
        self.pushButton_mentor_preferences.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_mentor_preferences.setObjectName("pushButton_mentor_preferences")
        self.pushButton_mentor_search = QtWidgets.QPushButton(parent=Form)
        self.pushButton_mentor_search.setGeometry(QtCore.QRect(30, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_mentor_search.setFont(font)
        self.pushButton_mentor_search.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_mentor_search.setObjectName("pushButton_mentor_search")
        self.tableWidget_mentor = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget_mentor.setGeometry(QtCore.QRect(230, 170, 601, 341))
        self.tableWidget_mentor.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.tableWidget_mentor.setObjectName("tableWidget_mentor")
        self.tableWidget_mentor.setColumnCount(6)
        self.tableWidget_mentor.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mentor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mentor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mentor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mentor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mentor.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mentor.setHorizontalHeaderItem(5, item)
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(470, 110, 361, 31))
        self.comboBox.setStyleSheet("border-radius : 15px;\n"
"border: 3px solid rgb(85, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MENTOR MENU"))
        self.label_3.setText(_translate("Form", "MENTOR MENU"))
        self.pushButton_mentor_all_app.setText(_translate("Form", "All Applications"))
        self.pushButton_mentor_exit.setText(_translate("Form", "Exit"))
        self.lineEdit_mentor_username.setPlaceholderText(_translate("Form", "      Name or Surname"))
        self.pushButton_mentor_preferences.setText(_translate("Form", "Preferences"))
        self.pushButton_mentor_search.setText(_translate("Form", "Search"))
        item = self.tableWidget_mentor.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Interview Date"))
        item = self.tableWidget_mentor.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name Surname"))
        item = self.tableWidget_mentor.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mentor"))
        item = self.tableWidget_mentor.horizontalHeaderItem(3)
        item.setText(_translate("Form", "IT Knowledge"))
        item = self.tableWidget_mentor.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Nieuwe kolom"))
        item = self.tableWidget_mentor.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Comments"))
        self.comboBox.setItemText(0, _translate("Form", "    VIT Projesini Tamamina Katilmasi Uygundur."))
        self.comboBox.setItemText(1, _translate("Form", "    VIT Projesinin Ilk IT Egitimi Al... a Yonlendirimesi Uygundur."))
        self.comboBox.setItemText(2, _translate("Form", "    VIT Projesinin Ingilizce Egitim Al... a Yonlendirimesi Uygundur."))
        self.comboBox.setItemText(3, _translate("Form", "    VIT Projesi Kapsaminda Dir... Yonlendirilmesi Uygundur."))
        self.comboBox.setItemText(4, _translate("Form", "    Direk Bireysel Kocluk Ile Ise yonlendirilmesi Uygundur."))
        self.comboBox.setItemText(5, _translate("Form", "    Bir Sonra Vit Projesine Katilmasi Uygun Olur."))
        self.comboBox.setItemText(6, _translate("Form", "    Baska Bir Soktere Yonlendirmesi Uygun Olur."))
        self.comboBox.setItemText(7, _translate("Form", "    Diger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())