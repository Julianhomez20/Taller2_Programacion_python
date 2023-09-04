def numero_palindromo (num):
    # Se convierte el número ingresado en un String
    num_str = str(num)
    
    # Comparamos el String con el String invertido
    if num_str == num_str[::-1]:
        print("El numero es palindromo")
    else:
        print("El numero no es palindromo")

numero_palindromo(int(input("Ingrese un número: ")))
