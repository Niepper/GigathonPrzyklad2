from math import degrees, acos


def DegreeFormula(a:int, b:int, c:int, roundTo = 2):
    return round(degrees(acos(((b ** 2) + (c ** 2) - (a ** 2)) / (
            2 * b * c))), roundTo)