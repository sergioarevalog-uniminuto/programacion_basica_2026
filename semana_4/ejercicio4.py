#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario la nota número 1.
#Guardar la nota número 1.
#Solicitar al usuario la nota número 2.
#Guardar la nota número 2.
#Solicitar al usuario la nota número 3.
#Guardar la nota número 3.
#Calcular el promedio de las tres notas.
#Mostrar la nota número 1.
#Mostrar la nota número 2.
#Mostrar la nota número 3.
#Mostrar el promedio de las tres notas.
#Comparar si el promedio es mayor que 3.0.
#Mostrar el resultado de la comparación.
#Finalizar el programa.


#PSEUDOCODIGO

#INICIO
#ESCRIBIR "Ingrese la nota numero 1 (entre 0.0 y 5.0)"
#LEER nota1

#ESCRIBIR "Ingrese la nota numero 2 (entre 0.0 y 5.0)"
#LEER nota2

#ESCRIBIR "Ingrese la nota numero 3 (entre 0.0 y 5.0)"
#LEER nota3

#promedio <- (nota1 + nota2 + nota3) / 3

#ESCRIBIR "Nota 1:", nota1
#ESCRIBIR "Nota 2:", nota2
#ESCRIBIR "Nota 3:", nota3
#ESCRIBIR "El promedio de las 3 notas es:", promedio
#ESCRIBIR "¿El estudiante aprobo (nota minima 3.0)?", promedio > 3.0
#FIN

nota1=float(input("Ingrese la nota numero 1 (entre 0.0 y 5.0) "))
nota2=float(input("Ingrese la nota numero 2 (entre 0.0 y 5.0) "))
nota3=float(input("Ingrese la nota numero 3 (entre 0.0 y 5.0) "))

promedio=(nota1+nota2+nota3)/3

print("Nota 1:",nota1)
print("Nota 2:",nota2)
print("Nota 3:",nota3)
print("El promedio de las 3 notas es:",promedio)
print("¿El estudiante aprobo (nota minima 3.0)? ",promedio>3.0)