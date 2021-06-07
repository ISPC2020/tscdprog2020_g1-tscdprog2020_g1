class Calculadora:
    # inicializamos los atributos
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        
    #Metodo de suma
    def suma(self):
        return self.valor1 + self.valor2
    
    #Metodo de resta
    def resta(self):
        return self.valor1 - self.valor2
    
    #Metodo de multiplicacion
    def multiplicacion(self):
        return self.valor1 * self.valor2
    
    #Metodo de division
    def division(self):
        return self.valor1 / self.valor2


t = Calculadora(1,2)

print(t.suma())
print(t.resta())
print(t.multiplicacion())
print(t.division())