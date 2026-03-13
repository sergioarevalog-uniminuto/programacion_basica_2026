#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario su nombre y apellido.
#Guardar el nombre ingresado.
#Solicitar al usuario su edad.
#Guardar la edad ingresada.
#Solicitar al usuario su ciudad de residencia.
#Guardar la ciudad ingresada.
#Mostrar en pantalla el mensaje: “Hola, soy” junto con el nombre.
#Mostrar en pantalla el mensaje: “Tengo” junto con la edad y la palabra “años”.
#Mostrar en pantalla el mensaje: “Vivo en” junto con la ciudad.
#Comparar si la edad es mayor que 18.
#Mostrar en pantalla el resultado de la comparación para indicar si es mayor de edad.
#Finalizar el programa.


#PSEUDOCODIGO

#INICIO
#LEER nombre
#LEER edad
#LEER ciudad
#ESCRIBIR "Hola, soy ", nombre
#ESCRIBIR "Tengo ", edad, " años"
#ESCRIBIR "Vivo en ", ciudad
#ESCRIBIR "¿Es mayor de edad?", edad > 18
#FIN

nombre=input("Ingrese su nombre y aprellido ")
edad=int(input("Ingrese su edad "))
ciudad=input("Ingrese su ciudad de residencia ")

print("Hola, soy",nombre)
print("Tengo",edad,"años")
print("Vivo en",ciudad)
print("¿Es mayor de edad?", edad > 18)
