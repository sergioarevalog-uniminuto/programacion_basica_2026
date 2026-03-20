#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario la longitud del lado A.
#Guardar la longitud del lado A.
#Solicitar al usuario la longitud del lado B.
#Guardar la longitud del lado B.
#Solicitar al usuario la longitud del lado C.
#Guardar la longitud del lado C.
#Verificar si las tres longitudes pueden formar un triángulo.
#Para ello, comprobar que la suma del lado A y el lado B sea mayor que el lado C.
#Comprobar que la suma del lado A y el lado C sea mayor que el lado B.
#Comprobar que la suma del lado B y el lado C sea mayor que el lado A.
#Si las tres condiciones se cumplen, entonces sí forman un triángulo.
#Comparar si los tres lados son iguales.
#Si los tres lados son iguales, mostrar el mensaje: “Triángulo EQUILÁTERO”.
#Si no, comparar si dos lados son iguales.
#Si dos lados son iguales, mostrar el mensaje: “Triángulo ISÓSCELES”.
#En caso contrario, mostrar el mensaje: “Triángulo ESCALENO”.
#Si no se cumplen las condiciones para formar triángulo, mostrar el mensaje: “NO forman un triángulo”.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese la longitud del lado A:"
#LEER lado_a

#ESCRIBIR "Ingrese la longitud del lado B:"
#LEER lado_b

#ESCRIBIR "Ingrese la longitud del lado C:"
#LEER lado_c

#SI (lado_a + lado_b > lado_c) Y (lado_a + lado_c > lado_b) Y (lado_b + lado_c > lado_a) ENTONCES
    #SI lado_a = lado_b Y lado_b = lado_c ENTONCES
        #ESCRIBIR "Triángulo EQUILÁTERO"
    #SINO SI lado_a = lado_b O lado_a = lado_c O lado_b = lado_c ENTONCES
        #ESCRIBIR "Triángulo ISÓSCELES"
    #SINO
        #ESCRIBIR "Triángulo ESCALENO"
    #FIN SI
#SINO
    #ESCRIBIR "NO forman un triángulo"
#FIN SI
#FIN

lado_a = float(input("Ingrese la longitud del lado A: "))
lado_b = float(input("Ingrese la longitud del lado B: "))
lado_c = float(input("Ingrese la longitud del lado C: "))

if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a): #Si esas 3 condiciones se cumplen, sí existe triángulo
    if lado_a == lado_b == lado_c: #Equilátero: los 3 lados son iguales.
        print("Triángulo EQUILÁTERO")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c: #Isósceles: exactamente 2 lados son iguales.
        print("Triángulo ISÓSCELES")
    else: #Escaleno: todos los lados son diferentes.
        print("Triángulo ESCALENO")
else:
    print("NO forman un triángulo")