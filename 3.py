print(" ")# print imprime un espacion
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")# print imprime un espacion

class Triangulo:# define clase
    def __init__(self, lado1, lado2, lado3):# atributos
        self.lado1 = lado1# atributo lado1
        self.lado2 = lado2# atributo lado2
        self.lado3 = lado3# atributo lado3

    def lado_mayor(self):# dfine lado mayor
        return max(self.lado1, self.lado2, self.lado3)# devuelve el lado maximo

    def tipodetriangulo(self):# define tipo de triangulo
        if self.lado1 == self.lado2 == self.lado3:# abriendo if
            return 'Equilátero'# devuelve equilatero
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:# elif
            return 'Isósceles'# devuelve isosceles
        else:# else
            return 'Escaleno'# devuelve equilatero

lado1 = float(input("Introduce el primer lado del triángulo: "))# pide que ungreses el primer lado
print(" ") # print imprime un espacio
lado2 = float(input("Introduce el segundo lado del triángulo: "))# pide que ungreses el segundo lado
print(" ") # print imprime un espacio
lado3 = float(input("Introduce el tercer lado del triángulo: "))# pide que ungreses el tercer lado

triangulo = Triangulo(lado1, lado2, lado3)# dando datos
print(" ") # print imprime un espacio
print(f"El lado mayor del triángulo es: {triangulo.lado_mayor()}") # print imprime el lado mayor del triangulo
print(" ") # print imprime un espacio
print(f"El triángulo es: {triangulo.tipodetriangulo()}")# print imprime el tipo de triangulo

print(" ") # print imprime un espacio