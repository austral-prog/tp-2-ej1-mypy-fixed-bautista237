def is_leap_year() -> bool:
    año: int = int(input("Ingrese un año: "))
    bisiesto:bool = False
    if (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0):
            bisiesto:bool = True
    print(f"El año {año} {'es' if bisiesto else 'no es'} bisiesto")
    return bisiesto
