from math import cos, acos, degrees

from helper import DegreeFormula
from triangleTypes import typesOfTriangle


class triangle:
    sides: list[int] = []
    degrees: list[float] = []
    triangleType: typesOfTriangle

    def displayType(self):
        translations = ["nie-trójkąt", "trójkąt równoramienny", "trójkąt równoboczny", "trójkąt prostokątny",
                        "trójkąt dowolny"]
        print(f"Jest to {translations[self.triangleType.value]}")

    def determineType(self):
        temp = set(self.sides)

        if self.sides[0] + self.sides[1] < self.sides[2]:
            self.triangleType = typesOfTriangle.NOT
        elif (self.sides[0] ** 2) + (self.sides[1] ** 2) == (self.sides[2] ** 2):
            self.triangleType = typesOfTriangle.RIGHT
        elif len(temp) == 2:
            self.triangleType = typesOfTriangle.ISOSCELES
        elif len(temp) == 1:
            self.triangleType = typesOfTriangle.EQUILATERAL
        else:
            self.triangleType = typesOfTriangle.ANY

    def canBeCreated(self):
        pass

    def displayDegree(self):
        if self.triangleType.value != 0:
            print(f"Kąty tego trójkąta wynoszą: {self.degrees[0]}°, {self.degrees[1]}° i {self.degrees[2]}°")
        else:
            print("To nie jest trójkąt, więc nie można obliczyć jego kątów")

    def calcDegree(self):
        if self.triangleType.value != 0:
            self.degrees.append(DegreeFormula(self.sides[0], self.sides[1], self.sides[2]))
            self.degrees.append(DegreeFormula(self.sides[1], self.sides[2], self.sides[0]))
            self.degrees.append(DegreeFormula(self.sides[2], self.sides[1], self.sides[0]))
        else:
            for i in range(0, 3):
                self.degrees.append(-1)

    def create(self):
        try:
            self.sides[0] = (int(input("Podaj długość pierwszego boku: ")))
            self.sides[1] = (int(input("Podaj długość drugiego boku: ")))
            self.sides[2] = (int(input("Podaj długość trzeciego boku: ")))
        except ValueError:
            print("Nie podano liczby")
            self.sides = []
            self.create(triangle)
            exit(0)

        self.sides.sort()

    def __init__(self, sides: list[int]):
        self.sides = sides
        self.sides.sort()


class isosceles(triangle):
    def __init__(self, sides: list[int]):
        self.sides = sides
        self.sides[2] = sides[0] if sides[1] < sides[0] else sides[1]
        self.sides.sort()

    def drawTriangle(self):
