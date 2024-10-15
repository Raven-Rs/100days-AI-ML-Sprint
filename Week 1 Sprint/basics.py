# Python Basics Concepts

# 1. Variables and Data Types
favorite_number = 7          # Integer
user_name = "Alice"          # String
is_sunny = True              # Boolean
height = 1.75                # Float

# Rules for Naming Variables
#  - Must start with a letter or underscore
#  - Can contain letters, numbers, and underscores
#  - Case-sensitive
#  - Cannot be a Python keyword

# 2. Basic Operations and Operators
sum_result = favorite_number + 3     # Addition
difference = favorite_number - 2      # Subtraction
product = favorite_number * 2         # Multiplication
quotient = favorite_number / 2        # Division
floor_quotient = favorite_number // 2 # Floor Division
remainder = favorite_number % 3       # Modulo
power = favorite_number ** 2          # Exponentiation

# Print Basic Operations Results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Floor Quotient:", floor_quotient)
print("Remainder:", remainder)
print("Power:", power)

# 3. Control Structures
age = 18

# Conditional Statements
if age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
else:
    print("You're an adult!")

# Loops
# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count

# 4. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Lambda Functions
square = lambda x: x ** 2
print(square(4))

# 5. Input/Output Operations
user_input = input("What's your name? ")
print(f"Nice to meet you, {user_input}!")

# 6. String Methods
text = "  Hello, World!  "

# upper() - Converts to uppercase
print(text.upper())

# lower() - Converts to lowercase
print(text.lower())

# strip() - Removes leading and trailing whitespace
print(text.strip())

# replace() - Replaces occurrences of a substring
print(text.replace("World", "Python"))

# split() - Splits a string into a list
split_text = text.split(", ")
print(split_text)

# String Indexing and Slicing
first_char = text[0]        # Accessing the first character
substring = text[2:7]       # Slicing (from index 2 to 6)
print(first_char)
print(substring)

# 7. List Operations
# len() - Returns the number of elements in the list
print(len(fruits))

# in - Checks if an element is present
print("banana" in fruits)

# not in - Checks if an element is not present
print("grape" not in fruits)

# del - Deletes an element at a specific index
del fruits[1]               # Removes "banana"
print(fruits)

# pop() - Removes and returns the last element
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

# remove() - Removes the first occurrence of a specified element
fruits.append("banana")
fruits.remove("apple")
print(fruits)

# sort() - Sorts the list
fruits.sort()
print(fruits)

# reverse() - Reverses the list
fruits.reverse()
print(fruits)

# 8. Dictionaries
student = {"name": "Bob", "age": 13, "grade": 7}

# Accessing Values
name = student["name"]      # "Bob"
age = student.get("age")    # 13
print(name, age)

# Modifying Dictionaries
student["grade"] = 8        # Update grade
student["city"] = "New York"  # Add new key-value pair
print(student)

# Common Dictionary Operations
print(len(student))         # Number of key-value pairs
print(student.keys())       # Keys
print(student.values())     # Values
print(student.items())      # Key-value pairs
print(student.get("country", "Not Found"))  # Default value if key not found

# 9. Type Identification
print(type(age))            # Type of age
print(type(student))        # Type of student
