def suma(number):
    numero = + 10
def metodoTipoNoPrimitivo(lista):
    #se modifica para que no modifique la lista originarl
    #metodos bibliotecas listas python
    listaCopia = [0] * len(lista) #[0,0,0]
    for i in range(0,len(lista)):
        listaCopia[i] = lista[i]
        
        listaCopia[0]+=10
        return listaCopia

if __name__ == "__main__":
    x = 20
    suma(x)
    print(x)
    
    y = [0,0,0]
    lista = metodoTipoNoPrimitivo(y)
    print(y)
    print(lista)