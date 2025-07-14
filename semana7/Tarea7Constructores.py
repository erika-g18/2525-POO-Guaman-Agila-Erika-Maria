#ejemplo de constructor
#"Consideremos una clase Persona Y mascota  con un constructor definido.
# La creación de un objeto Persona y mascota se vería así en Python:"

class Persona:
    def __init__(self, nombre, apellido,edad, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion
class Mascota:
    def __init__(self, animal, nombre, edad):
        self.animal = animal
        self.nombre = nombre
        self.edad = edad

#
Persona =Persona("Carmen","Lopez",28,"profesora")
Mascota=Mascota("perro","luli",5)

print("hola soy:",Persona.nombre,Persona.apellido,"tengo",Persona.edad,"años mi profesion es:", Persona.profesion)
print("mi mascota es un",Mascota.animal,"se llama",Mascota.nombre,"su edad es de",Mascota.edad,"años")