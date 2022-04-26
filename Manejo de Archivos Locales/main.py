
class Materia():
    def __init__(self,nombre,profesor,alumnos):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = alumnos
    def showData(self):
        print("Nombre: "+self.nombre)
        print("Profesor: "+self.profesor)
        print("Alumno: "+self.alumnos)
        print(self)

def LoadData():
    #Leer informacion
    with open("Manejo de Archivos Locales/prueba.txt", encoding="utf8", errors='ignore') as Data:
        text = Data.read()
        list_line = text.split("\n")
        list_line.pop(0)
        for line in list_line:
            texto = line.split("-")
            Clase = Materia(texto[0],texto[1],texto[2])
            Clase.showData()
    
def LoadData2():
    #Leer Informacion
    archivo = open("Manejo de Archivos Locales/prueba/prueba2.txt","r")
    #Codigo
    txt = archivo.read()
    archivo.close()

    #Escribir Informacion
    archivo = open("Manejo de Archivos Locales/prueba/prueba2.txt","w")
    #Codigo
    for i in range(1000000):
        txt += str(i) + "\n"
    archivo.write(txt)
    archivo.close()




LoadData2()