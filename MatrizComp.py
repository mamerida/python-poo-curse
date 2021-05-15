def imprimir(matriz):
    contenido = ""
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            contenido += str(matriz[f][c]) + "\t"
        contenido += "\n"
    print(contenido)

matriz1 = [None] * 10 # creo una matriz con 10 elementos 

for celda in range(len(matriz1)):
    matriz1[celda] = [0]*5 #aca a cada fila le agrego 5 columnas



#acceder a elementos matriz
#cambiar elementos aislados
matriz1[0][0] = 6
matriz1[1][2] = 15

#imprimir(matriz1)
#acceder elementos y asingarnos 

celda1 = matriz1[0][0] #va a dar 6
#print(celda1)
lista0 = matriz1[0]#me devuelve una lista 

#print(lista0)


########## matriz de numeros primos######

matriz2 = [0] * 10

for i in range(len(matriz2)):
    matriz2[i] = [0] * 5
n = 1 
for f in range(len(matriz2)):
    for c in range(len(matriz2[f])):
        matriz2[f][c] = n
        n += 2 

##imprimir(matriz2)

### matriz rango y append

matriz3 = [0] * 10 
n = 1
for f in range(len(matriz3)): # creo un arreglo para recorrer las 10 filas
    matriz3[f] = [] # genero en cada fila una lista vacia
    for c in range(5): # genero un for para que a cada lista le agrege 5 elemenos n
        matriz3[f].append(n)
        n += 1

imprimir(matriz3)