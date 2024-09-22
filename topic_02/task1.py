from math import *

def discriminant(a, b, c): # Пошук дискримінанта
    return b**2 - 4 * a * c

def quadratic(a, b, c):
    D = discriminant(a, b, c) 
    
    if D > 0: # Якщо дискримінант більше 0, то має два кореня
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0: # Якщо дискримінант == 0, то має один корень
        x = -b / (2 * a)
        return x, x
    else: # Якщо дискримінант < 0, то немає коренів
        return "Коренів немає"

print(quadratic(-2, 5, 6))