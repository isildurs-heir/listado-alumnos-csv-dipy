from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import os 
import pathlib

class clsEditForm(QtWidgets.QMainWindow):
    dataToCsv = QtCore.pyqtSignal(dict)
    updateCsv = QtCore.pyqtSignal()
    def __init__(self):
        super(clsEditForm,self).__init__()
        dirpath = pathlib.Path(__file__).parent.resolve()
        uiPath = os.path.join(dirpath,'resources/ui-files/edit-form.ui')
        uic.loadUi(uiPath,self)
        self.dicc = {}

        self.setupUiComponents()

    def setupUiComponents(self):
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnCerrar.clicked.connect(self.close)
    
    def guardar(self):
        alumno = self.alumno_edit.toPlainText()
        lu = self.lu_edit.toPlainText()
        if alumno != "" and lu != "":
            self.dicc['alumno'] = alumno
            self.dicc['lu'] = lu
            self.dataToCsv.emit(self.dicc)
            self.updateCsv.emit()
            self.close()

        else:
            self.alumno_edit.setPlainText("vacio!")
            self.lu_edit.setPlainText("vacio!")