def max_of_two(x: float, y: float) -> float:
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        biggest = x  # Solo se asigna el valor sin la declaración de tipo
    else:
        biggest = y
    return biggest

def max_of_three(x: float, y: float, z: float) -> float:
    """Given x, y, and z, which are 3 numbers, return the biggest number of the three."""
    max_value = x  # Solo se asigna el valor sin la declaración de tipo

    if y > max_value:
        max_value = y
    if z > max_value:
        max_value = z

    return max_value
