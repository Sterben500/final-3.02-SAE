# coding=utf-8
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QSize
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
import pandas as pd
import threading,time
from PyQt5.Qt import Qt 
import json
from functions import *


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 715)
        MainWindow.setStyleSheet("background-color: rgb(178, 219, 213);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(500, 55, 30, 30))
        self.icon.setObjectName("icon")
        self.state = QtWidgets.QLabel(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(380, 40, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.state.setFont(font)
        self.state.setObjectName("state")
        self.import_2 = QtWidgets.QPushButton(self.centralwidget)
        self.import_2.setGeometry(QtCore.QRect(140, 120, 131, 41))
        self.import_2.setStyleSheet("background-color: rgb(43, 97,109);\n"
                        "color: rgb(255, 255, 255);\n"
                        "border-radius: 1em ;\n"
                        "border: 0px ;")
        self.import_2.setObjectName("import_2")
        self.clients = QtWidgets.QComboBox(self.centralwidget)
        self.clients.setGeometry(QtCore.QRect(250, 190, 301, 41))
        self.clients.setStyleSheet("QComboBox{\n"
                                        "font: 12pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border: 1px solid #2ECC71;\n"
                                        "border-radius: 0.5em;\n"
                                        "padding-left: 7px;}\n"
                                        "QComboBox::drop-down {\n"
                                        "    width:30px;\n"
                                        "    border:0px;\n"
                                        "    margin:0px;\n"
                                        "\n"
                                        "}\n"
                                        "QComboBox::down-arrow {\n"
                                        "    \n"
                                        "    image: url(\"down.png\");\n"
                                        "}\n"
                                        "QComboBox QAbstractItemView\n"
                                        "{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border: 0px solid #2ECC71;\n"
                                        "border-radius: 0.0em;\n"
                                        "padding-left: 7px;\n"
                                        "}")
        self.clients.setObjectName("clients")
        self.clients.addItem("")
        self.clients.setItemText(0, "")
        self.connect = QtWidgets.QPushButton(self.centralwidget)
        self.connect.setGeometry(QtCore.QRect(350, 120, 131, 41))
        self.connect.setStyleSheet("background-color: rgb(43, 97,109);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1em ;\n"
"border: 0px ;")
        self.connect.setObjectName("connect")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 250, 541, 321))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border: 1px solid #2ECC71;\n"
"border-radius: 0.5em ;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-top: 4px;\n"
"padding-left: 3px;")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 610, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 1px solid #2ECC71;\n"
"border-radius: 0.5em ;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-top: 4px;\n"
"padding-left: 3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(550, 610, 131, 41))
        self.send.setStyleSheet("background-color: rgb(43, 97,109);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1em ;\n"
"border: 0px ;")
        self.send.setObjectName("send")
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(550, 120, 131, 41))
        self.delete_2.setStyleSheet("background-color: rgb(43, 97,109);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1em ;\n"
"border: 0px ;")
        self.delete_2.setObjectName("delete_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.setWindowTitle('service client controller')
        self.setWindowIcon(QIcon('client.png'))

        self.connect.clicked.connect(lambda: self.func1())
        self.send.clicked.connect(lambda:send_msg())
        self.import_2.clicked.connect(lambda:self.open_file_dialog())
        self.clients.activated.connect(lambda: self.select_client())
        self.delete_2.clicked.connect(lambda: remove())

        self.pixmap = QPixmap('circle.png')
        self.pixmap=self.pixmap.scaled(QSize(25,25))
        self.icon.setPixmap(self.pixmap)
        
        self.text_labels=[self.textEdit]
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "STATUS : "))
        self.icon.setText(_translate("MainWindow", "     .  "))
        self.state.setText(_translate("MainWindow", "Disconnect"))
        self.import_2.setText(_translate("MainWindow", "IMPORT"))
        self.connect.setText(_translate("MainWindow", "CONNECT"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "TYPE HERE"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "TYPE HERE"))
        self.send.setText(_translate("MainWindow", "SEND"))
        self.delete_2.setText(_translate("MainWindow", "delete"))

    def select_client(self):
        for i in self.text_labels:
            i.hide()
        self.text_labels[self.clients.currentIndex()].show()
    def func1(self):
        threading.Thread(target=main,args=('localhost',5050,[self.textEdit,self.icon,self.clients,self.lineEdit])).start()
    def open_file_dialog(self):
      try:
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","json File (*.json)")
        if fileName:
            
                with open(fileName,'r') as f:
                    data=json.load(f)
                    name=data['name']
         
                add_client_to_combobox(str(connections[connections_names.index(name)]))
                self.text_labels.append(self.new_chat_box())
                update_text_labels(self.text_labels)
                names_validation[name]=True
      
      except:pass
    def new_chat_box(self):
        textEdit = QtWidgets.QTextEdit(self.centralwidget)
        textEdit.setGeometry(QtCore.QRect(140, 250, 541, 321))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        textEdit.setFont(font)
        textEdit.setStyleSheet("border: 1px solid #2ECC71;\n"
                                    "border-radius: 0.5em ;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "padding-top: 4px;\n"
                                    "padding-left: 3px;")
        _translate = QtCore.QCoreApplication.translate
        textEdit.setPlaceholderText(_translate("MainWindow", "TYPE HERE"))
        textEdit.hide()
        
        return textEdit
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
