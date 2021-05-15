class Carta:


	'''Viejo constructor
	def __init__(self):
		self.palo = "Espadas"
		self.numero = 8
	'''
# nuevo constructor 
	def __init__(self, palo , number):
		self.palo = palo
		self.numero = number


	def imprimir(self):
		print("Este es su palo ",self.palo," este es su numero ",self.numero)


'''
# Defina aquí su clase Automovil
class Automovil:
# Recuerde programar el constructor de clase que inicializa los 3 atributos
    def __init__(self,velocidad_actual,marca,estado):
    	self.velocidad_actual = velocidad_actual
    	self.marca= marca
    	self.estado= estado
        
# Adicionalmente agregue los 4 métodos que se encargan de modificar la velocidad y el estado
	def aumentar_velocidad(self):
		self.velocidad_actual += 10
	def reducir_velocidad (self):
		self.velocidad_actual -=6
	def encender(self):
		self.estado = True
	def apagar(self):
		self.estado = False 

# No es necesario que cree instancias o pruebas ya que el código se evalúa automáticamente
'''
#Ejéemplos con strings
#Mezcla de caracteres
print("Hoy es %d de %s del anioo %d " %(7 , "diciembre" , 2020 )) # %d se utiliza para representar un numero %s un caracter 


# para evitar el salto de linea

print("hola mundo" ,end=" ")
print("Esta linea sale la lado de la anterior ")