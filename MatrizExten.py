def imprimir(lista):
    for f in range(len(matriz)):
        linea =""
        for c in range(len(matriz[f])):#itero por el largo de cada lista dentro de matriz
            linea += str(matriz[f][c]) + " "
        
        print(linea)    
        


if __name__ == "__main__":
    #por extencion
    matriz=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    imprimir(matriz)

