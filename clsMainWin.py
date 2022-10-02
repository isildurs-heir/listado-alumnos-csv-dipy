from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import csv
import sys
from tempfile import NamedTemporaryFile
import shutil
import clsEstadoForm as estadoForm

#Hacer dos csv el principal con los datos de la cursada
# y otro con los datos del alumno
class clsMainWIn(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(clsMainWIn, self).__init__(parent)
        uic.loadUi('ui-files/main-table.ui',self)        
        
        self.listPath = 'csv-files/listado.csv'
        self.csvEstadoPath = 'csv-files/estado.csv'
        self.auxFIle = 'temporary-listado.csv' #=???
        
        self.setupUiComponents()
        

    def setupUiComponents(self):
        self.loadTable()
        self.datos.doubleClicked.connect(self.moreData)
        self.btnCerrar.clicked.connect(self.closeMainWindow)
        
    def moreData(self,index):
        column = index.column()
        row = index.row()
        if column == 0:
            print("datos de alumno")
        elif column == 2:
            self.estadoForm = estadoForm.clsEstadoForm(self.csvEstadoPath,row)
            self.estadoForm.show()
            self.estadoForm.id.setText("Nombre: "+self.datos.item(row,0).text()+" \nLu: "+self.datos.item(row,1).text())
            
    def closeMainWindow(self):
        self.close()
    
    def loadTable(self):
        myFile = open(self.listPath,'r')
        try:
            reader = csv.reader(myFile,delimiter = ',')
            rowI = 0
            for row in reader:
                self.datos.setRowCount(rowI+1)
                columns = len(row)
                if rowI == 0:
                    self.datos.setColumnCount(columns)
                
                for columnJ in range(columns):
                    myValue = row[columnJ]
                    cell = QTableWidgetItem(str(myValue))
                    self.datos.setItem(rowI,columnJ,cell)
                rowI = rowI + 1
        finally:
            myFile.close()
            
        
def main():
    app = QApplication(sys.argv)
    
    objeto = clsMainWIn()
    objeto.show()
    app.exec_()
    
if __name__ == '__main__':
    main()