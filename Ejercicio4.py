'''
Crear un programa en python que:
1. De un mensaje de bienvenida que indique "Ferretería La Tuerca"

2. Le permita al usuario ingresar productos en cuatro categorías: 
Artículos de ferretería, 
Artículos de electricidad, 
Herramientas 
Máquinas.

3. Todos los productos deberán tener:
código, 
nombre 
precio
se podrá acceder a esta información mediante un método.

4. Los artículos tendrán un número de stock y un método que nos indique "Debe Comprar" si el mismo menor  a 100.

5. Los artículos eléctricos deberán poseer además el dato de tensión y se deberá poder acceder a un método que 
defina si es de baja tensión (menos a 48V) o no.

6. Las herramientas deberán tener un rubro (electricidad, construcción, plomería, etc).  
Se deberá poder acceder a un método que informe el rubro al que pertenece.

7. Las máquinas deberán tener un valor de potencia
Tendrán unmétodo que nos indique "Es de consumo alto" si la potencia es superior a los 2500W.

8. Cada vez que se ingrese un producto en el sistema, se deberán ejecutar todos los métodos correspondientes a su categoría.'''

#SUPERCLASE
class Articulo:
    def __init__(self, codigo, nombre, precio, stock = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.submenu = {
            1: ("Controlar stock", self.controlar_stock),
            2: ("Mostrar artículo", self.mostrar_info),
            0: ("Volver", None)  
            }

    def controlar_stock(self):
        diferencia = 100 - self.stock
        if self.stock < 100:
            print(f"Debe comprar {diferencia} unidades de {self.nombre}")
        else:
            print("No debe comprar")

    def mostrar_info(self):
        print(f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}")

    def convertir_a_lista(self):
        return [self.codigo, self.nombre, self.precio, self.stock, ""]

#CLASES
class ArticuloFerreteria(Articulo):
    def __init__(self, codigo, nombre, precio, stock):
        super().__init__(codigo, nombre, precio, stock)

class ArticuloElectrico(Articulo):
    def __init__(self, codigo, nombre, precio, stock, tension):
        super().__init__(codigo, nombre, precio, stock)
        self.tension = tension
        self.submenu.update({
            3: ("Identificar Tensión", self.determinar_tension)
        })

    def determinar_tension(self):
        if int(self.tension) < 50:
            print("Es de muy baja tensión")
        else:
            print("Es de baja tensión")
    
    def convertir_a_lista(self):
        return [self.codigo, self.nombre, self.precio, self.stock, f"{self.tension}V"]

class ArticuloHerramienta(Articulo):
    def __init__(self, codigo, nombre, precio, stock, rubro):
        super().__init__(codigo, nombre, precio, stock)
        self.rubro = rubro
        self.submenu.update({
            3: ("Identificar Rubro", self.mostrar_rubro)
        })

    def mostrar_rubro(self):
        print(f"El rubro de la herramienta es: {self.rubro}")

    def convertir_a_lista(self):
        return [self.codigo, self.nombre, self.precio, self.stock, self.rubro]

class ArticuloMaquina(Articulo):
    def __init__(self, codigo, nombre, precio, stock, potencia):
        super().__init__(codigo, nombre, precio, stock)
        self.potencia = potencia
        self.submenu.update({
            3: ("Identificar tipo de Consumo", self.calcular_consumo)
        })

    def calcular_consumo(self):
        if self.potencia > 2500:
            print("Es de consumo alto")
        else:
            print("Es de bajo consumo")
    
    def convertir_a_lista(self):
        return [self.codigo, self.nombre, self.precio, self.stock, f"{self.potencia}W"]

#CLASES CON HERENCIA MULTIPLE
class ArticuloMaquinaElectrica(ArticuloMaquina, ArticuloElectrico):
    def __init__(self, codigo, nombre, precio, stock, potencia, tension):
        #Para evitar construir dos veces Articulo por medio de las clases padres (Maquina y Electrico)
        Articulo.__init__(self, codigo, nombre, precio, stock) 
        self.potencia = potencia
        self.tension = tension
        self.intensidad = float(potencia)/float(tension)
        self.submenu.pop(3, None)  # elimina posibles duplicados
        self.submenu.update({
            3: ("Mostrar Ficha Técnica", self.mostrar_ficha)
        })
    #anulo los métodos de los padres
    def determinar_tension(self):
        pass

    def calcular_consumo(self):
        pass

    def mostrar_ficha(self):
        print(f"Intensidad de trabajo: {self.intensidad:.2f}A")
        print(f"Potencia de trabajo: {self.potencia}W")
        print(f"Tensión de trabajo: {self.tension}V")

    #sobreescribo el convertir_a_lista del abuelo
    def convertir_a_lista(self):
        ficha = f"{self.intensidad:.2f}A | {self.potencia}W | {self.tension}V"
        return [self.codigo, self.nombre, self.precio, self.stock, ficha]

class ArticuloHerramientaFerreteria(ArticuloFerreteria, ArticuloHerramienta):
    def __init__(self, codigo, nombre, precio, stock, rubro):
        #Para evitar construir dos veces Articulo por medio de las clases padres (Herramienta y Ferreteria)
        Articulo.__init__(self, codigo, nombre, precio, stock)
        self.rubro = rubro
        self.submenu.pop(3, None)  # elimina posibles duplicados
        self.submenu.update({
            3: ("Identificar Rubro", self.mostrar_rubro)
        })

    #Sobrescribo el método del abuelo para usar un stock mínimo distinto.
    def controlar_stock(self):
        minimo = 50
        diferencia = minimo - self.stock
        if self.stock < minimo:
            print(f"⚠️ Debe reponer {diferencia} unidades del artículo '{self.nombre}' (rubro: {self.rubro})")
        else:
            print(f"✅ Stock suficiente de {self.nombre}")
 
    def mostrar_rubro(self):
        pass

    #Invoco explicitamente la versión de la clase padre ArticuloHerramienta
    def convertir_a_lista(self):
        return ArticuloHerramienta.convertir_a_lista(self)

#########################################
#Librerías
import os
import pandas as pd
import csv
from menu_utils import Menu

#1- Funciones auxiliares
csv_path = "ferreteria.csv"

#Si hay articulos cargados en archivo csv, genera contadores 
# para garantizar que los códigos no se repitan y que los articulos se archiven correctamente
def obtener_contadores(csv_path):
    contadores = {"1": 0, "2": 0, "3": 0, "4":0, "5":0, "6":0}
    if os.path.exists(csv_path):
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                codigo = row["codigo"]
                tipo = codigo.split("-")[1]
                if tipo in contadores:
                    contadores[tipo] +=1
    else:
        #cuando el archivo aun no se ha generado
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["codigo", "nombre", "precio", "stock", "otros"])
            
    return contadores

#Generar código de artículo
def generar_codigo(tipo, contadores):
    contadores[tipo] += 1
    return f"0000-{tipo}-{contadores[tipo]}"

#2- Mostrar el submenú interactivo de los artículos de la Ferretería hasta que se elija salir
def abrir_submenu(articulo):
    menu = Menu(titulo=f"Submenú {articulo.codigo} {articulo.nombre} {articulo.precio} {articulo.stock}", opciones=articulo.submenu, salida=0)
    menu.mostrar()

#3- Carga de artículo
def cargar_articulo(tipo, contadores):
    tipo = str(tipo)
    if tipo in contadores:
        codigo = generar_codigo(tipo, contadores)
        nombre = input("Tipee el nombre del artículo: ")
        precio = float(input("Ingrese el precio del artículo: "))
        stock = int(input("Indique la cantidad de artículos en stock: "))

        if tipo == "1":
            tension = input("Indique la tensión que admite el artículo eléctrico (v): ")
            articulo = ArticuloElectrico(codigo, nombre, precio, stock, tension)
        elif tipo == "2":
            rubro = input("Indique el rubro de la herramienta (electricidad, construcción, plomería, etc): ")
            articulo = ArticuloHerramienta(codigo, nombre, precio, stock, rubro)
        elif tipo == "3":
            potencia = int(input("Indique la potencia del equipo (W): "))
            articulo = ArticuloMaquina(codigo, nombre, precio, stock, potencia)
        elif tipo =="4":
            articulo = ArticuloFerreteria(codigo, nombre, precio, stock)
        elif tipo == "5":
            potencia = int(input("Indique la potencia del equipo (W): "))
            tension = input("Indique la tensión que admite el artículo eléctrico (v): ")
            articulo = ArticuloMaquinaElectrica(codigo, nombre, precio, stock, potencia, tension)
        elif tipo == "6":
            rubro = input("Indique el rubro de la herramienta (electricidad, construcción, plomería, etc): ")
            articulo = ArticuloHerramientaFerreteria(codigo, nombre, precio, stock, rubro)

    else:
        print("tipo de artículo inexistente.")
        return

    return articulo

#Guardar artículo en el archivo csv.
def guardar_articulo(articulo):
    registro = articulo.convertir_a_lista()
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer =csv.writer(f)
        writer.writerow(registro)
        print(f"Artículo {articulo.codigo} guardado con exito.")

#Llamar a cargar_articulo y guardar_articulo        
def cargar_y_guardar():
    contadores = obtener_contadores(csv_path)
    sub_menu = Menu(titulo="Seleccione el tipo de artículo", opciones={
        1: ("Artículo Electrico", None),
        2: ("Articulo Herramienta", None),
        3: ("Articulo Maquina", None),
        4: ("Articulo Ferreteria", None),
        5: ("Articulo Maquina Electrica", None),
        6: ("Articulo Herramienta Ferreteria", None),
        0: ("Salir", None)
    }, salida=0)
    tipo = sub_menu.mostrar()
    if tipo == 0:
        return
    art = cargar_articulo(tipo, contadores)
    if art:
        # Ejecutar todos los métodos correspondientes
        art.controlar_stock()  # todos los artículos tienen este método

        # Ejecutar métodos específicos según la subclase
        if isinstance(art, ArticuloElectrico):
            art.determinar_tension()
        elif isinstance(art, ArticuloHerramienta):
            art.mostrar_rubro()
        elif isinstance(art, ArticuloMaquina):
            art.calcular_consumo()
        elif isinstance(art, ArticuloFerreteria):
                art.mostrar_info()

        guardar_articulo(art)

#4- Ver articulo:
def ver_articulos():
    if not os.path.exists(csv_path):
        print("No hay artículos registrados aun.")
        return
    df = pd.read_csv(csv_path)
    print(df.to_string(index=False))

#5 Salida
def salir():
    print("🛠️ Ferretería 🛠️ La Tuerca 🛠️ agradece su visita.")
    exit()

#5- Menu general: carga de artículos, ver la lista de artículos y entrar al submenú de un artículo
def menu_principal():
    menu = Menu(titulo="Ferretería 🛠️ La Tuerca 🛠️",
    opciones={
            1: ("Cargar Artículo", cargar_y_guardar),
            2: ("Ver Artículos", ver_articulos),
            0: ("Salir", salir)
    }, salida=0)
    while True:
        menu.ejecutar_opcion()


#6- Punto de ejecución:
if __name__ == "__main__":
    menu_principal()
