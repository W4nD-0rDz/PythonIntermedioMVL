#Funciones de cálculo
def sumar(num1, num2):
    return num1 + num2
def restar(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operación equivocada"

print("\n=== CALCULADORA ===\n")

#Variables
while True:
    try:
        num1= (float(input("Ingrese un número: ")))
        num2= (float(input("Ingrese otro número: ")))
        break
    except ValueError:
        print("El valor ingresado no es correcto. Intente nuevamente.")

operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

#Condicionales
if operacion == "+":
    print(sumar(num1, num2))
    print()
elif operacion == "-":
    print(restar(num1, num2))
    print()
elif operacion == "*":
    print(multiplicar(num1, num2))
    print()
elif operacion == "/":
    print(dividir(num1, num2))
    print()
else:
    print("operando inválido")
    print()

#Línea de código final (que debe ejecutarse siempre)
print("Operación matemática ejecutada con éxito.\n")

          
    

