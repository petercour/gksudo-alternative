#!/usr/bin/python3
# gksudo alternative
# https://pythonbasics.org/pyqt/
#
# example: ./qtsudo.py ls -al

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
 
class Example(QtWidgets.QDialog):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonBox.accepted.connect(self.onClick)

    def onClick(self):
        password = self.lineEditPassword.text()
        password = password.replace("\n","")
        cmd = str(' '.join(sys.argv[1:]))
        # now run sudo cmd with password
        os.system("echo " + password + " | sudo -S " + cmd)

app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
