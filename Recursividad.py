def calcular_sumatoria(numero):
    resultado=0
    if(numero>0):
        resultado= numero + calcular_sumatoria(numero-1)
    
    return resultado

def calcular_factorial(n):
    if n<0:
        return None
    resultado=1
    if n>1:
        resultado = n*calcular_factorial(n-1)
        return resultado
    elif n == 1:
        return resultado
    else:
        return 0



def main():
    print(calcular_sumatoria(-5)) 
    print(calcular_factorial(5)) 
    print(calcular_factorial(10)) 


if __name__ =='__main__':
    main();