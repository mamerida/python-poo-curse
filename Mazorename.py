from Carta import Carta

""""
class Mazo:

	def __init__(self):
		self.carta1 = Carta("pica",7)
		self.carta2= Carta("Diam",8)

	def imprimir(self):
		self.carta1.imprimir()
		self.carta2.imprimir()
	def crear_mazo(self):
"""
class Mazo:
	def __init__(self):
		self.cartas = []
		self.crear_mazo()

	def crear_mazo(self):
		for  j in range(1,5):
			for i in range(1,14):
				carta = Carta(i , self.retornar_palo(j))
				self.cartas.append(carta)

	def imprimir(self):
		for instanciaCarta in self.cartas:
			instanciaCarta.imprimir()

	def retornar_palo(self, i):
		palo = " "
		if (i == 1):
			palo = "Trebol"
		elif (i == 2):
			palo = "Pica"
		elif (i == 3):
			palo = "Corazon"
		elif (i == 4):
			palo = "Diamantes"
		return palo





mazo1 = Mazo()

mazo1.imprimir()