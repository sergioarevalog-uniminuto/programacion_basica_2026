edad = int(input("ingresa tu edad: "))
licencia = input("¿Tienes licencia vigente? (si/no) ")
if edad >= 18 and licencia == "si":
    print("Puedes conducir. ¡Maneja con cuidado!")
else:
    print("No puedes conducir.")
