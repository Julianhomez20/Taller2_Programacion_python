#Se inicializa una lsita para guardar los numeros
l_numeros = []
# Contador de numeros positivos
p_numeros = 0
# Contador de numeros negativos
n_numeros = 0

# Se usa la estructura while true
# While-True se ejecuta hasta la aparición del break
while True:
    numero = int(input("Ingrese un numero: "))
    # Si el numero ingresado es 0 se termina el programa
    if numero == 0:
        break
    # Cada numero se ingresa a la lista inicial
    l_numeros.append(numero)
# Se recorre cada numero de la lista 
for num in l_numeros:
    # Se valida si cada numero es menor que 0
    if num < 0:
        # Numeros negativos se suman al contador negativo
        n_numeros += 1
    else:
        # Numeros positivos se suman al contador positivo
        p_numeros += 1
# Se multiplica la cantidad de numeros positivos por asterico
p_asteriscos = "*" * p_numeros
# Se multiplica la cantidad de numeros negativos por asterisco
n_asteriscos = "*" * n_numeros
print(f"Positivos: {p_asteriscos}")
print(f"Negativos: {n_asteriscos}")
        
    