print(" ")# print imprime un espacion
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")# print imprime un espacion

class Agenda:# define clase
    def __init__(self):# define __init__
        self.contactos = []# contactos

    def anadir_contacto(self):# define añadir contactos
        self.contactos.append(input("Nombre, Teléfono, Email: "))# pide que ingreses el nombre, telefono y email

    def listar_contactos(self):# define listar contactos
        print("\n".join(self.contactos))# print imprimiendo

    def buscar_contacto(self):# define biscar contacto
        nombre = input("Nombre: ")# pide nombre
        for contacto in self.contactos:# bucle for
            if contacto.startswith(nombre):# abriendo if
                print(contacto)# print contacto
                return
        print("No encontrado.")# print imprime no encontrado

    def editar_contacto(self):# define editar contacto
        nombre = input("Nombre: ")# pide nombre
        for i, contacto in enumerate(self.contactos):# bucle for
            if contacto.startswith(nombre):# abriendo if
                self.contactos[i] = input("Nuevo Nombre, Teléfono, Email: ")# pide nuevo nombre, telefono y email

    def menu(self):# define menu
        opciones = {# abriendo diccionario
            "1": self.anadir_contacto,# dando dato
            "2": self.listar_contactos,# dando dato
            "3": self.buscar_contacto,# dando dato
            "4": self.editar_contacto,# dando dato
            "5": exit# dando dato
        }# cerrando diccionario

        while True:# bucle while
            opcion = input("\n1. Añadir\n2. Lista\n3. Buscar\n4. Editar\n5. Salir\nOpción: ")# pide que eljas una opcion
            if opcion in opciones:# abriendo if
                opciones[opcion]()# opciones

agenda = Agenda()# agenda
agenda.menu()# menu

print(" ")# print imprime un espacion