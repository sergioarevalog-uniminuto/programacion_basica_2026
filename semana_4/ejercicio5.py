#ALGORITMO

#Iniciar el programa.
#Solicitar al usuario el nombre del producto.
#Guardar el nombre del producto.
#Solicitar al usuario el precio unitario del producto.
#Guardar el precio unitario.
#Solicitar al usuario la cantidad de unidades.
#Guardar la cantidad de unidades.
#Calcular el subtotal multiplicando el precio por la cantidad.
#Calcular el IVA tomando el 19% del subtotal.
#Calcular el total sumando el subtotal y el IVA.
#Mostrar el nombre del producto.
#Mostrar el precio unitario.
#Mostrar la cantidad de unidades.
#Mostrar el subtotal.
#Mostrar el valor del IVA.
#Mostrar el total a pagar.
#Comparar si el total es mayor que 50000.
#Mostrar si aplica descuento especial.
#Finalizar el programa.


#PSEUDOCODIGO

#INICIO
#ESCRIBIR "Ingrese el nombre del producto:"
#LEER producto

#ESCRIBIR "Ingrese el precio unitario:"
#LEER precio

#ESCRIBIR "Ingrese la cantidad de unidades:"
#LEER cantidad

#subtotal <- precio * cantidad
#iva <- subtotal * 0.19
#total <- subtotal + iva

#ESCRIBIR "Producto:", producto
#ESCRIBIR "Precio:", precio
#ESCRIBIR "Cantidad:", cantidad
#ESCRIBIR "Subtotal:", subtotal
#ESCRIBIR "IVA (19%):", iva
#ESCRIBIR "Total:", total
#ESCRIBIR "Aplica descuento especial?:", total > 50000
#FIN

producto=input("Ingrese el nombre del producto: ")
precio=float(input("Ingrese el precio unitario: "))
cantidad=int(input("Ingrese la cantidad de unidades: "))

subtotal=precio*cantidad
iva=subtotal * 0.19
total=subtotal + iva

print("Producto:", producto)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Subtotal:", subtotal)
print("IVA (19%):", iva)
print("Total:", total)
print("Aplica descuento especial?:", total>50000)