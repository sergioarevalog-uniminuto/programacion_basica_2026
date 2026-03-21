#Parcial ejercicio 1 consumo agua

#ALGORITMO
#Iniciar el programa
#Solicitar al usuario el nombre
#Guardar el nombre
#Solicitar al usuario el consumo en metros cubicos (numero entero)
#Guardar el consumo
#Comparar el consumo si es mayor o igual a 1 y SI es menor o igual  a 15
#Si el consumo esta entre 1 y 15 muestra el nombre, la categoria: Bajo consumo y el mensaje :¡Excelente! Eres un usuario responsable del agua
#Comparar el consumo si es mayor o igual a 15 y SI es menor o igual  a 30
#Si el consumo esta entre 16 y 30 muestra el nombre, la categoria: Consumo normal y el mensaje: Tu consumo está dentro del promedio del hogar
#Comparar el consumo si es mayor a 30
#Si el consumo es mayor a 30 muestra el nombre, la categoria: Alto consumo y el mensaje: Atención: tu consumo es alto, revisa posibles fugas
#Si no entro en las comparaciones anteriores se sabe que el numero es 0 o es negativo
#Si el consumo es 0 o negativo muestra el mensaje: Dato inválido, Error: el consumo debe ser mayor a 0
#Terminar programa

nombre = input("Ingrese su nombre ")
consumo = int(input("Ingrese su consumo mensual de agua en metros cúbicos (número entero) "))

if consumo >= 1 and consumo <= 15:
    print(nombre,"-","Bajo consumo","¡Excelente! Eres un usuario responsable del agua")
elif consumo > 15 and consumo <= 30:
    print(nombre,"-","Consumo normal","Tu consumo está dentro del promedio del hogar")
elif consumo > 30:
    print(nombre,"-","Alto consumo","Atención: tu consumo es alto, revisa posibles fugas")
else:
    print("Dato inválido, Error: el consumo debe ser mayor a 0")
