'''
Crear las clases necesarias y los objetos para la siguiente lista 
de materiales de un bazar gastronímico:
'''
#########################BAZAR GASTRONOMICO
import math

class Pizzera():
    def __init__(self, codigo, alto, diametro, material):
        self.codigo = codigo
        self.alto = alto
        self.diametro = diametro
        self.material = material
    
    def __str__(self):
        return f"codigo: {self.codigo} \nalto: {self.alto} \ndiametro: {self.diametro} \nmaterial: {self.material}"

class Vaso():
    def __init__(self, codigo, alto, diametro, material):
        self.codigo = codigo
        self.alto = alto
        self.diametro = diametro
        self.material = material

    def calcular_capacidad(self):
        radio = self.diametro / 2
        return round(math.pi * radio**2 * self.alto, 2)
    
    def __str__(self):
        return f"codigo: {self.codigo} \ncapacidad: {self.calcular_capacidad()}cm3 \nmaterial: {self.material}"
    
class Olla():
    def __init__(self, codigo, alto, diametro, material):
        self.codigo = codigo
        self.alto = alto
        self.diametro = diametro
        self.material = material

    def calcular_capacidad(self):
        radio = self.diametro / 2
        return round(math.pi * radio**2 * self.alto, 2)
    
    def __str__(self):
        return f"codigo: {self.codigo} \ncapacidad: {self.calcular_capacidad()}cm3 \nmaterial: {self.material}"
    
##############CARGA OBJETOS
pizzera1 = Pizzera(1, 2, 30, "acero")
pizzera2 = Pizzera(2, 2, 32, "acero")
pizzera3 = Pizzera(3, 2, 34, "acero")
pizzera4 = Pizzera(4, 2.25, 36, "acero")
pizzera5 = Pizzera(5, 2.5, 38, "acero")

vaso1 = Vaso(1, 10, 5, "vidrio")
vaso2 = Vaso(2, 15, 5, "acero")
vaso3 = Vaso(3, 15, 4.5, "vidrio")
vaso4 = Vaso(4, 10, 4.5, "plástico")
vaso5 = Vaso(5, 10, 5, "vidrio")

olla1 = Olla(1, 20, 40, "acero")
olla2 = Olla(2, 5, 15, "aluminio")
olla3 = Olla(3, 15, 20, "barro")
olla4 = Olla(4, 10, 25, "cobre")
olla5 = Olla(5, 25, 35, "cerámica")

###############MUESTRA OBJETOS
print()
print(pizzera1)
print(vaso4)
print(olla2)