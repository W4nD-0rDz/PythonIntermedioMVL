'''
Crear un programa en python que:
1. De un mensaje inicial que diga "Bienvenido a la ANSES"
2. Le pida a través de un menú al usuario que seleccione entre las opciones registrarse, 
ver usuarios, ver datos, borrar usuario y salir del sistema.
3. Si selecciona la opción registrarse deberá almacenar en una lista llamada usuarios un objeto que contenga el nombre, 
el dni y la edad del usuario. 
Si la edad no es un valor numérico deberá ejecutar una excepción para que la reingrese.
4. El usuario deberá también ingresar una clave la cual deberá no podrá ser accesible desde fuera de la clase. 
Al ingresarla, deberá confirmarla y si lo hace correctamente le imprimirá un mensaje que diga "contraseña almacenada correctamente".
5. Todos los nombres ingresados deberán almacenarse en una lista llamada nombre.
6. Si el usuario selecciona la opción ver usuarios, deberán imprimirse desde la lista nombres todos los usuarios registrados hasta el momento.
7. Si selecciona la opción ver datos, el sistema le pedirá el dni del usuario que desea ver. 
Al ingresarlo le imprimirá todos los datos (nombre, edad, dni y contraseña). En caso que ingrese un dni que no se encuentra en el sistema, informárselo.
8. Si selecciona borrar usuario, el sistema le pedirá el nombre y lo eliminará de la lista nombres. 
En caso que ingrese un usuario que no se encuentra registrado, el programa se lo informará.
9. Si selecciona la opción salir, e le dará un mensaje de despedida y cerrará la ejecución del programa.
10. Todas las opciones deberán regresar al menú al terminar de ejecutarse.'''
from datetime import datetime, date
import os
import csv
from tabulate import tabulate
from menu_utils import Menu

#0 Crear csv
csv_path = "anses.csv"
if not os.path.exists(csv_path):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nombre", "dni", "fecha_nacimiento", "edad", "clave", "alta"])


#SUPERCLASE
class Persona():
    def __init__(self, nombre, dni, fecha_nacimiento):
        self._nombre = nombre
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
        
#CLASE
class Usuario(Persona):
    def __init__(self, nombre, dni, fecha_nacimiento, clave=""):
        super().__init__(nombre, dni, fecha_nacimiento)
        self.__edad = self.__calcular_edad()
        self.__clave = self.__validar_clave(clave)

    def __calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self._fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self._fecha_nacimiento.month, self._fecha_nacimiento.day):
            edad -= 1
        return edad

    def __validar_clave(self, clave):
        if len(clave) < 6:
            raise ValueError("La clave debe tener al menos 6 caracteres.")
        if len(set(clave)) != len(clave):
            raise ValueError("La clave debe contener caracteres distintos.")
        if not any (c.isdigit () for c in clave):
            raise ValueError("La clave debe contener al menos un número.")
        if not any (c.isupper () for c in clave):
            raise ValueError("La clave debe contener al menos una letra mayúscula.")
        if not any (c.islower () for c in clave):
            raise ValueError("La clave debe contener al menos una letra minúscula.")
        if not any (c in "!@#$%&?¡¿/*-_+" for c in clave):
            raise ValueError("La clave debe contener al menos un caracter especial.")
        return clave
    
    def convertir_a_lista(self):
        return list([self._nombre, self._dni,  str(self._fecha_nacimiento), self.__edad, self.__clave])
    
    def mostrar_datos(self):
        print(f"Nombre: {self._nombre} ({self.__edad})")
        print(f"DNI: {self._dni}")
        print(f"Fecha de nacimiento: {self._fecha_nacimiento}")
        print(f"Clave: {self.__clave}")

#1 Registrarse
def registrar():
    print ("Bienvenido al sistema de Registro de ANSES")
    nombre = input("Ingrese su nombre completo: ").strip()
    while True:
        try:
            dni = input("Ingrese su DNI: ").strip()
            validar_dni(dni)
            break
        except Exception as e:
            print("Error: ",e)
            print("Intente nuevamente.")

    while True:
        try:
            print("A continuación ingrese su fecha de nacimiento:")
            dia = int(input("Día (XX):"))
            mes = int(input("Mes (XX): "))
            año = int(input("Año (XXXX): "))
            fecha_nacimiento = date(año, mes, dia)
            validar_fecha(fecha_nacimiento)
            break
        except Exception as e:
            print("Error: ",e)
            print("Intente nuevamente.\n")
    
    while True:
        try:
            clave = input("Ingrese una clave de 6 (seis) dígitos alfanuméricos.\n"
            "Tenga en cuenta: no repetir caracteres.\n"
            "Debe incluir al menos 1 Letra mayúscula, 1 número, 1 letra minúscula,\n"
             "y al menos 1 caracter especial (!@#$%&?¡¿/*-_+): ")
            # Validación preliminar: probamos crear el usuario temporalmente
            _ = Usuario(nombre, dni, fecha_nacimiento, clave)
            print("✔ Clave almacenada correctamente.\n")
            break
        except Exception as e:
            print("Error: ",e)
            print("Intente nuevamente.")

    usuario = Usuario(nombre, dni, fecha_nacimiento, clave)
    return usuario

def almacenar(id, usuario):
    registro = usuario.convertir_a_lista()    
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer =csv.writer(f)
        writer.writerow([id] + registro + ["True"])
        print(f"Usuario DNI: {registro[1]} guardado con exito.")
    
def registrar_almacenar():
    usuario = registrar()
    #Si el archivo existe...
    if os.path.exists(csv_path):
            id = generar_id()
            almacenar(id, usuario)
    else:
        #cuando el archivo aun no se ha generado
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nombre", "dni", "fecha_nacimiento", "edad", "clave", "alta"])
            id = generar_id()
            almacenar(id, usuario)

def generar_id():
    if not os.path.exists(csv_path):
        return "0000-00000000"
    ultimo_id = None
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row:
                ultimo_id = row[0]

    if ultimo_id is None:
        return "0000-00000000"
    prefijo_str, contador_str = ultimo_id.split("-")
    prefijo = int(prefijo_str)
    contador = int(contador_str)

    contador += 1
    if contador > 99999999:
        contador = 0
        prefijo += 1
        if prefijo > 9999:
            raise ValueError("Se superó el límite máximo de IDs disponibles.")

    nuevo_id = f"{str(prefijo).zfill(4)}-{str(contador).zfill(8)}"
    return nuevo_id        

def validar_dni(dni):
    if not all(n.isdigit() for n in dni):
        raise ValueError("El DNI debe contener solo dígitos.")
    if not os.path.exists(csv_path):
        return True
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and row[2] == dni:
                raise ValueError("El DNI ya existe en la base de datos.")

    return True

def validar_fecha(fecha_nacimiento):
    hoy = date.today()
    if not isinstance(fecha_nacimiento, date):
        raise ValueError("La fecha debe ser una fecha válida.")
    if fecha_nacimiento > hoy:
        raise ValueError("La fecha de nacimiento no puede ser mayor a la fecha actual.")
    if fecha_nacimiento == hoy:
        raise ValueError("La fecha de nacimiento no puede ser la fecha actual.")
    if hoy.year - fecha_nacimiento.year > 120:
        raise ValueError("La fecha indica una persona mayor a 120 años revise los datos.")
    return True

#2 Ver usuarios
def ver_usuarios():
    columnas_seguras = ["nombre", "dni", "fecha_nacimiento", "edad", "alta"]
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader =csv.DictReader(f)
            filas_filtradas = []
                    
            for row in reader:
                try:
                    #1 - claves faltantes
                    seleccion = {col: row[col] for col in columnas_seguras}
                    if seleccion["alta"] is None:
                        raise AttributeError
                    if seleccion["alta"].lower() == "true": #Solo muestra usuarios no dados de baja (== borrados)
                        filtrado = {"DNI": seleccion["dni"], 
                                    "Nombre": seleccion["nombre"],  
                                    "Fecha de Nacimiento": convertir_formato_fecha(seleccion["fecha_nacimiento"]), 
                                    "Edad": seleccion["edad"]}
                        filas_filtradas.append(filtrado)
                except KeyError:
                    print("Error: faltan columnas obligatorias en el archivo CSV.")
                    return
                except ValueError:
                    print("Error: formato de fecha inválido en uno de los usuarios.")
                    return
                except AttributeError:
                    print("Error: datos incompletos o corruptos en el campo 'alta'.")
                    return

    except FileNotFoundError:
        print("No existe la base de datos. Registre un usuario primero.")
        return

    if not filas_filtradas:
        print("No hay usuarios activos registrados.")
        return
        
    print(tabulate(filas_filtradas, headers="keys", tablefmt="fancy_grid"))

def convertir_formato_fecha(fecha):
    fecha_raw = datetime.strptime(fecha, "%Y-%m-%d")
    return fecha_raw.strftime("%d/%m/%Y")

#3 Ver datos
def ver_datos():
    intentos = 0
    while intentos < 3:
        try:
            dni = input("Ingrese el DNI buscado: ").strip()
            with open (csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                fila = next((r for r in reader if r["dni"] == dni), None)
        except FileNotFoundError:
            print("La base de datos no existe.")
            return
        
        if not fila:
            print("⛔ No se encontró el DNI ingresado. Intente nuevamente.\n")
            intentos += 1
            continue
        else:
            mostrar_datos(fila)
            break
    if intentos == 3:
        print("⛔ Tres intentos fallidos. Volviendo al menú...\n")
        return
       
def mostrar_datos(fila): #Con Tabulate
    tabla = [
        ["Nombre", fila["nombre"]],
        ["DNI", fila["dni"]],
        ["Fecha de nacimiento", fila["fecha_nacimiento"]],
        ["Edad", fila["edad"]],
        ["Contraseña", ocultar_clave(fila["clave"])]
    ]
    print("\n🔎 Datos del usuario:")
    print(tabulate(tabla, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
    print()

def ocultar_clave(clave: str) -> str:
    if not clave:
        return "******"
    return "*" * len(clave)

#4 Borrar usuario
def borrar_usuario():
    intentos = 0
    while intentos < 3:
        try:
            dni = input("Ingrese el Nombre del usuario buscado: ").strip()
            with open (csv_path, "r", encoding="utf-8") as archivo:
                reader = csv.DictReader(archivo)
                filas = list(reader)
                fila = next((f for f in filas if f["nombre"] == dni), None)
        except FileNotFoundError:
            print("La base de datos no existe.")
            return
        
        if not fila:
            print("⛔ No se encontró el Nombre ingresado. Intente nuevamente.\n")
            intentos += 1
            continue
        elif fila["alta"].lower() =="false":
            print("⛔ Usuario dado de baja")
            return
        else:
            editar_datos(filas, fila)
            return
    print("⛔ Tres intentos fallidos. Volviendo al menú...\n")
    
def editar_datos(filas, fila):
    for i, f, in enumerate(filas):
        if f["nombre"] == fila["nombre"]:
            filas[i]["alta"] = "False"
            break

    with open(csv_path, "w", encoding="utf-8", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=filas[0].keys())
        writer.writeheader()
        writer.writerows(filas)

    print("✔ Usuario dado de baja con exito.")

#5 Salir
def salir():
    print("ANSES agradece su visita.")
    exit()

#6 Menu general: carga de artículos, ver la lista de artículos y entrar al submenú de un artículo
def menu_principal():
    menu = Menu(titulo="ANSES",
    opciones={
            1: ("Registrarse", registrar_almacenar),
            2: ("Ver Usuarios", ver_usuarios),
            3: ("Ver Datos", ver_datos),
            4: ("Borrar Usuario", borrar_usuario),
            0: ("Salir", salir)
    }, salida=0)
    while True:
        menu.ejecutar_opcion()

if __name__ == "__main__":
    menu_principal()
