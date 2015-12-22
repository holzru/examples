import math
from decimal import Decimal, getcontext

def triangle_type(a, b, c):
    sides = (a, b, c)
    sides = list(sides)
    sides.sort()
    getcontext().prec = 10
    if sides[0] == 0:
        return 0
    try:
        if sides[2]**2 == sides[0]**2 + sides[1]**2:
            return 2
        else:
            gamma = math.degrees(math.acos(Decimal(sides[0]**2 + sides[1]**2 - sides[2]**2)/Decimal(2*sides[0]*sides[1])))
            if 0 < gamma < 90:
                return 1
            elif 180 > gamma > 90:
                return 3
            else:
                return 0
    except ValueError:
        return 0
