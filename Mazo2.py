from Carta import Carta
import random


class Mazo:
    def __init__(self):
        self.cartas = []
        self.crear_mazo()
    def crear_mazo(self):
        simbolos=["Trebol","Diamante","Pica","Corazones"]
        for j in range (0,4):
            for i in range(1,18):
                carta= Carta(i,simbolos[j])
                self.cartas.append(carta)
    def imprimir(self):
	    for instanciaCarta in self.cartas:
		    instanciaCarta.imprimir()
    def revolver(self):
        for celda in range(len(self.cartas)):
            aleatorio = random.randint(0,51)
            temporal = self.cartas[celda]
            self.cartas[celda]=self.cartas[aleatorio]
            self.cartas[aleatorio]=temporal




""" al utilizar arreglos no se necesita este metodo   

    def crear_mazo(self): constructor viejo
	    for  j in range(1,5):
		    for i in range(1,14):
			    carta = Carta(i , self.retornar_palo(j))
			    self.cartas.append(carta)
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
"""


mazo1 = Mazo()

mazo1.revolver()
mazo1.imprimir()