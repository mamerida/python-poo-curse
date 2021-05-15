def multiplicar_celdas(lista):
    if len(lista)==0:
        return 0
    variable = 1
    for i in range(0,len(lista)):
        variable = variable * lista[i] 

    return variable

def formar_numero(lista):
    coso = []
    variable = ""
    if len(lista)==0:
        return 0
    for i in range(0,len(lista)):
        coso.append(str(abs(lista[i])))
        variable = variable + coso[i]
    variable = int(variable)
    print(variable)
    return variable

formar_numero([1,-2,3])