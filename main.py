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
from square_generator import SquareGenerator

square_gen = SquareGenerator()
start_num = 1
end_num = 10
squares = square_gen.generate_squares(start_num, end_num)
square_roots = square_gen.calculate_square_roots(squares)

print(f"Squares of numbers from {start_num} to {end_num}: {squares}")
print(f"Square roots of squares: {square_roots}")

