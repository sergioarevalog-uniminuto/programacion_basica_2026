#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario la hora de inicio del viaje.
#Guardar la hora ingresada.
#Solicitar al usuario la distancia total del viaje en kilómetros.
#Guardar la distancia ingresada.
#Asignar el valor base del viaje en 5000.
#Comparar si la hora es mayor o igual a 21 o menor o igual a 5.
#Si la condición se cumple, calcular el recargo nocturno como el 30% del valor base.
#Sumar el recargo nocturno al total.
#Mostrar el valor del recargo nocturno aplicado.
#Comparar si la distancia del viaje es mayor que 10 kilómetros.
#Si la distancia es mayor que 10, calcular los kilómetros adicionales restando 10 a la distancia total.
#Calcular el recargo por kilómetros extra multiplicando los kilómetros adicionales por 800.
#Sumar el recargo por kilómetros extra al total.
#Mostrar la cantidad de kilómetros adicionales.
#Mostrar el valor del recargo por kilómetros extra.
#Mostrar el costo total del viaje.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese la hora de inicio del viaje (0 a 23):"
#LEER hora

#ESCRIBIR "Ingrese la distancia total del viaje en kilómetros:"
#LEER km

#total <- 5000

#SI hora >= 21 O hora <= 5 ENTONCES
    #recargo_nocturno <- total * 0.30
    #total <- total + recargo_nocturno
    #ESCRIBIR "Recargo nocturno aplicado: $", recargo_nocturno
#FIN SI

#SI km > 10 ENTONCES
    #km_extra <- km - 10
    #recargo_km <- km_extra * 800
    #total <- total + recargo_km
    #ESCRIBIR "Kilómetros adicionales:", km_extra
    #ESCRIBIR "Recargo por kilómetros extra: $", recargo_km
#FIN SI

#ESCRIBIR "Costo total del viaje: $", total
#FIN

hora = int(input("Ingrese la hora de inicio del viaje (0 a 23): "))
km = float(input("Ingrese la distancia total del viaje en kilómetros: "))

total = 5000

if hora >= 21 or hora <= 5: #Si la hora está entre 9 pm y 5 am, se suma un 30% de recargo.
    recargo_nocturno = total * 0.30
    total = total + recargo_nocturno
    print("Recargo nocturno aplicado: $", int(recargo_nocturno))

if km > 10: #Si el viaje supera 10 km, se cobran $800 por cada km adicional
    km_extra = km - 10
    recargo_km = km_extra * 800
    total = total + recargo_km
    print("Kilómetros adicionales:", km_extra)
    print("Recargo por kilómetros extra: $", int(recargo_km))

print("Costo total del viaje: $", int(total))