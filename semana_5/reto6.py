#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario la temperatura en grados Celsius.
#Guardar la temperatura ingresada.
#Comparar si la temperatura es menor que 5.
#Si la temperatura es menor que 5, mostrar el mensaje: “MUY FRÍO: Usa ropa de invierno”.
#Si no, comparar si la temperatura está entre 5 y 14.
#Si está entre 5 y 14, mostrar el mensaje: “FRÍO: Usa chaqueta”.
#Si no, comparar si la temperatura está entre 15 y 24.
#Si está entre 15 y 24, mostrar el mensaje: “TEMPLADO: Ropa cómoda de diario”.
#Si no, comparar si la temperatura está entre 25 y 34.
#Si está entre 25 y 34, mostrar el mensaje: “CALIENTE: Usa ropa fresca”.
#En caso contrario, mostrar el mensaje: “MUY CALIENTE: Hidrátate bien”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese la temperatura en grados Celsius:"
#LEER temperatura

#SI temperatura < 5 ENTONCES
    #ESCRIBIR "MUY FRÍO: Usa ropa de invierno"
#SINO SI temperatura >= 5 Y temperatura <= 14 ENTONCES
    #ESCRIBIR "FRÍO: Usa chaqueta"
#SINO SI temperatura >= 15 Y temperatura <= 24 ENTONCES
    #ESCRIBIR "TEMPLADO: Ropa cómoda de diario"
#SINO SI temperatura >= 25 Y temperatura <= 34 ENTONCES
    #ESCRIBIR "CALIENTE: Usa ropa fresca"
#SINO
    #ESCRIBIR "MUY CALIENTE: Hidrátate bien"
#FIN SI
#FIN

temperatura = int(input("Ingrese la temperatura en grados Celsius: "))

if temperatura < 5: #Si la temperatura es menor que 5, es MUY FRÍO
    print("MUY FRÍO: Usa ropa de invierno")
elif 5 <= temperatura <= 14: #Si está entre 5 y 14, es FRÍO
    print("FRÍO: Usa chaqueta")
elif 15 <= temperatura <= 24: #Si está entre 15 y 24, es TEMPLADO
    print("TEMPLADO: Ropa cómoda de diario")
elif 25 <= temperatura <= 34: #Si está entre 25 y 34, es CALIENTE
    print("CALIENTE: Usa ropa fresca")
else: #Si es 35 o más, es MUY CALIENTE
    print("MUY CALIENTE: Hidrátate bien")