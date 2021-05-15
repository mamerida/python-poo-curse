class Interfaz:

	def solicitar_un_numero_rel(self,titulo):
		variable = input(titulo)
		try:
			var= float(variable) #float real o int entero 
		except ValueError as error:
			print("El dato ingresado no es un numero") 
			var = 0 
		return var

	def solicitar_numero_entero(self,titulo):
		variable = input(titulo)
		try:
			var = int(variable)
		except ValueError as error:
			print("El dato ingresado no es un numero")
			var = 0 
		return var


