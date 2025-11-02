'''
Ejercicio 2 - Método constructor
Realizar un programa que:
1. De un mensaje de bienvenida al usuario que diga "Automotores La Rueda".
2. Le de un menu de opciones en donde el usuario pueda agregar autos al sistema, ver los autos, cotizarlos o salir del sistema.
3. En caso que seleccione agregar autos, pedirle la marca, el modelo y el costo. Al ingresar el costo del mismo su valor estará 
en dólares. Almacenar el auto en una lista.
4. Si elije ver autos, deberá imprimir una línea con marca, modelo y costo por cada auto almacenado en la lista del punto anterior.
5. Si desea cotizar un auto, el sistema deberá pedirle el modelo del auto y calcular su precio haciendo el producto de su costo por
 la cotización del dólar ($185).
6. Si desea salir del sistema, se le dará un mensaje de despedida y se cerrará la ejecución del programa.
7. En caso que ingrese una opción incorrecta, informárselo y volver al menu.
'''

import pandas as pd
import os

#Definición de la clase
class Auto:
    exchange_rate = 185.0
    ##Constructor
    def __init__(self, marca, modelo, costo_ars):
        self.marca = marca
        self.modelo = modelo
        self.costo_ars = float(costo_ars)
        self.costo_usd = self.cotizar_en_dolares()
    ##Método auxiliar
    def cotizar_en_dolares(self, rate=None):
        rate = rate or self.exchange_rate
        return round(self.costo_ars / rate, 2)
    ##Método que transforma en texto "mostrable"
    def __str__(self):
        return f"Vehículo {self.marca}, {self.modelo} - ${self.costo_ars} - US${self.costo_usd}"    

#Declaración de las variables
lista_autos = []
csv_path = "autos.csv"
if os.path.exists(csv_path):
    df_autos = pd.read_csv(csv_path)
else:
    df_autos = pd.DataFrame(columns=["marca", "modelo", "costo_ars", "costo_usd"])

#Funciones del aplicativo
def agregar_auto():
    marca = input("Ingrese la marca del auto: ").strip()
    modelo = input("Ingrese el modelo del auto: ").strip()
    costo_ars = float(input("Ingrese el costo del auto en ARS (pesos argentinos) $AR$: "))
    auto = Auto(marca, modelo, costo_ars)
    lista_autos.append(auto)
    print("Auto agregado correctamente.")

def ver_autos():
    for auto in lista_autos:
        print(auto)

def cotizar_autos():
    modelo = input("Ingrese el modelo del auto a cotizar: ")
    for auto in lista_autos:
        if auto.modelo == modelo:
            print(f"El costo del auto {auto.marca}, {auto.modelo} es US${auto.costo_usd}")
            break
    else:
        print("Auto no encontrado.")

def guardar_autos_en_csv():
    global df_autos #porque se crea fuera de la función salir()
    if lista_autos: #Si hay algo en la lista
            df_autos_nuevos = pd.DataFrame([{ #se crea el dataframe directamente a partir de la lista
                "marca": auto.marca, 
                "modelo": auto.modelo, 
                "costo_ars": auto.costo_ars, 
                "costo_usd": auto.costo_usd
                } for auto in lista_autos])
            if not df_autos_nuevos.empty:
                df_autos = pd.concat([df_autos, df_autos_nuevos], ignore_index=True) #Se concatenan los preexistentes y los nuevos
                df_autos.to_csv("autos.csv", index=False) #se guarda en el csv al salir del aplicativo

def salir():
    guardar_autos_en_csv()    
    print("Gracias por su visita. Hasta pronto.")
    print("Automotores La Rueda")

#Función de menú reutilizable
def menu():
    print("Automotores La Rueda")
    print("Seleccione una opción:")
    print("1. Agregar autos")
    print("2. Ver autos")
    print("3. Cotizar autos")
    print("4. Salir")

    opcion = int(input("Opcion: "))
    return opcion

while True:
    opcion = menu()

    if opcion == 1:
        agregar_auto()
        pass
    elif opcion == 2:
        ver_autos()
        pass
    elif opcion == 3:
        cotizar_autos()
        pass
    elif opcion == 4:
        salir()
        break
    else:
        print("Opcion incorrecta. Intente nuevamente.")
        pass