# Se importa la libreria random
# Random proporciona funciones relacionadas con la generacion de numeros aleatorios
import random

# Se genera un numero aleatorio entre 0 y 100
numero_aleatorio = random.randint(0, 100)
# Inicializacion de el contador de intentos
intentos = 0

# Se usa una estructura while-true que se deja de ejecutar en caso de un break
while True:
    numero_usuario = int(input("Adivina el numero entre 1 y 100: "))
    # Se valida si el numero ingresado es menor que el numero aleatorio
    if numero_usuario < numero_aleatorio:
        # Se otorga una pista en funcion al numero ingresado
        print(f"El numero es mayor que {numero_usuario}")
        # Cada intento fallido se suma al contador
        intentos += 1
    elif numero_usuario > numero_aleatorio:
        print(f"El numero es menor que {numero_usuario}")
        intentos += 1
    else: 
        print(f"Adivinaste el numero \nCantidad de intentos: {intentos} \nEl numero es: {numero_aleatorio} ")
        break
    
    
        