#Menu reutilizable

class Menu():
    def __init__(self,titulo, opciones=None, salida=None):
        self.titulo = titulo
        self.opciones = opciones or {}
        self.salida = salida

    def mostrar(self):
        while True:
            print(f"\n=== {self.titulo} ===")

            #Ordena las opciones
            claves_ordenadas = sorted(self.opciones.keys())
            #Remueve la salida (0) y la agrega al final
            if self.salida in claves_ordenadas:
                claves_ordenadas.remove(self.salida)
                claves_ordenadas.append(self.salida)
            #Muestra las opciones ordenadas
            for clave in claves_ordenadas:
                texto, _ = self.opciones[clave]
                print(f"{clave} - {texto} ")

           #Pide al usuario la opción
            entrada = input("Opción:...").strip()
            if not entrada.isdigit():
                print("❌ Opcion incorrecta. Intente nuevamente.")
                continue #vuelve a mostrar el menu

            clave = int(entrada)
            if clave == self.salida:
                print("Saliendo del menú...")
                break
            elif clave in self.opciones:
                funcion = self.opciones[clave][1]
                if callable(funcion):
                    funcion()
            else:
                print("❌ Opción no encontrada. Intente nuevamente.")