import random
class Buscaminas:
    def __init__(self, f , c):
        self.tablero = [None] * f #tablero logico
        self.tablero_usuario = [None] * f # tablero usuario 

        for i in range(f):
            self.tablero[i] = [0]*c
            self.tablero_usuario[i] = [0] *c
    
    def colocarMinas(self, minas):
        while(minas >0):
            fila = random.randint(0,len(self.tablero)-1)
            columna = random.randint(0,len(self.tablero[fila]) -1 ) # pregunta dentro de la fila donde me encuentro la cantida de elementos
            if(self.tablero[fila][columna] == 0):
                self.tablero[fila][columna] = -1
                minas -= 1 
    
    def colocar_numeros(self):
        filas = [0,0,-1,1,1,1,-1,-1] # esto va a servir para recorer el arreglo y poder moverme dentro del mismo
        cols =  [1,-1,0,0,1,-1,1,-1] # cada combinacion de fila y columna es un movimiento espefico

        for f in range(len(self.tablero)):
            for c in range(len(self.tablero[f])):
                if(self.tablero[f][c] == -1):
                    contador = 0
                    while(contador <8): # se le coloca menor a 8 para contar los 8 movimientos 
                        nueva_fila = f + filas[contador]
                        nueva_columna = c + cols[contador]
                        if (nueva_fila >=0 and nueva_fila < len(self.tablero) and nueva_columna >=0 
                            and nueva_columna < len(self.tablero[nueva_fila]) and self.tablero[nueva_fila][nueva_columna] != -1):
                                self.tablero[nueva_fila][nueva_columna] +=1
                        contador +=1





        

    def __str__(self):
        contenido = ""
        for f in range(len(self.tablero)):
            for c in range(len(self.tablero[f])):
                if(self.tablero[f][c]== -1):
                     contenido +=("M\t")
                else:
                    contenido += str(self.tablero[f][c]) + "\t"
            contenido += "\n"
        return contenido
            

if __name__ == "__main__":
    buscaminas = Buscaminas(5,6)
    print(buscaminas)
    buscaminas.colocarMinas(10)
    print(buscaminas)
    buscaminas.colocar_numeros()
    print(buscaminas)