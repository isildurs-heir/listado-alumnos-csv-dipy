from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import csv
import shutil
import sys
from tempfile import NamedTemporaryFile


class clsEstadoForm(QtWidgets.QMainWindow):
    updateCsv = QtCore.pyqtSignal()
    def __init__(self, csvEstado,  row, parent=None):  # aqui
        super(clsEstadoForm, self).__init__()
        uic.loadUi('ui-files/estado-form.ui', self)
        self.csvEstado = csvEstado
        self.auxFile = 'temporary-estado.csv'
        self.row = row

        self.setupUiComponents()

    def setupUiComponents(self):
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnCerrar.clicked.connect(self.close)
        self.loadTable()

    def guardar(self):
        self.updateCsv.emit()
        self.close()
    
    def loadTable(self):
        with open(self.csvEstado) as f:
            i = [*csv.DictReader(f)]
            self.datos.setRowCount(1)
            self.datos.setColumnCount(len(i[0]))
            self.datos.setItem(0, 0, QTableWidgetItem(str(i[self.row]['1p'])))
            self.datos.setItem(0, 1, QTableWidgetItem(str(i[self.row]['1r'])))
            self.datos.setItem(0, 2, QTableWidgetItem(str(i[self.row]['2p'])))
            self.datos.setItem(0, 3, QTableWidgetItem(str(i[self.row]['2r'])))


def main():
    app = QtWidgets.QApplication(sys.argv)

    form = clsEstadoForm()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
