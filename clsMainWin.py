from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import csv
import sys
from tempfile import NamedTemporaryFile
import shutil
import clsEstadoForm as estadoForm
from resources import clsController as ctrl

#Hacer dos csv el principal con los datos de la cursada
# y otro con los datos del alumno
class clsMainWIn(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(clsMainWIn, self).__init__(parent)
        uic.loadUi('ui-files/main-table.ui',self)
        self.csvListado = 'csv-files/listado.csv'
        self.csvEstado = 'csv-files/estado.csv'
        self.handy = ctrl.controller(self.csvListado,self.csvEstado)
        #self.auxFIle = 'temporary-listado.csv' #=???
        
        self.setupUiComponents()
        

    def setupUiComponents(self):
        self.handy.refresh_file()
        self.loadTable()
        self.datos.doubleClicked.connect(self.moreData)
        self.btnCerrar.clicked.connect(self.close)
        
    def moreData(self,index):
        column = index.column()
        row = index.row()
        if column == 0:
            print("datos de alumno")
        elif column == 2:
            self.estadoForm = estadoForm.clsEstadoForm(self.csvEstado,row)
            self.estadoForm.show()
            self.estadoForm.alumno.setText("Nombre: "+self.datos.item(row,0).text())
            self.estadoForm.lu.setText("Lu: "+self.datos.item(row,1).text())
            self.estadoForm.updateCsv.connect(self.loadTable)
            
    
    def loadTable(self):
        with open(self.csvListado) as f:
            listado = [*csv.DictReader(f)]
            self.datos.setRowCount(len(listado))
            self.datos.setColumnCount(len(listado[0]))
            count = 0  #problema
            for i in listado:
                myValue = i['alumno']
                cell = QTableWidgetItem(str(myValue))
                self.datos.setItem(count,0,cell)
                myValue = i['lu']
                cell = QTableWidgetItem(str(myValue))
                self.datos.setItem(count,1,cell)
                myValue = i['estado']
                cell = QTableWidgetItem(str(myValue))
                self.datos.setItem(count,2,cell)
                count +=1
                
            
        
def main():
    app = QApplication(sys.argv)
    objeto = clsMainWIn()
    objeto.show()
    app.exec_()
    
if __name__ == '__main__':
    main()