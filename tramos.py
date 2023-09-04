# Se crean dos listas para almacenar la duracion en minutos y en horas
dm_tramos = []
dh_tramos = []

# Con un bucle while se solicita el tiempo hasta que el valor ingresado sea 0
# Cuando es 0 se ejecuta el break para detener el bucle 
while True:
    tramo = int(input("Ingrese la duracion de su tramoe en minutos: "))
    if tramo != 0:
        # Se agrega cada tramo a la lista de tramos en minutos
        dm_tramos.append(tramo)
    # Cuando se ingresa el 0 se detiene la solicitud de tiempos
    else:
        # Con un ciclo for se recorre cada tiempo dentro de la lista
        for tramo in dm_tramos:
            # Cada tiempo de cada tramo se convierte en horas
            h_tramo = tramo / 60
            # Ya que el tiempo esta en horas se agrega a la lista de tramos en hora
            dh_tramos.append(h_tramo)
        # Usando la funcion sum, sumamos todos los valores de la lista de tiempo en horas
        total_tiempo = sum(dh_tramos)
        # Se separa la parte entera de la decimal del tiempo
        horas = int(total_tiempo)
        # Conversion de la parte decimal a minutos
        minutos = int((total_tiempo - horas) * 60)
        print(f"Tiempo total del recorrido ha sido {horas}:{minutos} horas")
        break
    
        
        
    