#Codigo de Jorge
#Companero Nicolas Gomez

import os
import time 
from collections import defaultdict
 
if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
 
time.sleep(1)
os.system(var) 
print("**************") 
print("*                                      *")
print("*     BANCON - TU BANCO DIGITAL        *")
print("*                                      *")
print("**************")
 
time.sleep(2)
os.system(var)
 
print("**************")
print("*                                      *")
print("*TE PRESENTAMOS TU NUEVO BANCO DIGITAL *")
print("*                                      *")
print("**************")



#Creamos la clase cliente
class Cliente:
    def __init__(self, nombre, apellido, dni, telefono, dirección, ciudad, codigo, mail): #Aqui definimos los atributos de la clase cliente
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.dni = dni
        self.telefono = telefono
        self.dirección = dirección.capitalize()
        self.ciudad = ciudad.capitalize()
        self.codigo = codigo 
        self.mail = mail
        self.monto = 0 

    def __str__(self):
        return(f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"DNI: {self.dni}\n"
                f"Telefono: {self.telefono}\n"
                f"Dirección: {self.dirección}\n"
                f"Ciudad: {self.ciudad}\n"
                f"Codigo Postal: {self.codigo}\n"
                f"Mail: {self.mail}\n"
               )

class funcion_cliente:
    cuentas =  defaultdict(list)
    def __init__(self,dni,monto):  #metodo para sumar un deposito al monto del cliente 
        self.dni = dni
        self.monto = monto
        funcion_cliente.cuentas[self.dni].append(self.monto)
        print(funcion_cliente.cuentas)
        
    def extraer(self,dni,monto):     #metodo para extraer y actualiza el valor de la cuenta del cliente
        self.dni = dni
        self.monto = monto
        funcion_cliente.cuentas[self.dni].append(self.monto)
        print(funcion_cliente.cuentas)

    def retornar_monto(self):     #metodo para mostar el saldo de cada cliente, me sirve para luego sumar todos los montos y sacar el dinero que tiene el banco
        for cuentak, cuentav in funcion_cliente.cuentas.items():
            if cuentak == self.dni:
                return sum(cuentav)

    def imprimir(self):         #metodo
        print(self.dni,"tiene depositado la suma de",self.monto)

        
#creamos la clase Banco 
class Banco:
    
    usuarios = []

    def agregar_cliente(self):
        
       
        print("***********************")
        nombre = input("Digite el Nombre del usuario: ")
        apellido = input("Digite el Apellido del usuario: ")
        dni = int(input("Digite el DNI del usuario: "))
        telefono = int(input("Ingrese el Numero de telefono: "))
        dirección = (input ("Ingresar Dirección: "))
        ciudad = (input("Ingresar Ciudad: "))
        codigo = int(input("Ingresar Codigo Postal: "))
        mail = input("Ingresar Mail: ")
        print("***********************","\n")
        
        #Uso if para que se verifique que no se repita el dni
        if self.buscar_por_dni(dni):
            print("***********************")
            print("\n**PRECAUCÍON ** Ya existe un usuario con el mismo DNI ** ")
            print("***********************")
        else:
            Banco.usuarios.append(Cliente(nombre, apellido, dni, telefono, dirección, ciudad, codigo, mail ))
            print(Banco.usuarios)
    #Buscar por Dni
    def buscar_por_dni(self, dni):
        for usuario in Banco.usuarios:
            if usuario.dni == dni:
                return usuario
            
    #Eliminar por dni
    def eliminar_por_dni(self, dni):
        cont=0
        for usuario in Banco.usuarios:
            if usuario.dni == dni:
                del Banco.usuarios[cont]
                print("Usuario Eliminado")
            else:
                cont+=1
                
    #mostrar Cliente           
    def mostrar_cliente(self, dni):
        cliente = self.buscar_por_dni(dni)
        if cliente:
            print("\n", cliente)
        else:
            print("******************")
            print("\nNo existe un cliente con el DNI seleccionado","\n")
            print("******************")
        
    
    #return False
        
        
        #for usuario in self.usuarios:
            #if usuario == dni:
               # self.usuarios.pop
                #del(usuario)
        
        #cliente = self.buscar_por_dni(dni)
        #if cliente == dni:
            #usuario.dni.pop
            #print("el usuario fue eliminado correctamente")
        
        
        #for i, cliente in enumerate(cliente):
             #if cliente['dni'] == dni:
                #cliente = cliente.pop(i)
               # show(cliente)
               # return true
        #return False
                
                
  
            
        
        

def main():
    time.sleep(1)
    os.system(var)
    banco = Banco()
   
    print("******************")
    print("\n**   BIENVENIDO AL BANCO SUCURSAL 444 CÓRDOBA **","\n")
    print("******************")
    while True:
        try:
            print("**************")
            print("*                                      *")
            print("*         MENU PRINCIPAL               *")
            print("*                                      *")
            print("**************")
            print("\nDigite una opcion: \n\n"
            
                  "  1) Agregar usuario\n"
                  "  2) Visualizar usuario\n"
                  "  3) Eliminar usuario\n"
                  "  4) Generar Deposito\n"
                  "  5) Extracción Caja de Ahorro\n"
                  "  6) Realizar Plazo Fijo\n"
                  "  7) Salir")

            opcion = input("\nDigite una opcion: ")
           
            
            if opcion == "1":
                banco.agregar_cliente()
                
            elif opcion == "2":
                dni = int(input("\nDigite el DNI del usuario que desea buscar: "))
                print("======================================================")
                banco.mostrar_cliente(dni)
                print("======================================================")
                
            elif opcion =="3": 
                
                dni = int(input("\nIngrese DNI del Usuario a Eliminar: "))
                print("======================================================")
                banco.eliminar_por_dni(dni)
                print("======================================================")
               
            
            elif opcion =="4": 
                    
                    print("**********************")
                    dni = int(input("Ingrese su numero de DNI: "))
                    print("**********************","\n")
                    if banco.buscar_por_dni(dni):
                        monto = float(input("Cuanto dinero desea depositar en su cuenta ->"))
                        f1 = funcion_cliente(dni,monto)
                        print("\n")
                        print(f"El dinero se acredito correctamente - Su Saldo es: $", monto)
                        print("**********************")
                        print("\n")
                        print("El total de dinero en su cuenta Caja de Ahorro es: $", f1.retornar_monto())
                        print("**********************")
                        print("\n")
                    else:
                        print("**********************")
                        print("El dni ingresado no pertenece a un cliente del banco")
                        print("**********************")
                        
            elif opcion =="5": 
                print("**********************")
                dni = int(input("Ingrese su numero de DNI: "))
                print("**********************","\n")
                if banco.buscar_por_dni(dni):
                    print("**********************")
                    extraer = float(input("Cuanto dinero desea extrer de su cuenta ->"))
                    if extraer > f1.retornar_monto():
                        print("\n")
                        print("El saldo en su cuenta es insuficiente","\n")
                    else:
                        f1.extraer(dni,(extraer*(-1)))
                        print("\n")
                        print("El total de dinero en su cuenta Caja de Ahorro es: $", f1.retornar_monto(),"\n")
                        print("*********************")
                        
            #elif opcion =="6":
            elif opcion =="7":
                        print("**************************")
                        print(" *Gracias por Utilizar Nuestros Servicios* - Bancon - Tu Banco Digital")
                        print("**************************")
                        quit()
                        
                    
        except ValueError:
            print("\nOpción incorrecta, intentelo nuevamente")
            
            
main()
