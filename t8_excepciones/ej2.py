while True:
    try:
        x = int(input("Por favor, ingresa un número: "))
        break
    except ValueError:
        print("¡Vaya! Eso no es un número válido. Inténtalo de nuevo...")
