def is_leap_year() -> bool:
    año: int = int(input("Ingrese un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        bisiesto = True  # Solo se asigna el valor sin la declaración de tipo
    else:
        bisiesto = False
    print(f"El año {año} {'es bisiesto' if bisiesto else 'no es bisiesto'}")
    return bisiesto
