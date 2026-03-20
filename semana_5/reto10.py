#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario la nota numérica del estudiante.
#Guardar la nota ingresada.
#Comparar si la nota está entre 4.5 y 5.0.
#Si está en ese rango, asignar la letra “A” y el concepto “EXCELENTE”.
#Si no, comparar si la nota está entre 4.0 y 4.4.
#Si está en ese rango, asignar la letra “B” y el concepto “SOBRESALIENTE”.
#Si no, comparar si la nota está entre 3.5 y 3.9.
#Si está en ese rango, asignar la letra “C” y el concepto “BUENO”.
#Si no, comparar si la nota está entre 3.0 y 3.4.
#Si está en ese rango, asignar la letra “D” y el concepto “ACEPTABLE”.
#Si no, comparar si la nota está entre 0.0 y 2.9.
#Si está en ese rango, asignar la letra “E” y el concepto “REPROBADO”.
#En caso contrario, mostrar el mensaje: “Nota inválida”.
#Finalizar el programa si la nota es inválida.
#Mostrar la letra y el concepto asignados.
#Comparar si la nota es mayor o igual a 3.0.
#Si la nota es mayor o igual a 3.0, mostrar el mensaje: “Estado: Aprobado”.
#En caso contrario, mostrar el mensaje: “Estado: Reprobado”.
#Si está reprobado, comparar si la nota está entre 2.0 y 2.9.
#Si está en ese rango, mostrar el mensaje: “Puede presentar habilitación”.
#En caso contrario, mostrar el mensaje: “Sin derecho a habilitación”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese la nota numérica del estudiante:"
#LEER nota

#SI nota >= 4.5 Y nota <= 5.0 ENTONCES
    #letra <- "A"
    #concepto <- "EXCELENTE"
#SINO SI nota >= 4.0 Y nota <= 4.4 ENTONCES
    #letra <- "B"
    #concepto <- "SOBRESALIENTE"
#SINO SI nota >= 3.5 Y nota <= 3.9 ENTONCES
    #letra <- "C"
    #concepto <- "BUENO"
#SINO SI nota >= 3.0 Y nota <= 3.4 ENTONCES
    #letra <- "D"
    #concepto <- "ACEPTABLE"
#SINO SI nota >= 0.0 Y nota <= 2.9 ENTONCES
    #letra <- "E"
    #concepto <- "REPROBADO"
#SINO
    #ESCRIBIR "Nota inválida"
#FIN
#FIN SI

#ESCRIBIR "Letra:", letra, "-", concepto

#SI nota >= 3.0 ENTONCES
    #ESCRIBIR "Estado: Aprobado"
#SINO
    #ESCRIBIR "Estado: Reprobado"

    #SI nota >= 2.0 Y nota <= 2.9 ENTONCES
        #ESCRIBIR "Puede presentar habilitación"
    #SINO
        #ESCRIBIR "Sin derecho a habilitación"
    #FIN SI
#FIN SI
#FIN

nota = float(input("Ingrese la nota numérica del estudiante: "))

if 4.5 <= nota <= 5.0: #A: 4.5 a 5.0
    letra = "A"
    concepto = "EXCELENTE" 
elif 4.0 <= nota <= 4.4: #B: 4.0 a 4.4
    letra = "B"
    concepto = "SOBRESALIENTE"
elif 3.5 <= nota <= 3.9: #C: 3.5 a 3.9
    letra = "C"
    concepto = "BUENO"
elif 3.0 <= nota <= 3.4: #D: 3.0 a 3.4
    letra = "D"
    concepto = "ACEPTABLE"
elif 0.0 <= nota <= 2.9: #E: 0.0 a 2.9
    letra = "E"
    concepto = "REPROBADO"
else:
    print("Nota inválida")
    exit()

print("Letra:", letra, "-", concepto)

if nota >= 3.0: #Si la nota es 3.0 o más, aprueba
    print("Estado: Aprobado")
else:
    print("Estado: Reprobado")
    
    if 2.0 <= nota <= 2.9: #Si está entre 2.0 y 2.9, puede presentar habilitación
        print("Puede presentar habilitación")
    else: #Si es menor de 3.0, reprueba
        print("Sin derecho a habilitación")