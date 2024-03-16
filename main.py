print("----------TASK 1----------")
# TASK 1: Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehensions.ares)
squares = [x**2 for x in range(1,10)]

print(squares)
print("----------TASK 2----------")
# TASK 2: Expand the previous program by defining a function that takes a range of numbers as input
# and returns a list of squares for that range.e_squares(start, end))
def generate_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares
start_num = 1
end_num = 10
result = generate_squares(start_num, end_num)
print(f"Squares of numbers from {start_num} to {end_num}: {result}")
print("----------TASK 3----------")
#TASK 3: Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.
class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x ** 2 for x in range(start, end + 1)]
        return squares
square_gen = SquareGenerator()
start_num = 1
end_num = 10
result = square_gen.generate_squares(start_num, end_num)
print(f"Squares of numbers from {start_num} to {end_num}: {result}")
print("----------TASK 4----------")
#TASK 4: Utilize the math library to calculate the square root of each number in the generated list from the previous task.
import math
class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

square_gen = SquareGenerator()
start_num = 1
end_num = 10
squares = square_gen.generate_squares(start_num, end_num)
square_roots = square_gen.calculate_square_roots(squares)

print(f"Squares of numbers from {start_num} to {end_num}: {squares}")
print(f"Square roots of squares: {square_roots}")
print("----------TASK 5----------")
#TASK 5: Handle the case where the end of the range is less than the start in the SquareGenerator class.
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

square_gen = SquareGenerator()
start_num = 1
end_num = 10
squares = square_gen.generate_squares(start_num, end_num)
square_roots = square_gen.calculate_square_roots(squares)

print(f"Squares of numbers from {start_num} to {end_num}: {squares}")
print(f"Square roots of squares: {square_roots}")
print("----------TASK 6----------")
#TASK 6: Extract the SquareGenerator class into a separate module named square_generator.py
from square_generator.square_generator import SquareGenerator

square_gen = SquareGenerator()
start_num = 1
end_num = 10
squares = square_gen.generate_squares(start_num, end_num)
square_roots = square_gen.calculate_square_roots(squares)

print(f"Squares of numbers from {start_num} to {end_num}: {squares}")
print(f"Square roots of squares: {square_roots}")

#TASK 7: Transform the square_generator module into a package by adding an empty __init__.py file and organize it accordingly.
print("----------TASK 7----------")

from square_generator.square_generator import SquareGenerator

square_gen = SquareGenerator()
start_num = 1
end_num = 10
squares = square_gen.generate_squares(start_num, end_num)
square_roots = square_gen.calculate_square_roots(squares)

print(f"Squares of numbers from {start_num} to {end_num}: {squares}")
print(f"Square roots of squares: {square_roots}")
#TASK 8: Create a subclass called CubicGenerator that inherits from the SquareGenerator class. Modify the CubicGenerator to generate cubes instead of squares.
print("----------TASK 8----------")

from square_generator.square_generator import SquareGenerator, CubicGenerator

square_gen = SquareGenerator()
start_num = 1
end_num = 10
squares = square_gen.generate_squares(start_num, end_num)
square_roots = square_gen.calculate_square_roots(squares)

print(f"Squares of numbers from {start_num} to {end_num}: {squares}")
print(f"Square roots of squares: {square_roots}")

cubic_gen = CubicGenerator()
start_num = 1
end_num = 10
cubes = cubic_gen.generate_cubes(start_num, end_num)
cube_roots = cubic_gen.calculate_cube_roots(cubes)

print(f"Cubes of numbers from {start_num} to {end_num}: {cubes}")
print(f"Cube roots of cubes: {cube_roots}")

#TASK 9: Override the square generation method in the Cubic Generator class to generate squares
# with a check to see if the start of the range is less than the end, if not return an Exceptions
print("----------TASK 9----------")

from square_generator.square_generator import CubicGenerator

cubic_gen = CubicGenerator()
start_num = 1
end_num = 10

try:
    squares = cubic_gen.generate_squares(start_num, end_num)
    print(f"Squares of numbers from {start_num} to {end_num}: {squares}")
except ValueError as e:
    print(f"Error: {e}")