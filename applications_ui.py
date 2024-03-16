# Form implementation generated from reading ui file 'applications_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 680)
        Form.setMinimumSize(QtCore.QSize(1080, 680))
        Form.setMaximumSize(QtCore.QSize(1080, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/wehere_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.499773, y1:1, x2:0.5, y2:0.00568182, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_app_all_app = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_all_app.setGeometry(QtCore.QRect(40, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_all_app.setFont(font)
        self.pushButton_app_all_app.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_all_app.setObjectName("pushButton_app_all_app")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(270, 22, 261, 101))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pictures/wehere_logo.ico"))
        self.label.setObjectName("label")
        self.pushButton_app_planned_mentor = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_planned_mentor.setGeometry(QtCore.QRect(40, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_planned_mentor.setFont(font)
        self.pushButton_app_planned_mentor.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_planned_mentor.setObjectName("pushButton_app_planned_mentor")
        self.pushButton_app_unscheduled_meeting = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_unscheduled_meeting.setGeometry(QtCore.QRect(40, 310, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_unscheduled_meeting.setFont(font)
        self.pushButton_app_unscheduled_meeting.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_unscheduled_meeting.setObjectName("pushButton_app_unscheduled_meeting")
        self.pushButton_app_pre_vit_control = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_pre_vit_control.setGeometry(QtCore.QRect(40, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_pre_vit_control.setFont(font)
        self.pushButton_app_pre_vit_control.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_pre_vit_control.setObjectName("pushButton_app_pre_vit_control")
        self.pushButton_app_rep_registrations = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_rep_registrations.setGeometry(QtCore.QRect(40, 410, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_rep_registrations.setFont(font)
        self.pushButton_app_rep_registrations.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_rep_registrations.setObjectName("pushButton_app_rep_registrations")
        self.pushButton_diff_registration = QtWidgets.QPushButton(parent=Form)
        self.pushButton_diff_registration.setGeometry(QtCore.QRect(40, 460, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_diff_registration.setFont(font)
        self.pushButton_diff_registration.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_diff_registration.setObjectName("pushButton_diff_registration")
        self.pushButton_app_preferences = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_preferences.setGeometry(QtCore.QRect(40, 510, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_preferences.setFont(font)
        self.pushButton_app_preferences.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_preferences.setObjectName("pushButton_app_preferences")
        self.pushButton_app_filter_app = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_filter_app.setGeometry(QtCore.QRect(40, 560, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_filter_app.setFont(font)
        self.pushButton_app_filter_app.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_filter_app.setObjectName("pushButton_app_filter_app")
        self.pushButton_app_exit = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_exit.setGeometry(QtCore.QRect(40, 610, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_exit.setFont(font)
        self.pushButton_app_exit.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_exit.setObjectName("pushButton_app_exit")
        self.pushButton_app_search = QtWidgets.QPushButton(parent=Form)
        self.pushButton_app_search.setGeometry(QtCore.QRect(40, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_search.setFont(font)
        self.pushButton_app_search.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"}")
        self.pushButton_app_search.setObjectName("pushButton_app_search")
        self.tableWidget_app = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget_app.setGeometry(QtCore.QRect(250, 130, 801, 521))
        self.tableWidget_app.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.tableWidget_app.setObjectName("tableWidget_app")
        self.tableWidget_app.setColumnCount(8)
        self.tableWidget_app.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(7, item)
        self.lineEdit_app_username = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_app_username.setEnabled(True)
        self.lineEdit_app_username.setGeometry(QtCore.QRect(40, 130, 171, 31))
        self.lineEdit_app_username.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEdit_app_username.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_app_username.setText("")
        self.lineEdit_app_username.setObjectName("lineEdit_app_username")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(530, 50, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(71, 84, 88);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(8, 10, 231, 121))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pictures/project_app.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "APPLICATION"))
        self.pushButton_app_all_app.setText(_translate("Form", "All Applications"))
        self.pushButton_app_planned_mentor.setText(_translate("Form", "Planned Mentor Meetings"))
        self.pushButton_app_unscheduled_meeting.setText(_translate("Form", "Unscheduled M. Meetings"))
        self.pushButton_app_pre_vit_control.setText(_translate("Form", "Previous VIT Control"))
        self.pushButton_app_rep_registrations.setText(_translate("Form", "Repeated Registration"))
        self.pushButton_diff_registration.setText(_translate("Form", "Different Registration"))
        self.pushButton_app_preferences.setText(_translate("Form", "Preferences"))
        self.pushButton_app_filter_app.setText(_translate("Form", "Filter Application"))
        self.pushButton_app_exit.setText(_translate("Form", "Exit"))
        self.pushButton_app_search.setText(_translate("Form", "Search"))
        item = self.tableWidget_app.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget_app.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name Surname"))
        item = self.tableWidget_app.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mail"))
        item = self.tableWidget_app.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Telephone"))
        item = self.tableWidget_app.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Post Code"))
        item = self.tableWidget_app.horizontalHeaderItem(5)
        item.setText(_translate("Form", "State"))
        item = self.tableWidget_app.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Status"))
        item = self.tableWidget_app.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Economical \n"
"Situation"))
        self.lineEdit_app_username.setPlaceholderText(_translate("Form", "      Name or Surname"))
        self.label_2.setText(_translate("Form", "PROJECT APPLICATIONS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
