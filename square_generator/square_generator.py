import math

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            start, end = end, start
        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to start")
        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def generate_cubes(self, start, end):
        if end < start:
            start, end = end, start
        cubes = [x**3 for x in range(start, end + 1)]
        return cubes

    def calculate_cube_roots(self, numbers):
        cube_roots = [math.pow(num, 1/3) for num in numbers]
        return cube_roots
