#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario un número entero
#Guardar el número ingresado.
#Comparar si el número es mayor que 0.
#Si el número es mayor que 0, mostrar el mensaje: “El número es POSITIVO”.
#Si no, comparar si el número es menor que 0.
#Si el número es menor que 0, mostrar el mensaje: “El número es NEGATIVO”.
#En caso contrario, mostrar el mensaje: “El número es CERO”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese un número entero:"
#LEER numero

#SI numero > 0 ENTONCES
    #ESCRIBIR "El número es POSITIVO"
#SINO SI numero < 0 ENTONCES
    #ESCRIBIR "El número es NEGATIVO"
#SINO
    #ESCRIBIR "El número es CERO"
#FIN SI
#FIN

numero = int(input("Ingrese un número entero: "))

if numero > 0: #verifica si el número es mayor que 0
    print("El número es POSITIVO")
elif numero < 0: #verifica si es menor que 0
    print("El número es NEGATIVO")
else: #se ejecuta cuando no es mayor ni menor, o sea que es 0
    print("El número es CERO")