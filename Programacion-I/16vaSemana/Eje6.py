class Cliente:
    #Definomos los atributos
    nombre = ""
    __cantidad = 0
    #Inicializamos el metodo
    def __init__(self):
        pass
    
    #Metodo depositar
    def depositar(self, dep):
        self.dep = dep
        Cliente.__cantidad += self.dep 
    
    #Metodo extraer
    
    def extraer(self,ext):
        self.ext = ext
        Cliente.__cantidad -= self.ext
    
    
    def mostrar_total(self):
        print(Cliente.__cantidad) 
        

        

a = Cliente()
a.nombre = "Nicolas"
a.extraer(1000)
a.mostrar_total()
