#Programa para calcular el area del triangulo
#ingresar la base del triangulo en metros
#ingresar la altura del triangulo en metros
#usar formula area = (base*altura)/2
#muestra el area calculada
#evaluar la siguiente condicion: si el area > 100 muestra true
#evaluar la siguiente condicion: si el area <= 100 muestra false

base=float(input("Ingrese el valor de la base del triangulo en metros "))
altura=float(input("Ingrese el valor de la altura del triangulo en metros "))
area=((base*altura)/2)
print(area)
print("El area es mayor que 100", area > 100)
print("El area es menor o igual que 100", area <= 100)
