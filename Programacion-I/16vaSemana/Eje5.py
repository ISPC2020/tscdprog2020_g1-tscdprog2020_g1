class Agenda:
    l = []
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono 
        self.email = email
    
    def añadir_contacto(self):
        Agenda.l.append(self.nombre)
        Agenda.l.append(self.telefono)
        Agenda.l.append(self.email)
    
    def lista_de_contatos(self):
        lista_str = ""
        k=0
        for i in Agenda.l:
            if k == 0:
                lista_str +="Nombre: " + str(i) + " | "
                k +=1
            elif k == 1:
                lista_str +="Telefono: " + str(i) + " | "
                k +=1    
            else:
                lista_str +="Email: " + str(i)  + "\n"
                k = 0                    
        return lista_str
    
    def buscar_contacto(self,nombrequequierobuscar):
        lista_buscar= ""
        for i in Agenda.l:
            if i == nombrequequierobuscar:
                lista_buscar += "Nombre: " + str(i) + " | "
                c = Agenda.l.index(i)
                c += 1
                lista_buscar += "Telefono: "+ str(Agenda.l[c]) + " | "
                c += 1
                lista_buscar += "Email: "+ str(Agenda.l[c]) + " \n"
        print(lista_buscar)
    
    def editar_contacto(self,nombrequequierocambiar, nombreeditado):
        for i in Agenda.l:
            if i == nombrequequierocambiar:
                c = Agenda.l.index(i)
                Agenda.l[c]= nombreeditado
    

def Menu_agenda():
    while True:
        print("Bienvenido a la AGENDA");
        print("1 Agregar contacto")
        print("2 Lista de contactos");
        print("3 Buscar contacto");
        print("4 Editar contacto");
        print("5 Cerrar Agenda");
        opcion = int(input("Escriba una opcion :  "));
        if 1 == opcion:
            v1= str(input("Ingrese Nombre: "))
            v2 = int(input("Ingrese el Telefono: "))
            v3 = str(input("Ingrese el Email: "))
            e = Agenda(v1,v2,v3)
            e.añadir_contacto()
        
        if 2 == opcion:
            print(e.lista_de_contatos())
        
        if 3 == opcion:
            v1= str(input("Ingrese Nombre que quiere buscar: "))
            e.buscar_contacto(v1)
        
        if 4 == opcion:
            v1= str(input("Ingrese Nombre que quiere editar: "))
            v2= str(input("Ingrese el nombre actulizado: "))
            e.editar_contacto(v1,v2)
        
        if 5 == opcion:
            break
    
Menu_agenda()