def leap_year() -> bool:
    año: int = int(input("Ingrese un año: "))
    # Determina si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        bisiesto = True
    else:
        bisiesto = False
    # Imprime el resultado
    print(f"El año {año} {'es bisiesto' if bisiesto else 'no es bisiesto'}")
    return bisiesto


