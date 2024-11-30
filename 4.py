print(" ")# print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ") # print imprime un espacio

class Calculadora: # define una clase
    def __init__(self, num1, num2): # atributos
        self._num1 = num1 # atributo num1
        self._num2 = num2 # atributo num2

    def suma(self): # define suma
        resultado = self._num1 + self._num2 # haciendo operacion
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}") # print imprime resultado

    def resta(self): # define resta
        resultado = self._num1 - self._num2 # haciendo operacion
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}") # print imprime resultado

    def division(self): # define division
        if self._num2 != 0:  
            resultado = self._num1 / self._num2  # haciendo operacion
            print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado:.2f}") # print imprime resultado
        else: 
            print("Error: No se puede dividir entre cero.")

    def multiplicacion(self): # define multiplicacion
        resultado = self._num1 * self._num2 # haciendo operacion
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}") # print imprime resultado

operacion = Calculadora(56, 4) # dando valores
operacion.suma() # suma

print(" ")# print imprime un espacio

operacion = Calculadora(100, 50) # dando valores
operacion.resta() # resta

print(" ")# print imprime un espacio

operacion = Calculadora(456, 3) # dando valores
operacion.division() # division

print(" ")# print imprime un espacio

operacion = Calculadora(12, 5) # dando valores
operacion.multiplicacion() # multiplicacion

print(" ")# print imprime un espacio