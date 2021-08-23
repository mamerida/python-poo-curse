#!/usr/bin/env python 
#-*- coding: utf-8 -*-

def main():
    hilera="Hola Mundo"
    hilera2 = hilera.upper()
    print(hilera2)
    hilera3 = hilera2.lower()
    print(hilera3)
    print(hilera == hilera2) #false
    print(hilera.upper() == hilera2.upper())#true

    #para ubicar un caracter dentro de una hilera 
    pos=hilera.find("Hola") #retorna -1 si no llega a existir o la posicion inicial
    print(pos)

    #como obtener subhileras
    subhilera= hilera[0:4] #esto me trae las subhileras dentro de lo que paso como parametros y los guarda en subhileras
    print(subhilera)
    print(hilera[4::])#esto indica ir desde la posicion 4 hasta el final

    for letra in hilera:
        print(letra)
        
    #metodo split
    print(hilera.split(" "))#[Hola,mundo]
    print(hilera.split("la"))
    
    #separar y volver a unir
    arreglo = hilera.split(" ")#serpado el codigo
    print(arreglo)
    arreglo2 = ' '.join(arreglo) # lo vuelvo a unir 
    print(arreglo2)

#ejercicio 1 
def es_palindromo(palabra):
    palabra = palabra.lower()
    replacements= (("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u"))
    for a,b in replacements:
        palabra = palabra.replace(a,b)
    
    palabraReversa = ''.join(reversed(palabra))
    for i in range(0,len(palabra)):
        if palabra[i] != palabraReversa[i]:
            return False
            
#ejercicio 2



def encriptar(lista):
    replacements=(("a","1"),("e","2"),("i","3"),("o","4"),("u","5"),("A","6"),("E","7"),("I","8"),("O","9"),("U","0"))
    palabra = "-".join(lista) 
    for a,b in replacements:
        palabra = palabra.replace(a,b)
    if palabra == ['']:
        return []
    lista2 = palabra.split("-")
    if lista2 == ['']:
        return []
    return lista2

#ejercicio 3 
def desencriptar(lista):
    replacements=(("1","a"),("2","e"),("3","i"),("4","o"),("5","u"),("6","A"),("7","E"),("8","I"),("9","O"),("0","U"))
    palabra = "-".join(lista) 
    for a,b in replacements:
        palabra = palabra.replace(a,b)
    if palabra == ['']:
        return []
    lista2 = palabra.split("-")
    if lista2 == ['']:
        return []
    return lista2
 


if __name__=="__main__":
    main()
