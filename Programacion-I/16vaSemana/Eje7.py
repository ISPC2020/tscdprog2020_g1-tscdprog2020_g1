#Clase padre Cuenta
class Cuenta:
    #Metodo inicializar los atributos
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    #metodo imprimir Cuenta
    def __str__(self):
        return "Datos del titular: \n" + self.titular + "\nCantidad: \n" + str(self.cantidad)
    

#Clase Plazo Fijo (Hija)     
class PlazoFijo(Cuenta):
    #Metodo inicializar los atributos de la clase padre e hija
    def __init__(self, titular,cantidad, plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo = plazo
        self.interes = interes
    #Metodo para calcular el importe total del interes 
    def importe_interes(self):
        self.importe = self.cantidad * self.interes/100
        return self.importe
    
    #Metodo para imprimir la clase padre e hija
    def __str__(self):
        return super().__str__() + "\nPlazo: \n" + str(self.plazo)  + "\nInteres: \n" + str(self.interes) + "\nTotal de Interes: \n"  + str(self.importe_interes())      
        

#Clase Caja de ahorro (Hija)
class CajaAhorro(Cuenta):
    #metodo para inicializar la clase padre
    def __init__(self, titular,cantidad):
        super().__init__(titular,cantidad)
    #imprimir la clase padre
    def __str__(self):
        return super().__str__()
    
    
var1 = Cuenta("Nicolas",50000)
var2 = PlazoFijo("Aylen",60000,10,15)
var3 = CajaAhorro("Nacho",50000)
print(var1)
print(var2)
print(var3)