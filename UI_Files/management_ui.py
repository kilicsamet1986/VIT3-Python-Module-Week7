# Form implementation generated from reading ui file 'UI_Files/management_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormManagement(object):
    def setupUi(self, FormManagement):
        FormManagement.setObjectName("FormManagement")
        FormManagement.resize(750, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormManagement.sizePolicy().hasHeightForWidth())
        FormManagement.setSizePolicy(sizePolicy)
        FormManagement.setMinimumSize(QtCore.QSize(750, 500))
        FormManagement.setMaximumSize(QtCore.QSize(750, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_Files\\pictures/werhere_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FormManagement.setWindowIcon(icon)
        FormManagement.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.494, y2:0, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButtonExit = QtWidgets.QPushButton(parent=FormManagement)
        self.pushButtonExit.setGeometry(QtCore.QRect(10, 430, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.labelLogo = QtWidgets.QLabel(parent=FormManagement)
        self.labelLogo.setGeometry(QtCore.QRect(190, 32, 261, 101))
        self.labelLogo.setStyleSheet("\n"
"background-color: rgba(0, 0, 0,0%);")
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("UI_Files\\pictures/werhere_logo.ico"))
        self.labelLogo.setObjectName("labelLogo")
        self.pushButtonSendEmail = QtWidgets.QPushButton(parent=FormManagement)
        self.pushButtonSendEmail.setGeometry(QtCore.QRect(10, 270, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButtonSendEmail.setFont(font)
        self.pushButtonSendEmail.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButtonSendEmail.setObjectName("pushButtonSendEmail")
        self.labelPicture = QtWidgets.QLabel(parent=FormManagement)
        self.labelPicture.setGeometry(QtCore.QRect(10, 10, 191, 171))
        self.labelPicture.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.labelPicture.setText("")
        self.labelPicture.setPixmap(QtGui.QPixmap("UI_Files\\pictures/main_admin.png"))
        self.labelPicture.setScaledContents(True)
        self.labelPicture.setObjectName("labelPicture")
        self.labelManagement = QtWidgets.QLabel(parent=FormManagement)
        self.labelManagement.setGeometry(QtCore.QRect(450, 60, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.labelManagement.setFont(font)
        self.labelManagement.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(71, 84, 88);")
        self.labelManagement.setObjectName("labelManagement")
        self.tableWidget = QtWidgets.QTableWidget(parent=FormManagement)
        self.tableWidget.setGeometry(QtCore.QRect(200, 190, 521, 271))
        self.tableWidget.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.pushButtonBackMenu = QtWidgets.QPushButton(parent=FormManagement)
        self.pushButtonBackMenu.setGeometry(QtCore.QRect(10, 350, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButtonBackMenu.setFont(font)
        self.pushButtonBackMenu.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButtonBackMenu.setObjectName("pushButtonBackMenu")
        self.labelPage = QtWidgets.QLabel(parent=FormManagement)
        self.labelPage.setGeometry(QtCore.QRect(410, 110, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.labelPage.setFont(font)
        self.labelPage.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(71, 84, 88);")
        self.labelPage.setObjectName("labelPage")
        self.pushButtonGetAllEvents = QtWidgets.QPushButton(parent=FormManagement)
        self.pushButtonGetAllEvents.setGeometry(QtCore.QRect(10, 190, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButtonGetAllEvents.setFont(font)
        self.pushButtonGetAllEvents.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButtonGetAllEvents.setObjectName("pushButtonGetAllEvents")

        self.retranslateUi(FormManagement)
        QtCore.QMetaObject.connectSlotsByName(FormManagement)
        FormManagement.setTabOrder(self.pushButtonGetAllEvents, self.pushButtonSendEmail)
        FormManagement.setTabOrder(self.pushButtonSendEmail, self.pushButtonBackMenu)
        FormManagement.setTabOrder(self.pushButtonBackMenu, self.tableWidget)
        FormManagement.setTabOrder(self.tableWidget, self.pushButtonExit)

    def retranslateUi(self, FormManagement):
        _translate = QtCore.QCoreApplication.translate
        FormManagement.setWindowTitle(_translate("FormManagement", "MANAGEMENT PAGE"))
        self.pushButtonExit.setText(_translate("FormManagement", "Exit"))
        self.pushButtonSendEmail.setText(_translate("FormManagement", "Send Mail"))
        self.labelManagement.setText(_translate("FormManagement", "MANAGEMENT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FormManagement", "Event Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FormManagement", "Start Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FormManagement", "Participant Mail"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FormManagement", "Organizer Mail"))
        self.pushButtonBackMenu.setText(_translate("FormManagement", "Back Menu"))
        self.labelPage.setText(_translate("FormManagement", "PAGE"))
        self.pushButtonGetAllEvents.setText(_translate("FormManagement", "Get All Events"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormManagement = QtWidgets.QWidget()
    ui = Ui_FormManagement()
    ui.setupUi(FormManagement)
    FormManagement.show()
    sys.exit(app.exec())
