'''POO, excepciones, modulos, paquetes, librerías, BD'''
'''los objetos tienen atributos y métodos'''
class Plato:
    #constructor
    def __init__(self, material, color, diametro, altura, precio):
        self.material = material
        self.color = color
        self.diametro = diametro
        self.altura = altura
        self.precio = precio

    #métodos
    def calcular_volumen(self):
        vol = self.altura * self.diametro
        return vol
    
    def mostrar_material_color(self):
        return f"El material es {self.material} y el color es {self.color}"

    def mostrar_precio(self):
        return f"${self.precio}"
    
    def __str__(self):
        return f"Plato de {self.material}, color {self.color}, ${self.precio}"

######
plato1= Plato("cerámica", "blanco", 24, 2.25, 2568.36)
plato2= Plato("plastiloza", "amarillo", 24, 1.75, 3528.87)
plato3= Plato("silicona", "verde", 24, 1.25, 5684.95)
plato4= Plato("vidrio templado", "gris", 25, 3.15, 1568.75)
plato5= Plato("madera", "rojo", 21, 2.54, 1248.25)

########
print()
print(plato1)
print(plato2.mostrar_material_color())
print(plato3.mostrar_precio())
