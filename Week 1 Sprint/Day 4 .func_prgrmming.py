# Functional Programming and Comprehensions

# 1. Map, Filter, and Reduce Functions
from functools import reduce

def square(x):
    """Return the square of a number."""
    return x ** 2

def is_even(x):
    """Return True if the number is even, otherwise False."""
    return x % 2 == 0

def add(x, y):
    """Return the sum of two numbers."""
    return x + y

# Example data
numbers = [1, 2, 3, 4, 5]

# Using map to apply the square function to each element
squared_numbers = list(map(square, numbers))

# Using filter to keep only even numbers
even_numbers = list(filter(is_even, numbers))

# Using reduce to compute the sum of the list
sum_of_numbers = reduce(add, numbers)

# 2. Advanced List Comprehensions
# List comprehension to create a list of squares of even numbers
even_squares = [x**2 for x in numbers if is_even(x)]

# Nested list comprehension to flatten a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
flattened_matrix = [num for row in matrix for num in row]

# 3. Dictionary and Set Comprehensions
# Dictionary comprehension to create a dictionary of squares
squares_dict = {x: x**2 for x in numbers}

# Set comprehension to create a set of unique squares
unique_squares = {x**2 for x in numbers}

# 4. Generators and Iterators
def generate_numbers(n):
    """Generator function that yields numbers from 0 to n-1."""
    for i in range(n):
        yield i

# Using the generator
number_generator = generate_numbers(5)
generator_output = list(number_generator)

# Iterator example
class Counter:
    """An iterator that counts from 0 to a specified limit."""
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            current = self.count
            self.count += 1
            return current
        else:
            raise StopIteration

# Using the Counter iterator
counter = Counter(5)
counter_output = list(counter)

# 5. Decorators
def decorator_function(original_function):
    """A simple decorator that prints the function name before calling it."""
    def wrapper_function():
        print(f"Function name: {original_function.__name__}")
        return original_function()
    return wrapper_function

@decorator_function
def greet():
    """A simple function to greet."""
    return "Hello, world!"

# Testing the decorator
greeting = greet()

# All features demonstration
if __name__ == "__main__":
    print("Squared Numbers:", squared_numbers)
    print("Even Numbers:", even_numbers)
    print("Sum of Numbers:", sum_of_numbers)
    print("Even Squares:", even_squares)
    print("Flattened Matrix:", flattened_matrix)
    print("Squares Dictionary:", squares_dict)
    print("Unique Squares:", unique_squares)
    print("Generator Output:", generator_output)
    print("Counter Output:", counter_output)
    print("Greeting:", greeting)
