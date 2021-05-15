import pdb
print("Inicio de ejecucion")

pdb.set_trace() 
base = 2 
for i in range(1,11):
    multrip = 2 * i
    print( base," x ",i," = ", multrip)
print("fin de la ejecucion")

#hacer un debug del programa
#list dentro del PDB para poder ver el flujo
#continue para seguir la ejecucion
#next ejecuta la linea en pantalla y pasa a la siguiente
#step para ingresar a un metodo y ejecutar linea por linea
#si ejecuutamos con next hace el for completo
#list 5 , 7 imprime desde la linea 5 a la 7
#jump para saltar a una linea especifica
#pp <variable> permite mostrar el valor
#disable para deshabilitar los break point
#exit() para terminar un programa
