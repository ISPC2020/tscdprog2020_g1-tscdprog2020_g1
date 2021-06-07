class Triangulo:
    # inicializamos los atributos
    def __init__(self,ladoa,ladob,ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc
        
    #Metodo de tipo de triangulo
    def tipo_triangulo(self):
        if self.ladoa == self.ladob and  self.ladoa != self.ladoc and  self.ladob !=  self.ladoc:
            return "Isosceles"
        elif self.ladoa != self.ladob and  self.ladoa != self.ladoc and  self.ladob !=  self.ladoc:
            return "Escaleno"
        elif self.ladoa == self.ladob and  self.ladoa == self.ladoc and  self.ladob ==  self.ladoc:
            return "Equilatero"
    
    #Metodo que lado es mayor
    def lado_mayor(self):
        if self.ladoa > self.ladob and self.ladoa > self.ladoc:
            return "Izquierdo"
        elif self.ladob > self.ladoa and self.ladob > self.ladoc:
            return "Derecho"
        elif self.ladoc > self.ladoa and self.ladoc > self.ladoa:
            return "Inferior"
        else:
            return "Iguales"
    
    
    # Metodo imprimir
    def __str__(self):
        if self.lado_mayor() == "Iguales":
            return "Los lados son " + str(self.lado_mayor()) +", el tipo de triangulo es "+ str(self.tipo_triangulo()) 
        else:
            return "El lado mayor es el " + str(self.lado_mayor()) +", el tipo de triangulo es "+ str(self.tipo_triangulo())

t1= Triangulo(10,10,30)

print(t1)