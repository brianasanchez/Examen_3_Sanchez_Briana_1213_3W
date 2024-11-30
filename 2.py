print(" ")# print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")# print imprime un espacio

class Persona: # define una clase
    def __init__(self, nombre='', edad=0, ): # atributos
        self.nombre = nombre# atributo nombre
        self.edad = edad# atributo dato

    def mostrar(self):# define mostrar
        print(f"Nombre: {self.nombre} Edad: {self.edad}") # print imprime nombre y edad

    def mayor(self):# definiendo es mayor de edad
        return self.edad >= 18 # mayor de 18

persona = Persona("Leonardo", 16)# dando datos
persona.mostrar() # mostrar

print(" ")# print imprime un espacio

print("Es mayor de edad:", persona.mayor()) # print imprime si la persona es mayor de edad o no

print(" ") # print imprime un espacio
