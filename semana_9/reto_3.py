#Pide al usuario un número con input() y muestra su tabla de multiplicar del 1 al 10.
#Si el usuario escribe 7, imprime: 7x1=7, 7x2=14... hasta 7x10=70
num = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
