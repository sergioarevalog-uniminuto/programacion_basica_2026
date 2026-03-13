#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario la temperatura en grados Celsius.
#Guardar la temperatura ingresada.
#Calcular la temperatura en grados Fahrenheit.
#Calcular la temperatura en Kelvin.
#Mostrar la temperatura en grados Celsius.
#Mostrar la temperatura en grados Fahrenheit.
#Mostrar la temperatura en Kelvin.
#Comparar si la temperatura en Celsius supera los 37 grados.
#Mostrar el resultado de la comparación.
#Finalizar el programa.


#PSEUDOCODIGO

#INICIO
#ESCRIBIR "Ingrese la temperatura en ° Celsius"
#LEER temp

#fa <- (temp * 9 / 5) + 32
#ke <- temp + 273.15

#ESCRIBIR "Temperatura en ° Celsius:", temp
#ESCRIBIR "Temperatura en ° Fahrenheit:", fa
#ESCRIBIR "Temperatura en ° Kelvin:", ke
#ESCRIBIR "¿Supera la temperatura de fiebre (37°C)?", temp > 37
#FIN

temp=int(input("Ingrese la temperatura en ° Celsius "))

fa=(temp * 9/5) + 32
ke=temp + 273.15

print("Temperatura en ° Celsius:",temp)
print("Temperatura en ° Fahrenheit:",fa)
print("Temperatura en ° Kelvin:",ke)
print("¿Supera la temperatura de fiebre (37°C)?",temp>37)