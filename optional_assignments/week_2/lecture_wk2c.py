import math

def polysum(n, s):
    '''
    Area of regular polygon: (0.25*n*s^2)/tan(pi/n)
    Perimeter of a polygon: n * s
    
    Returns a sum of the area and square of the perimeter of the polygon
    '''
    area = (0.25 * n * (s ** 2)) / math.tan(math.pi / n)
    perimeter = n * s
    
    return round(area + perimeter ** 2, 4)