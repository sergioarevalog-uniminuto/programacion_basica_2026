#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario una opción del menú.
#Guardar la opción ingresada.
#Comparar si la opción es igual a 1.
#Si la opción es 1, mostrar el mensaje: “Elegiste: Bandeja Paisa - $18.000”.
#Si no, comparar si la opción es igual a 2.
#Si la opción es 2, mostrar el mensaje: “Elegiste: Ajiaco - $15.000”.
#Si no, comparar si la opción es igual a 3.
#Si la opción es 3, mostrar el mensaje: “Elegiste: Sancocho - $12.000”.
#En caso contrario, mostrar el mensaje: “Opción no válida, intenta de nuevo”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese una opción del menú (1, 2 o 3):"
#LEER opcion

#SI opcion = 1 ENTONCES
    #ESCRIBIR "Elegiste: Bandeja Paisa - $18.000"
#SINO SI opcion = 2 ENTONCES
    #ESCRIBIR "Elegiste: Ajiaco - $15.000"
#SINO SI opcion = 3 ENTONCES
    #ESCRIBIR "Elegiste: Sancocho - $12.000"
#SINO
    #ESCRIBIR "Opción no válida, intenta de nuevo"
#FIN SI
#FIN

opcion = int(input("Ingrese una opción del menú (1, 2 o 3): "))

if opcion == 1: #Si el usuario ingresa 1, muestra Bandeja Paisa
    print("Elegiste: Bandeja Paisa - $18.000")
elif opcion == 2: #Si ingresa 2, muestra Ajiaco
    print("Elegiste: Ajiaco - $15.000")
elif opcion == 3: #Si ingresa 3, muestra Sancocho
    print("Elegiste: Sancocho - $12.000")
else: #Cualquier otro número muestra mensaje de error
    print("Opción no válida, intenta de nuevo")