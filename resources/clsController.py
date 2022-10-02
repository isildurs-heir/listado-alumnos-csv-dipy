import csv
from tempfile import NamedTemporaryFile
import shutil

class controller():
    def __init__(self,csvListado,csvEstado):
        self.csvListado = csvListado
        self.csvEstado = csvEstado
        self.auxFile = 'temporary.csv'
    
    def refresh_file(self):
        self.__load_file()
    
    def __load_file(self):
        with open(self.csvEstado) as e:
            listaEstados = [*csv.DictReader(e)]
        with open(self.csvListado) as l:
            listado = [*csv.DictReader(l)]
        self.__update_data(listaEstados,listado)
        self.__update_file(listado)
        
    def __update_data(self,listaEstados,listado):
        for i,v in enumerate(listaEstados):
            flag = False
            if v['1p'] == "":
                flag = True
            elif not flag and v['1r'] == "":
                flag = True
            elif not flag and v['2p'] == "":
                flag = True
            elif not flag and  v['2r'] == "":
                flag = True
            if flag:
                listado[i]['estado'] = "Cursando"
            else:  #flag = false   -> no esta cursando
                if v['1p'] != "-" or v['1p'] != "" :
                    flag = int(v['1p'])>=60
                elif not flag and (v['1r'] != "-" or v['1r'] != ""):
                    flag = int(v['1r'])>=60
                if flag:  #si es falso, esta libre
                    flag = False
                    if v['2p'] != "-" and v['2p'] != "":
                        flag = int(v['2p'])>=60
                    elif not flag and  (v['2r'] != "-" and v['2r'] != ""):
                        flag = int(v['2r'])>=60
                if flag:
                    listado[i]['estado'] = "Regular"
                else:
                    listado[i]['estado'] = "Libre"
    
    def __update_file(self,listado):
        aux = [['alumno','lu','estado']]
        for i in listado:
            aux.append([i['alumno'],i['lu'],i['estado']])
        with open(self.auxFile,'w',newline ='') as file:
            writer = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC,delimiter=',')
            writer.writerows(aux)
        shutil.move(self.auxFile,self.csvListado)
        
