#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario su edad.
#Guardar la edad ingresada.
#Comparar si la edad es mayor o igual a 18.
#Si la edad es mayor o igual a 18, mostrar el mensaje: “Puedes ingresar a la discoteca”.
#En caso contrario, mostrar el mensaje: “No puedes ingresar, eres menor de edad”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese su edad:"
#LEER edad

#SI edad >= 18 ENTONCES
    #ESCRIBIR "Puedes ingresar a la discoteca"
#SINO
    #ESCRIBIR "No puedes ingresar, eres menor de edad"
#FIN SI
#FIN

edad = int(input("Ingrese su edad: ")) #pide la edad

if edad >= 18:
    print("Puedes ingresar a la discoteca") #verifica si tiene 18 o más
else:
    print("No puedes ingresar, eres menor de edad")