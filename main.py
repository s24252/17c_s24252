# Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehensions.ares)
squares = [x**2 for x in range(1,10)]

print(squares)

#Expand the previous program by defining a function that takes a range of numbers as input
# and returns a list of squares for that range.e_squares(start, end))
def generate_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares
start_num = 1
end_num = 10
result = generate_squares(start_num, end_num)
print(f"Squares of numbers from {start_num} to {end_num}: {result}")