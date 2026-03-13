#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario el primer número.
#Guardar el primer número ingresado.
#Solicitar al usuario el segundo número.
#Guardar el segundo número ingresado.
#Calcular la suma de los dos números.
#Calcular la resta del primer número menos el segundo.
#Calcular la multiplicación de los dos números.
#Calcular la división del primer número entre el segundo.
#Calcular la división entera del primer número entre el segundo.
#Calcular el residuo de la división del primer número entre el segundo.
#Calcular la potencia del primer número elevado al segundo.
#Mostrar el resultado de la suma.
#Mostrar el resultado de la resta.
#Mostrar el resultado de la multiplicación.
#Mostrar el resultado de la división.
#Mostrar el resultado de la división entera.
#Mostrar el resultado del residuo.
#Mostrar el resultado de la potencia.
#Comparar si la suma de los dos números es mayor que 100.
#Mostrar el resultado de la comparación.
#Finalizar el programa.


#PSEUDOCODIGO

#INICIO
#ESCRIBIR "Ingrese el primer numero"
#LEER num1

#ESCRIBIR "Ingrese el segundo numero"
#LEER num2

#suma <- num1 + num2
#resta <- num1 - num2
#multiplicacion <- num1 * num2
#division <- num1 / num2
#division_entero <- num1 // num2
#residuo <- num1 % num2
#potencia <- num1 ** num2

#ESCRIBIR "La suma de los numeros es:", suma
#ESCRIBIR "La resta de los numeros es:", resta
#ESCRIBIR "La multiplicacion de los numeros es:", multiplicacion
#ESCRIBIR "La division de los numeros es:", division
#ESCRIBIR "La division entera de los numeros es:", division_entero
#ESCRIBIR "El residuo de los numeros es:", residuo
#ESCRIBIR "La potencia de los numeros es:", potencia
#ESCRIBIR "¿La suma de los numeros es mayor que 100?:", suma > 100
#FIN

num1=int(input("Ingrese el primer numero "))
num2=int(input("Ingrese el segundo numero "))

suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=num1/num2
division_entero=num1//num2
residuo=num1%num2
potencia=num1**num2

print("La suma de los numeros es:",suma)
print("La resta de los numeros es:",resta)
print("La multiplicación de los numeros es:",multiplicacion)
print("La division de los numeros es:",division)
print("La division entera de los numeros es:",division_entero)
print("El residuo de los numeros es:",residuo)
print("La potencia de los numeros es:",potencia)
print("¿La suma de los numeros es mayor que 100?:",suma>100)











