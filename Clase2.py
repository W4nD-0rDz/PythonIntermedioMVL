#Superclase
class Animal():
#Métodos
##Métodos generales
###Constructor
    def __init__(self, patas, nombre, edad):
        self.patas = patas
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("Está comiendo")

    def hablar(self):
        return f"Shhhh..."

    def __str__(self):
        return f"Mi mascota se llama {self.nombre} y tiene {self.edad} años"

#Instancias de la superclase
"""gato1 = Animal(4, "Felix", "Persa", 3)
perro1 = Animal(4, "Firulay", "Chihuahua", 2)

print(gato1.mostrar())
print(gato1.hablar())
print(perro1.mostrar())
print(perro1.hablar())"""

#Subclases
class Gato(Animal):
    def __init__(self, patas, nombre, raza, edad):
        super().__init__(patas, nombre, edad)
        self.raza = raza

    def hablar(self):
        base = super().hablar()
        return f"{base}\n{self.nombre} está por decir algo...\n Hola, soy un gato de raza {self.raza}, me llamo {self.nombre} y digo miau"

class Perro(Animal):
    def __init__(self, patas, nombre, raza, edad):
        super().__init__(patas, nombre, edad)
        self.raza = raza

    def hablar(self):
        base = super().hablar()
        return f"{base}\n{self.nombre} está por decir algo...\n Hola, soy un perro de raza {self.raza}, me llamo {self.nombre} y digo guau guau"
    
class Gallina(Animal):
    def __init__(self, patas, nombre, raza, edad):
        super().__init__(patas, nombre, edad)
        self.raza = raza

    def hablar(self):
        base = super().hablar()
        return f"{base}\n{self.nombre} está por decir algo...\n Hola, soy una gallinita de raza {self.raza}, me llamo {self.nombre} y digo coco coco"   

#Crear instancias:
gato2 = Gato(4, "Felix", "Persa", 3)
perro2 = Perro(4, "Firulay", "Chihuahua", 2)
gallina2 = Gallina(2, "Margarita", "Sussex", 1)

print(gato2.mostrar())
print(gato2.hablar())
print("")
print(perro2.mostrar())
print(perro2.hablar())
print("")
print(gallina2.mostrar())
print(gallina2.hablar())