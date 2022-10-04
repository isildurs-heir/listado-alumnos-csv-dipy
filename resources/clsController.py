import csv
from tempfile import NamedTemporaryFile
import shutil
from multipledispatch import dispatch

class controller():
    def __init__(self,csvListado,csvEstado):
        self.csvListado = csvListado
        self.csvEstado = csvEstado
        self.auxFile = 'temporary.csv'
        self.listado = []
        self.listaEstados = []

    @dispatch()    
    def refresh_file(self):
        self.__load_file()
        self.__update_estado()
        self.__update_file_listado()


    @dispatch(dict)
    def refresh_file(self,data):
        self.__load_file()
        self.__add_row(data)


    def __load_file(self):
        with open(self.csvEstado) as e:
            self.listaEstados = [*csv.DictReader(e)]
        with open(self.csvListado) as l:
            self.listado = [*csv.DictReader(l)]

    def __update_estado(self):
        for i,v in enumerate(self.listaEstados):
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
                self.listado[i]['estado'] = "Cursando"
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
                    self.listado[i]['estado'] = "Regular"
                else:
                    self.listado[i]['estado'] = "Libre"
    
    def __update_file_listado(self):
        aux = [['alumno','lu','estado']]
        for i in self.listado:
            aux.append([i['alumno'],i['lu'],i['estado']])
        with open(self.auxFile,'w',newline ='') as file:
            writer = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC,delimiter=',')
            writer.writerows(aux)
        shutil.move(self.auxFile,self.csvListado)

    def __update_file_estados(self):
        aux = [['1p','1r','2p','2r']]
        for i in self.listaEstados:
            aux.append([i['1p'],i['1r'],i['2p'],i['2r']])
        with open(self.auxFile,'w',newline ='') as file:
            writer = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC,delimiter=',')
            writer.writerows(aux)
        shutil.move(self.auxFile,self.csvEstado)
        
    def __add_row(self,data):
        data['estado'] = 'cursando' #por defecto
        self.listado.append(data)
        estado = { #por defecto
            '1p': "",
            '1r': "",
            '2p': "",
            '2r': ""
        }
        self.listaEstados.append(estado)
        self.__update_file_listado()
        self.__update_file_estados()


#c1 = controller('/home/lobogelido/Desktop/Proyectos/listado-alumnos-csv-dipy/resources/csv-files/listado.csv', '/home/lobogelido/Desktop/Proyectos/listado-alumnos-csv-dipy/resources/csv-files/estado.csv')
#c1.refresh_file({"alumno": 'Saruman el blanco',"lu": "928"})