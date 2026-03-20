#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario un número entero.
#Guardar el número ingresado.
#Calcular el residuo de dividir el número entre 2.
#Comparar si el residuo es igual a 0.
#Si el residuo es igual a 0, mostrar el mensaje: “El número es PAR”.
#En caso contrario, mostrar el mensaje: “El número es IMPAR”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese un número entero:"
#LEER numero

#SI numero % 2 = 0 ENTONCES
    #ESCRIBIR "El número ", numero, " es PAR"
#SINO
    #ESCRIBIR "El número ", numero, " es IMPAR"
#FIN SI
#FIN

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0: #Si el residuo es 0, el número es par
    print("El número", numero, "es PAR")
else: #Si no es 0, el número es impar
    print("El número", numero, "es IMPAR")