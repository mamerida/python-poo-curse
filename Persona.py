class Persona:

	#para evitar error en tiempo de ejecucion mejor un constructor
	def __init__():
		self.nombre =""
		self.edad = 0 

	def bautizar(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad


	def saludar(self):
		print("Hola mi nombre es ",self.nombre," y mi edad es ",self.edad)

	def cumplir_años(self):
		self.edad += 1

p1 = Persona()

p1.bautizar("David", 24)

p1.cumplir_años()

p1.saludar()