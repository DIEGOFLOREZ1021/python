import datetime

class Alumno:
    """ Comentarios de uso de la clase """
    # Variables o propiedades de la clase
    nombre = None
    apellido1= None
    apellido2= None
    fechaNacimiento = None

    # Funcion constructora que se ejecuta al crear (instanciar) el objeto
    def __init__(self,nombre,apellido1,apellido2 = "") -> None:
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
    
    def setBirthday(self, fecha):
        try:
            if(len(fecha)==8):
                self.Birthday = datetime.strptime(fecha,"%d,%m,%y").date()
            else:
                self.Birthday = datetime.strptime(fecha,"%d,%m,%Y").date()
            
            return True
        
        except:
            return False
    
    
    def getAge(self):
        if (self.Birthday == None):
            return -1
        else:
            return datetime.now().year - self.Birthday.year

class estudiante (Alumno):
    curso = None

alumno = estudiante("Diego", "Florez")
print("Me llamo : ",estudiante.getFullName())
estudiante.curso = "3A"
print("Curso: ",estudiante.curso)

# Creamos un objeto (instanciamos un objeto) ejecutando la funcion constructora



