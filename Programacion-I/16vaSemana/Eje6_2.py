# Definimos la clase Cliente
class Cliente:
    #Metodo inicializamos
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0
    
    # Metodo para depositar dinero
    def depositar(self,cantidad):
        self.cantidad+=cantidad
 
    # Metodo para extraer dinero
    def extraer(self,cantidad):
        self.cantidad-=cantidad
    
    # Metodo para obtener el total de dinero
    def devolver_cantidad(self):
        return self.cantidad
 
    # Metodo para imprimir los datos del cliente
    def imprimir(self):
        print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)
    
#Definimos la clase Banco, con herencia de la clase Cliente
class Banco():
    #Definimos los atributos, con el metodo init
    def __init__(self):
        self.b1 = Cliente("Nicolas")
        self.b2 = Cliente("Ramiro")
        self.b3 = Cliente("Ale")
    
    #Metodo para operar
    def operaciones(self):
       self.b1.depositar(1000)
       self.b2.depositar(99)
       self.b3.depositar(400)
       self.b1.extraer(486)
       self.b2.extraer(50)
       self.b3.extraer(200)
    
    #Devolver los depositos Totales
    def deposito_totales(self):
        total = self.b1.cantidad+self.b2.cantidad+self.b3.cantidad
        print(total)

#Objeto de la clase Banco
a1 = Banco()
a1.operaciones()
a1.deposito_totales()