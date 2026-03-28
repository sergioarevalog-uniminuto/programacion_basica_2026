usuario = input("ingrese el usuario:")
contrasena = input("ingrese la contraseña:")
if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido. Bienvenido!")
    print("Cargando tu perfil...")
else:
    print("Acceso denegado. Datos incorrectos.")