class Persona:
	def __init__(self, nombre ="",edad =0):
		self.nombre = nombre
		self.edad = edad

	def saludar(self):
		print("Hola mi nombre es ",self.nombre," y tengo una edad de ",self.edad)

	def cumplir_años(self):
		self.edad +=1



p1 = Persona("Karol", 15)

p2 = Persona("Maria", 24)

p1.saludar()

p1.cumplir_años()

p1.saludar()




