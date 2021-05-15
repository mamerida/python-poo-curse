class Matriz:
    def __init__(self):
        self.nombre = "Pepe"

    def generar_identidad(self,n):
        if n <= 0:
            return None
        matriz= [0] * n
        for f in range(len(matriz)):
            matriz[f] = [0]*n
        for f in range(len(matriz)):
            for c in range(len(matriz[f])):
                if f == c:
                    matriz[f][c] = 1
        return(matriz)

    def crear_tabla_multriplicar(self,n):
        if n <= 0:
            return []
        matriz = [0]*n
        for f in range(0,n):
            matriz[f] = [0]*n
        for f in range(len(matriz)):
            a = 1
            for c in range(len(matriz[f])):
               matriz[f][c] = a * (f+1)
               a +=1
        return matriz

                

            



if __name__ =="__main__":
    matriz1 = Matriz()
    print(matriz1.crear_tabla_multriplicar(4))
            
