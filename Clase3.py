#HERENCIA
"""Una empresa llamada LogiTrans gestiona vehículos que pueden ser terrestres, aéreos o acuáticos.
Todos los vehículos comparten algunos atributos y comportamientos básicos, pero cada tipo tiene características propias."""

#Superclase
class Vehiculo:
    def __init__(self, patente, marca, modelo, anio, **kwargs): #**kwargs para herencia múltiple
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.submenu = {
            1: ("Lavar", self.lavar),
            2: ("Realizar revisación técnica anual", self.revisar),
            3: ("Mostrar datos", self.mostrar),
            0: ("Volver", None)  
            }
        
    def lavar(self):
        print("Lavando...")
        print("Lavando...")    
        print("Lavado.")
    
    def revisar(self):
        print("Revisando...")
        print("Revisando...")
        print("Revisado.")
    
    def mostrar(self):
        print(f"Patente: {self.patente}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")

#Clases
class VehiculoTerrestre(Vehiculo):
    def __init__(self, patente, marca, modelo, anio, cant_ejes, num_ruedas, **kwargs):
        super().__init__(patente=patente, marca=marca, modelo=modelo, anio=anio,**kwargs)
        self.cant_ejes = cant_ejes
        self.num_ruedas = num_ruedas
        self.submenu.update({
            4: ("Revisar ruedas", self.revisar_ruedas)
        })

    def revisar_ruedas(self):
        if self.num_ruedas >2:
            for eje in range(self.cant_ejes):
                print("Revisando rueda izquierda...")
                print("Revisando rueda derecha...")
                print("Ruedas revisadas.")
    
    def mostrar(self):
        super().mostrar()
        print(f"Ejes: {self.cant_ejes}")
        print(f"Ruedas: {self.num_ruedas}")

class VehiculoAereo(Vehiculo):
    def __init__(self, patente, marca, modelo, anio, cant_motor, tipo, **kwargs):
        super().__init__(patente=patente, marca=marca, modelo=modelo, anio=anio,**kwargs)
        self.cant_motor = cant_motor
        self.tipo = tipo
        self.submenu.update({
            4: ("Revisar motor", self.revisar_motor),
        })

    def revisar_motor(self):
        for motor in range(self.cant_motor):
            print("Revisando motor...")
            print("Motor revisado.")

    def mostrar(self):
        super().mostrar()
        print(f"Motor: {self.cant_motor}")
        print(f"Tipo de aeronave:{self.tipo}")

class VehiculoAcuatico(Vehiculo):
    def __init__(self, patente, marca, modelo, anio, eslora, tipo_propulsion, **kwargs):
        super().__init__(patente=patente, marca=marca, modelo=modelo, anio=anio,**kwargs)
        self.eslora = eslora
        self.tipo_propulsion = tipo_propulsion
        self.submenu.update({
            4: ("Echar anclas", self.anclar)            
        })

    def anclar(self):
        print("Anclando...")
        print("Anclando...")
        print("Anclado. El vehículo está estable en el agua")

    def mostrar(self):
        super().mostrar()
        print(f"Eslora: {self.eslora} metros")
        print(f"Tipo de propulsión: {self.tipo_propulsion}")

#Subclases
class Automovil(VehiculoTerrestre):
    def __init__(self, patente, marca, modelo, anio, cant_ejes, num_ruedas, cant_motor, tipo):
        super().__init__(patente, marca, modelo, anio, cant_ejes, num_ruedas)
        self.cant_motor = cant_motor
        self.tipo = tipo
        self.submenu.update({
            4: ("Revisar motor", self.revisar_motor)
        })

    def revisar_motor(self):
        for motor in range(self.cant_motor):
            print("Revisando motor...")
            print("Motor revisado.")

    def mostrar(self):
        super().mostrar()
        print(f"Motor: {self.cant_motor}")
        print(f"Tipo de aeronave:{self.tipo}")

class Barco(VehiculoAcuatico):
    def __init__(self, patente, marca, modelo, anio, eslora, tipo_propulsion, vela = False):
        super().__init__(patente, marca, modelo, anio, eslora, tipo_propulsion)
        self.vela = vela
        self.submenu.update({
            5: ("Navegar sin motor", self.navegar_sin_motor)
        })

    def navegar_sin_motor(self):
        if self.vela == True:
            print("Navegando sin motor...")
        else:
            print("Si se apaga el motor... a los botes!!! Mujeres y niños primero!!!")

    def mostrar(self):
        super().mostrar()
        if self.vela == True:
            print("El barco tiene vela")
        else:
            print("El barco no tiene vela")

class Helicóptero(VehiculoAereo):
    def __init__(self, patente, marca, modelo, anio, cant_motor, tipo, helice = True):
        super().__init__(patente, marca, modelo, anio, cant_motor, tipo)
        self.helice = helice
        self.submenu.update({
            4: ("Revisar hélice", self.revisar_helice)
        })

    def revisar_helice(self):
        if self.helice:
            print("Revisando hélice...")
            print("Hélice revisada.")
        else:
            print("No hay hélice para revisar.")

    def mostrar(self):
        super().mostrar()
        print("El helicóptero tiene hélice" if self.helice else "El helicóptero no tiene hélice")


#Herencia múltiple
class Hidroavion(VehiculoAcuatico, VehiculoAereo):
    def __init__(self, patente, marca, modelo, anio, eslora, tipo_propulsion, cant_motor, tipo, modo_actual="acuático", cant_pasajeros=1):
        super().__init__(patente=patente, marca=marca, modelo=modelo, anio=anio,
                         eslora=eslora, tipo_propulsion=tipo_propulsion,
                         cant_motor=cant_motor, tipo=tipo)
        self.modo_actual = modo_actual
        self.cant_pasajeros = cant_pasajeros
        self.submenu.update({
            5: ("Cambiar modo", self.cambiar_modo)
        })

    def cambiar_modo(self):
        if self.modo_actual == "acuático":
            self.modo_actual = "aereo"
            print("Modo aereo activado")
        else:
            self.modo_actual = "acuático"
            print("Modo acuático activado")

    def mostrar(self):
        super().mostrar()
        print(f"Modo actual: {self.modo_actual}")
        print(f"Capacidad de pasajeros: {self.cant_pasajeros}")

class MotoDeAgua(VehiculoTerrestre, VehiculoAcuatico):
    def __init__(self, patente, marca, modelo, anio, cant_ejes, num_ruedas, eslora, tipo_propulsion, modo_actual="acuático", cant_pasajeros=1):
        super().__init__(patente=patente, marca=marca, modelo=modelo, anio=anio,
                         cant_ejes=cant_ejes, num_ruedas=num_ruedas,
                         eslora=eslora, tipo_propulsion=tipo_propulsion)
        self.modo_actual = modo_actual
        self.cant_pasajeros = cant_pasajeros
        self.submenu.update({
            5: ("Cambiar modo", self.cambiar_modo)
        })

    def cambiar_modo(self):
        if self.modo_actual == "acuático":
            self.modo_actual = "terrestre"
            print("Modo terrestre activado")
        else:
            self.modo_actual = "acuático"
            print("Modo acuático activado")
    
    def mostrar(self):
        super().mostrar()
        print(f"Modo actual: {self.modo_actual}")
        print(f"Capacidad de pasajeros: {self.cant_pasajeros}")

######################################
#Experimento 1:
"""h = Hidroavion("H123", "Cessna", "SeaPlane", 2022, 10, "motor a combustión", 2, "biplaza", "acuático", 4)
h.mostrar()

print("\nOrden de resolución de métodos (MRO):")
for cls in Hidroavion.mro():
    print(cls.__name__)"""

##########################################

# ========================
# BLOQUE PRINCIPAL DE PRUEBAS
# ========================

#1- importa el menú reutilizable
from menu_utils import Menu  

#2- Muestra el submenú interactivo del vehículo recibido hasta que se elija salir
def abrir_submenu(vehiculo):
    menu = Menu(titulo=f"Submenú {vehiculo.marca} {vehiculo.modelo}", opciones=vehiculo.submenu, salida=0)
    menu.mostrar()

#3- Crear instancias de cada subclase
auto = Automovil("AA123BB", "Toyota", "Corolla", 2020, 2, 4, 1, "sedán")
barco = Barco("B999", "Beneteau", "Oceanis", 2018, 15, "vela", True)
helicoptero = Helicóptero("H500", "Bell", "206", 2015, 1, "ligero", True)
hidroavion = Hidroavion("H123", "Cessna", "SeaPlane", 2022, 10, "motor a combustión", 2, "biplaza", "acuático", 4)
motoagua = MotoDeAgua("M456", "Yamaha", "WaveRunner", 2023, 1, 0, 3, "jet", "acuático", 2)

#4- Diccionario de objetos disponibles
vehiculos_menu = {
    1: ("Automóvil", lambda: abrir_submenu(auto)),
    2: ("Barco", lambda: abrir_submenu(barco)),
    3: ("Helicóptero", lambda: abrir_submenu(helicoptero)),
    4: ("Hidroavión", lambda: abrir_submenu(hidroavion)),
    5: ("Moto de agua", lambda: abrir_submenu(motoagua)),
    0: ("Salir", None)
}

#5- Muestra el menú principal de vehículos y permite seleccionar submenús o salir
menu_principal = Menu(titulo="Menú principal de LogiTrans", opciones=vehiculos_menu, salida=0)
menu_principal.mostrar()
