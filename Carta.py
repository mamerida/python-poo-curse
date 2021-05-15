class Carta:

	def __init__(self, numero, palo ):
		self.palo = palo
		self.numero = numero


	def convertir_numero_a_letra(self):
		valor=""
		if (self.numero == 11):
			valor ="J"
		elif (self.numero == 12):
			valor ="Q"
		elif (self.numero == 13):
			valor ="K"
		elif (self.numero == 1):
			valor = "As"
		else:
			valor = str(self.numero)
		return valor 

	def imprimir(self):
		numero = self.convertir_numero_a_letra()
		print(numero ," de ",self.palo)

	def obtener_numero(self):
		return 10 if self.numero > 10 else self.numero	

