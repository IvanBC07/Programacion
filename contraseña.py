contraseña_correcta = "python123"

# Inicializar variable para almacenar la contraseña ingresada por el usuario
contraseña_ingresada = ""

# Bucle que continuará hasta que se ingrese la contraseña correcta
while contraseña_ingresada != contraseña_correcta:
    contraseña_ingresada = input("Ingresa la contraseña: ")
    
    if contraseña_ingresada != contraseña_correcta:
        print("Contraseña incorrecta, intenta de nuevo.")

# Mensaje de acceso concedido cuando la contraseña es correcta
print("¡Acceso concedido!")