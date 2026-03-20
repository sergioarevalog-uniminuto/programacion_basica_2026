#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario el valor total de la compra.
#Guardar el valor de la compra.
#Comparar si el valor de la compra es mayor que 100000.
#Si la compra es mayor que 100000, calcular el total a pagar aplicando un descuento del 15%.
#Mostrar el mensaje: “Descuento aplicado.”
#Mostrar el total a pagar.
#En caso contrario, mostrar el mensaje: “Sin descuento.”
#Mostrar el valor original de la compra como total a pagar.
#Finalizar el programa.


#PSEUDOCÓDIGO

#INICIO
#ESCRIBIR "Ingrese el valor total de la compra:"
#LEER compra

#SI compra > 100000 ENTONCES
    #total_pagar <- compra * 0.85
    #ESCRIBIR "Descuento aplicado."
    #ESCRIBIR "Total a pagar: $", total_pagar
#SINO
    #ESCRIBIR "Sin descuento."
    #ESCRIBIR "Total a pagar: $", compra
#FIN SI
#FIN

compra = int(input("Ingrese el valor total de la compra: ")) #guarda el valor de la compra

if compra > 100000:
    total_pagar = compra * 0.85 #Si la compra es mayor a 100000, se aplica 15% de descuento
    print("Descuento aplicado.")
    print("Total a pagar: $", int(total_pagar))
else: #Si la compra es 100000 o menos, no hay descuento
    print("Sin descuento.")
    print("Total a pagar: $", compra)