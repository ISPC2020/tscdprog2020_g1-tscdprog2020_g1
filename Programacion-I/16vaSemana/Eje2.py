class Persona:
    # inicializamos los atributos
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad 
        
    # Para mostrar los datos
    def __str__(self):
        return "Nombre: " + self.nombre + "\n" + "Edad: " + str(self.edad)
    
    #Fucion para ver si es mayor de edad
    def mayor_de_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"
    
# bloque principal
# creamos los nuevos objetos
p1=Persona("Nicolas",23)
p2=Persona("Nacho",5)

print(p1)
print(p1.mayor_de_edad())

print(p2)
print(p2.mayor_de_edad())

