def max_of_two(x: float, y: float) -> float:
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        biggest: float = x
    else:
        biggest: float = y
    return biggest

def max_of_three(x: float, y: float, z: float) -> float:
    """Given x, y, and z, which are 3 numbers, return the biggest number of the three."""
    max_value: float = x  # Inicializamos max_value con el valor de x

    if y > max_value:
        max_value = y
    if z > max_value:
        max_value = z

    return max_value
