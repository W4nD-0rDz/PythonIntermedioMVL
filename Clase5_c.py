def mayorDeEdad(edad):
        if edad < 0:
            print()
            #raise TypeError("La edad no puede ser negativa")
            raise ValueError("La edad no puede ser negativa")
        elif edad >= 18:
            print()
            print("Eres mayor de edad")
            return True
        else:
            print()
            print("Eres menor de edad")
            return False

#Aquí debe capturarse el error que se levanta dentro de la función.
# try:
#     print(mayorDeEdad(-28))
# except Exception as e:
#     print(f"Error: {e}")

import math

def raizCuadrada(num):
    if num < 0:
        raise ValueError("No se puede calcular la raiz cuadrada de un número negativo")
    return math.sqrt(num)

try:
    print()
    print(raizCuadrada(144))
except Exception as e:
    print(f"Error: {e} ")
finally:
     print("Cálculo finalizado")

