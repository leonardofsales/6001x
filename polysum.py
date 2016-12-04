def polysum(n, s):
    """
    n is the number of sides of a regular polygon
    s is the lenght of each side
    the function returns the sum of the area and the square of the perimeter, limited to 4 decimal places
    """
    import math
    area = 0.25*n*s**2 / math.tan(math.pi/n)
    perimeter = n*s
    result = area + (perimeter**2)
    return round(result, 4)