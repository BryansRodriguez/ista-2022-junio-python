"""
-
Creen una clase para una persona con un método que imprima sus nombres y apellidos
-
Creen una lista de personas
-
Creen un ciclo for que llame el método para imprimir los nombres y apellido s

En replit.com
https://replit.com/join/hqlmgjqgpr-danoc93

"""

class Persona:
  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    
  def imprimir_nombres(self):
    print(f"La persona tiene nombre {self.nombre} {self.apellido}")

  def es_mayor_a(self, otra_persona):
    es_mayor = self.edad > otra_persona.edad
    print(f"Es mayor? {es_mayor}")
    return es_mayor

persona1 = Persona("Daniel", "Ortiz", 2)
persona2 = Persona("Juan", "Correa", 5)

lista_personas = [persona1, persona2]

lista_personas2 = []
lista_personas2.append(persona1)
lista_personas2.append(persona2)

print(lista_personas)
print(lista_personas2)

for persona in lista_personas:
  persona.imprimir_nombres()

variable = persona1.es_mayor_a(persona2)