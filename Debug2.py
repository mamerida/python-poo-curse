#como depurar normalmente
from icecream import ic
def sumar(x,y):
    ic()
    ic(x)
    ic(y)
    suma = x + y 
    return suma

ic.configureOutput(prefix="Prueba ", includeContext=True)
ic(sumar(3,4))


# para instalar paquetes en python uso icecream
#al terminar tengo que eliminar los debugs y la biblioteca