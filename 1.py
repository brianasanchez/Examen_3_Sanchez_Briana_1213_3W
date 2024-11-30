print(" ")# print imprime un espacion
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")# print imprime un espacion

class Estudiante: # Define una clase
    def __init__(self, nombre, nota): # atributos
        self.nombre = nombre # atributo nombre
        self.nota = nota # atributo nota

    def imprimir(self): # Define un método
        print(f"Nombre: {self.nombre} Nota: {self.nota}") # print imprime nombre y nota

    def resultados(self): # define resultado
        if self.nota >= 6: # mayor a 6
            print("¡Has APROBADO!")  # print imprime si aprobo
        else: # imprime parte falsa
            print("¡Has REPROBADO!") # imprime si reprobo

estudiante1 = Estudiante("Dayana", 9)  # dando valores
estudiante1.imprimir() # imprimir 
estudiante1.resultados() # resultado

print(" ")# print imprime un espacion

estudiante2 = Estudiante("Sofia", 5) # dando valores
estudiante2.imprimir()  # imprimir 
estudiante2.resultados()  # resultado

print(" ") # print imprime un espacion