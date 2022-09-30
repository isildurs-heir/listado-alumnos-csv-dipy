from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import csv
import sys
from tempfile import NamedTemporaryFile
import shutil

#Hacer dos csv el principal con los datos de la cursada
# y otro con los datos del alumno
class clsMainWIn(QtWidgets.QMainWindow):
    def __init__(self,filename, parent=None): #FILENAME
        super(clsMainWIn, self).__init__(parent)
        uic.loadUi('tp3/alumnos-dipy/main-table.ui',self)
        self.fileName = filename
        self.auxFIle = 'temporary.csv' #=???
        self.setupUiComponents()
        

    def setupUiComponents(self):
        self.datos.resizeColumnsToContents()
        self.datos.resizeRowsToContents()
        
        self.loadTable()
        self.datos.doubleClicked.connect(self.doSome)
        self.btnCerrar.clicked.connect(self.closeMainWindow)
        
    def doSome(self):
        print('xd')
    
    
    def closeMainWindow(self):
        self.close()
    
    def loadTable(self):
        myFile = open(self.fileName,'r')
        try:
            reader = csv.reader(myFile,delimiter = ',')
            rowI = 0
            for row in reader:
                self.datos.setRowCount(rowI+1)
                
                if rowI == 0:
                    columns = len(row)
                    self.datos.setColumnCount(columns)
                    
                columns = len(row)
                for columnJ in range(columns):
                    myValue = row[columnJ]
                    cell = QTableWidgetItem(str(myValue))
                    
                    self.datos.setItem(rowI,columnJ,cell)
                rowI = rowI + 1
        finally:
            myFile.close()
            
        
def main():
    app = QApplication(sys.argv)
    
    filename = 'tp3/alumnos-dipy/listado.csv'
    
    objeto = clsMainWIn(filename)
    objeto.show()
    app.exec_()
    
if __name__ == '__main__':
    main()