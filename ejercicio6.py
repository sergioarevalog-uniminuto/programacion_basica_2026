#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario su nombre completo.
#Guardar el nombre ingresado.
#Solicitar al usuario su peso en kilogramos.
#Guardar el peso ingresado.
#Solicitar al usuario su altura en metros.
#Guardar la altura ingresada.
#Calcular el índice de masa corporal dividiendo el peso entre la altura multiplicada por sí misma.
#Comparar si el IMC está en el rango normal, es decir, si es mayor o igual a 18.5 y menor o igual a 24.9.
#Mostrar el nombre del usuario.
#Mostrar el peso en kilogramos.
#Mostrar la altura en metros.
#Mostrar el valor del IMC.
#Mostrar si el IMC está en rango normal.
#Finalizar el programa.


#PSEUDOCODIGO

#INICIO
#ESCRIBIR "Ingrese su nombre completo:"
#LEER nombre

#ESCRIBIR "Ingrese su peso en kilogramos:"
#LEER peso

#ESCRIBIR "Ingrese su altura en metros:"
#LEER altura

#imc <- peso / (altura * altura)
#rango_normal <- imc >= 18.5 Y imc <= 24.9

#ESCRIBIR "Nombre:", nombre
#ESCRIBIR "Peso:", peso, "kg"
#ESCRIBIR "Altura:", altura, "m"
#ESCRIBIR "IMC:", imc
#ESCRIBIR "¿IMC en rango normal (18.5 - 24.9)?:", rango_normal
#FIN

nombre=input("Ingrese su nombre completo: ")
peso=int(input("Ingrese su peso en kilogramos: "))
altura=float(input("Ingrese su altura en metros: "))

imc=peso/(altura*altura)

rango_normal=imc>=18.5 and imc<=24.9

print("\nNombre :", nombre)
print("Peso :", peso, "kg")
print("Altura :", altura, "m")
print("IMC :", round(imc, 2))
print("¿IMC en rango normal (18.5 - 24.9)?:", rango_normal)