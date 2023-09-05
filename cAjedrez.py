def bienvenida():
    print("El caballo será representado como '*' en el tablero y 'X' son los movimientos posibles\n")
    
#La funcion "crear_tablero" crea la matriz 8x8 con sus coordenadas 
def crear_tablero():
    tablero = []
    tablero.append([" ", 1, 2, 3, 4, 5, 6, 7, 8])
    tablero.append([1, "-", "-", "-", "-", "-", "-", "-", "-"])
    tablero.append([2, "-", "-", "-", "-", "-", "-", "-", "-"])
    tablero.append([3, "-", "-", "-", "-", "-", "-", "-", "-"])
    tablero.append([4, "-", "-", "-", "-", "-", "-", "-", "-"])
    tablero.append([5, "-", "-", "-", "-", "-", "-", "-", "-"])
    tablero.append([6, "-", "-", "-", "-", "-", "-", "-", "-"])
    tablero.append([7, "-", "-", "-", "-", "-", "-", "-", "-"])
    tablero.append([8, "-", "-", "-", "-", "-", "-", "-", "-"])
    return tablero

#La función "tablero_ajedrez" recorre la matriz e imprime su contenido sin corchetes
def tablero_ajedrez(tablero):
    for fila in tablero:
        for elemento in fila:
            #La funcion end separa cada elemento de las filas con un espacio
            print(elemento, end=" ")
        #Luego de recorrer cada fila el siguiente print las separa con un salto de linea
        print()
    #Para separar el tablero del texto que se imprime se ejecuta otro print vacio
    print()
    
# La funcion movimientos toma como parametros la fila y la columna ingresados por el usuario
def movimientos(fila, columna):
    #Se crea una lista con diferentes tuplas que contienen los 8 posibles  movimientos del caballo dentro del tablero
    posibilidades = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    #Se inicia una lista vacia para guardar las posiciones nuevas
    nuevas_posiciones = []

    # Validar si coordenadas del usuario están dentro del tablero
    if 1 <= fila < len(mi_tablero) and 0 <= columna < len(mi_tablero[1]):
        # Si las coordenadas del usuario estan dentro del tablero se representaran con un "*"
        mi_tablero[fila][columna] = "*"
        print()
        # Con una estructura for se recorre las 8 posibilidades de movimiento del caballo
        for posibilidad in posibilidades:
            # A la fila ingresada por el usuario se le agrega la posibilidad en su posicion 0, es decir la fila
            nueva_fila = fila + posibilidad[0]
            # A la columna ingresafa por el usuario se le agrega la posibilidad en su posicion 0, es decir la columna
            nueva_columna = columna + posibilidad[1]
            
            # Se valida si las nuevas coordenadas estan dentro de los limites de la matriz
            if 1 <= nueva_fila < len(mi_tablero) and 0 <= nueva_columna < len(mi_tablero[1]):
                # Si estan dentro de la matriz se agregan a la lista de las posiciones nuevas
                nuevas_posiciones.append((nueva_fila, nueva_columna))
    # En caso de que las posiciones no esten dentro de la matriz
    else:
        print("Posicion invalida\n")
    # Se retorna la lista de nuevas posiciones como resultado de la funcion
    return nuevas_posiciones

# A la funcion de movimientos_caballo se le pasa la lista de nuevas posiciones como parametro
def movimientos_caballo(nuevas_posiciones):
    # Con una estructura for se recorre la lista en filas y columnas
    for fila, columna in nuevas_posiciones:
        #Cada conjunto de coordenadas se representa con una X dentro del tablero
        mi_tablero[fila][columna] = "X"

# Bienvenida al programa
bienvenida()

# Crear el tablero
mi_tablero = crear_tablero()

# Mostrar el tablero
tablero_ajedrez(mi_tablero)

# Solicitar coordenadas al usuario
fila = int(input("Ingrese la fila: "))
columna = int(input("Ingrese la columna: "))

# Obtener las nuevas posiciones
posiciones_caballo = movimientos(fila, columna)

# Actualizar el tablero con las posiciones del caballo
movimientos_caballo(posiciones_caballo)

# Mostrar el tablero actualizado
tablero_ajedrez(mi_tablero)



    
    
