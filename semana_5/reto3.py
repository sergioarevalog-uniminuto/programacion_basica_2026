#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario la nota final del estudiante.
#Guardar la nota ingresada.
#Comparar si la nota es mayor o igual a 3.0.
#Si la nota es mayor o igual a 3.0, mostrar el mensaje: “APROBASTE la materia. ¡Felicitaciones!”.
#En caso contrario, mostrar el mensaje: “REPROBASTE la materia. Debes presentar recuperación!”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese la nota final del estudiante:"
#LEER nota

#SI nota >= 3.0 ENTONCES
    #ESCRIBIR "APROBASTE la materia. ¡Felicitaciones!"
#SINO
    #ESCRIBIR "REPROBASTE la materia. Debes presentar recuperación!."
#FIN SI
#FIN

nota = float(input("Ingrese la nota final del estudiante: "))

if nota >= 3.0: #verifica si la nota es 3.0 o mayor
    print("APROBASTE la materia. ¡Felicitaciones!")
else: #se ejecuta cuando la nota es menor de 3.0
    print("REPROBASTE la materia. Debes presentar recuperación!.")