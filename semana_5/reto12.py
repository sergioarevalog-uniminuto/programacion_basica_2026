#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario un año.
#Guardar el año ingresado.
#Calcular si el año es divisible entre 4.
#Calcular si el año no es divisible entre 100.
#Calcular si el año es divisible entre 400.
#Verificar si se cumple alguna de estas condiciones:
#el año es divisible entre 4 y no es divisible entre 100
    #o el año es divisible entre 400
    #Si alguna condición se cumple, mostrar el mensaje: “El año ES bisiesto”.
#En caso contrario, mostrar el mensaje: “El año NO es bisiesto”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese un año:"
#LEER año

#SI (año % 4 = 0 Y año % 100 <> 0) O (año % 400 = 0) ENTONCES
    #ESCRIBIR "El año ", año, " ES bisiesto"
#SINO
    #ESCRIBIR "El año ", año, " NO es bisiesto"
#FIN SI
#FIN




#Un año es bisiesto si cumple una de estas condiciones:
#es divisible entre 4 y no es divisible entre 100 o es divisible entre 400

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año", año, "ES bisiesto")
else:
    print("El año", año, "NO es bisiesto")