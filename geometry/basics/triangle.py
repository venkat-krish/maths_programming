#
# Triangle shape is a 2D plane shapes, which has 3 sides
#

class Triangle:

    def __init__(self, base: int, height: int, angles: tuple, sides: tuple):
        self.base = base
        self.height = height
        self.angles = angles
        self.sides = sides

    def area(self) -> float:
        '''
            computes the area of the triangle. The formula is
            area = 1/2 x base x height
        :return: float
        '''
        area = 0.5 * (self.base * self.height)
        return area

    def perimeter(self) -> int:
        '''
            Computes the perimeter by adding the sides of the triangle
        :return: int
        '''
        return sum(self.sides)



    def triangle_type(self):
        """
            finds a type of triangle based on the angles
            Acute Triangle = All angles are less than 90 degree
            Right Triangle = Has one 90 degree
            Obtuse Triangle = Has an angle more than 90 degree
        """
        if sum(self.angles) != 180:
            return "Not a triangle"
        else:
            if 90 in self.angles:
                return "Right Triangle"
            else:
                obtuse_angle = list(filter(lambda x: x > 90, self.angles))
                acute_triangle = list(filter(lambda x: x < 90, self.angles))
                print(acute_triangle)
                if obtuse_angle:
                    return "Obtuse angle"
                elif acute_triangle:
                    return "Acute Triangle"

    def __str__(self):
        base_statement = f"The triangle base is {self.base} and height is {self.height}, with an area as {self.area()} \n"
        angle_statement = f"The angles indicate that the triangle is {self.triangle_type()}"
        perimeter_statement = f"The perimeter of the triangle is {self.perimeter()}"
        # statement list contains the definition of triangle
        statements = [base_statement, angle_statement, perimeter_statement]

        return "\n".join(statements)


if __name__ == "__main__":
    # angles = (45, 45, 90)
    angles = (68,41,71)
    sides = (208, 203, 145)
    triangle = Triangle(203, 137, angles, sides)

    print(triangle)
