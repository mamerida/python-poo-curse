#debe contener las cartas
# tener la capacidad de pedir cartar
#Imprimir sus cartas
#Poder sumar el valor de las cartas
from Interfaz import Interfaz
from Mazo import Mazo

class Jugador:
    def __init__(self,nombre,cartas =[]):
        self.nombre = nombre
        self.cartas = cartas

    def asingar_cartas(self,cartas):
        self.cartas = cartas 

    def imprimir(self):
        print(self.nombre, " estas son sus cartas ")
        for carta in self.cartas:
            carta.imprimir()
        print("Suma: ", self.sumar_cartas())


    def sumar_cartas(self):
        suma = 0
        aces = 0
        for carta in self.cartas:
            valor = carta.obtener_numero()
            if (valor==1):
                aces+=1
            suma += valor
        if(aces > 0 and suma + 10 <=21):
            suma +=10
        
        return suma

    def jugar(self,mazo):
        interfaz = Interfaz() # pedir variable de tipo entero
        solicitar  = True
        titulo = "Digite: \n1 -Pedir Carta \n2- Quedarse \n Valor:"
        while(solicitar and self.sumar_cartas()<=21):
            self.imprimir()
            valor = interfaz.solicitar_numero_entero(titulo)
            if(valor == 1):
                self.cartas.append(mazo.obtener_siguiente_carta())
                self.cartas[-1].imprimir()
            elif(valor == 2):
                solicitar = False
        return self.sumar_cartas()

if __name__ == "__main__":
    mazo1 = Mazo()
    j1 = Jugador("Mario")
    j1.jugar(mazo1)

