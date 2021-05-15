"""
numero = [0] * 10 
numero[4] = 9 
numero[-1] = 6

print(numero)
for i in range(0,len(numero)):
	numero[i] = (i+1)*2
"""
## SUBINDICES 

## lista = [x for x in range(0,10,2)] va a ir saltando de 2 en 2 

lista = [x for x in range(0,10)]

print(lista)

sublista = lista[:4] ##idem lista[0:4] 

print(sublista)

sublista2 = lista[2:5]

sublista3 = sublista2 + sublista

print(sublista3)

x = sublista3.index(3) ## indica el valor del indice 3 


