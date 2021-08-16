import random
class Buscaminas:
    def __init__(self, f , c):
        self.tablero = [None] * f #tablero logico
        self.tablero_usuario = [None] * f # tablero usuario 

        for i in range(f):
            self.tablero[i] = [0]*c
            self.tablero_usuario[i] = ["_"] *c
    
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


    def colocar_pieza(self , f , c , pierde = True ):
        filas = [0,0,-1,1,1,1,-1,-1] # esto va a servir para recorer el arreglo y poder moverme dentro del mismo
        cols =  [1,-1,0,0,1,-1,1,-1] # cada combinacion de fila y columna es un movimiento espefico
        if(f>=0 and len(self.tablero) and c >=0 and c< len(self.tablero[f])):

            if(self.tablero_usuario[f][c] =="_" and self.tablero[f][c]==0):
                #caso recursivo
                self.tablero_usuario[f][c] =str(self.tablero[f][c])
                contador = 0

                while(contador<8):
                    nueva_fila = f + filas[contador]
                    nueva_columna = c + cols[contador]
                    pierde = self.colocar_pieza(nueva_fila,nueva_columna,False)
                    contador += 1

            elif(self.tablero[f][c]>0):
                self.tablero_usuario[f][c] =str(self.tablero[f][c])
                pierde = False
            
            else:
                 self.tablero_usuario[f][c] =str(self.tablero[f][c])
            
        return pierde



        

    def __str__(self):
        contenido = ""
        for f in range(len(self.tablero)):
            for c in range(len(self.tablero[f])):
                if(self.tablero[f][c]== -1):
                     contenido +=("M\t")
                else:
                    contenido += str(self.tablero[f][c]) + "\t"
            contenido += "\n"
        


        contenido += " -- tablero usuario \n"
        for f in range(len(self.tablero_usuario)):
            for c in range(len(self.tablero_usuario[f])):
                    contenido += str(self.tablero_usuario[f][c]) + "\t"
            contenido += "\n"


    
        return contenido


            

if __name__ == "__main__":
    buscaminas = Buscaminas(5,6)
    print(buscaminas)
    buscaminas.colocarMinas(3)
    print(buscaminas)
    buscaminas.colocar_numeros()
    print(buscaminas)
    buscaminas.colocar_pieza(0,0)
    print(buscaminas)