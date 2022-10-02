from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import csv
import shutil
import sys
from tempfile import NamedTemporaryFile


class clsEstadoForm(QtWidgets.QMainWindow):
    def __init__(self, csvEstadoPath,  row,parent=None):  # aqui
        super(clsEstadoForm, self).__init__()
        uic.loadUi('ui-files/estado-form.ui', self)
        self.csvEstadoPath = csvEstadoPath
        self.auxFIle = 'temporary-estado.csv'
        self.row = row
        
        
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.btnCerrar.clicked.connect(self.close)

        self.loadTable()
        


    def loadTable(self):
        myFile = open(self.csvEstadoPath, 'r')
        try:
            reader = csv.reader(myFile, delimiter=",")
            self.datos.setRowCount(1)
            rowI = 0
            for row in reader:
                if  rowI == self.row:
                    columns = len(row)
                    self.datos.setColumnCount(columns)
                    for columnJ in range(columns):
                        myValue = row[columnJ]
                        cell = QTableWidgetItem(str(myValue))
                        self.datos.setItem(0,columnJ,cell)
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
