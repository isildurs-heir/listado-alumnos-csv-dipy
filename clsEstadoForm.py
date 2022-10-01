from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import csv
import shutil
import sys
from tempfile import NamedTemporaryFile


class clsEstadoForm(QtWidgets.QMainWindow):
    def __init__(self, row, parent=None):  # aqui
        super(clsEstadoForm, self).__init__()
        uic.loadUi('tp3/alumnos-dipy/ui-files/estado-form.ui', self)
        self.fileName = 'tp3/alumnos-dipy/csv-files/estado.csv'
        self.auxFIle = 'temporary-estado.csv'
        self.row = row
        
        
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.datos.resizeColumnsToContents()
        self.datos.resizeRowsToContents()
        self.btnCerrar.clicked.connect(self.close)

        self.loadTable()
        


    def loadTable(self):
        myFile = open(self.fileName, 'r')
        try:
            reader = csv.reader(myFile, delimiter=",")
            self.datos.setRowCount(2)
            p = 0
            rowI = 0
            for row in reader:
                if rowI == 0 or rowI == self.row:
                    columns = len(row)
                    self.datos.setColumnCount(columns)
                    for columnJ in range(columns):
                        myValue = row[columnJ]
                        cell = QTableWidgetItem(str(myValue))
                        self.datos.setItem(p,columnJ,cell)
                    p +=1
                rowI +=1
        finally:
            myFile.close()


def main():
    app = QtWidgets.QApplication(sys.argv)

    form = clsEstadoForm()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
