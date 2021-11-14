#
# Triangle shape is a 2D plane shapes, which has 3 sides
#

class Triangle:

    def __init__(self, base:int, height:int):
        self.base = base
        self.height = height

    def area(self) -> float:
        '''
            computes the area of the triangle. The formula is
            area = 1/2 x base x height
        :return: float
        '''
        area = 0.5 * (self.base * self.height)
        return area

    def __str__(self):
        return f"The triangle base is {self.base} and height is {self.height}, with an area as {self.area()}"


if __name__ == "__main__":
    triangle = Triangle(203, 137)

    print(triangle)