#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario su peso en kilogramos.
#Guardar el peso ingresado.
#Solicitar al usuario su altura en metros.
#Guardar la altura ingresada.
#Calcular el índice de masa corporal dividiendo el peso entre la altura elevada al cuadrado.
#Comparar si el IMC es menor que 18.5.
#Si el IMC es menor que 18.5, asignar la categoría “Bajo peso”.
#Si no, comparar si el IMC es menor o igual a 24.9.
#Si el IMC es menor o igual a 24.9, asignar la categoría “Normal”.
#Si no, comparar si el IMC es menor o igual a 29.9.
#Si el IMC es menor o igual a 29.9, asignar la categoría “Sobrepeso”.
#En caso contrario, asignar la categoría “Obesidad”.
#Mostrar el valor del IMC.
#Mostrar la categoría correspondiente.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese su peso en kilogramos:"
#LEER peso

#ESCRIBIR "Ingrese su altura en metros:"
#LEER altura

#imc <- peso / (altura ^ 2)

#SI imc < 18.5 ENTONCES
    #categoria <- "Bajo peso"
#SINO SI imc <= 24.9 ENTONCES
    #categoria <- "Normal"
#SINO SI imc <= 29.9 ENTONCES
    #categoria <- "Sobrepeso"
#SINO
    #categoria <- "Obesidad"
#FIN SI

#ESCRIBIR "IMC:", imc
#ESCRIBIR "Categoría:", categoria
#FIN

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2) #La fórmula del IMC es:peso / (altura ** 2)

if imc < 18.5: #menor de 18.5 → Bajo peso
    categoria = "Bajo peso"
elif imc <= 24.9: #de 18.5 a 24.9 → Normal
    categoria = "Normal"
elif imc <= 29.9: #de 25 a 29.9 → Sobrepeso
    categoria = "Sobrepeso"
else: #30 o más → Obesidad
    categoria = "Obesidad"

print("IMC:", round(imc, 2))
print("Categoría:", categoria)