# Data Structures

# 1. Lists and List Comprehensions
# Lists are versatile collections that allow for dynamic data storage.
numbers = [1, 2, 3, 4, 5]

# List comprehension for squaring each number in the list
squared_numbers = [x**2 for x in numbers]

# Filtering to include only even squared numbers
even_squared_numbers = [x for x in squared_numbers if x % 2 == 0]

# Nested lists and flattening a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]

# 2. Tuples
# Tuples are immutable sequences used to store fixed data points.
# Example: Representing a 3D point in space
point_3d = (10.0, 20.0, 30.0)
x, y, z = point_3d  # Unpacking

# Named tuple for better readability
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# 3. Dictionaries
# Dictionaries store data as key-value pairs, providing efficient lookups.
# Example: Storing employee information
employees = {
    'E001': {'name': 'Alice', 'age': 30, 'department': 'HR'},
    'E002': {'name': 'Bob', 'age': 25, 'department': 'IT'},
    'E003': {'name': 'Charlie', 'age': 35, 'department': 'Finance'}
}
# Adding a new employee
employees['E004'] = {'name': 'David', 'age': 28, 'department': 'Marketing'}

# Accessing an employee's information
bob_info = employees['E002']

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(6)}

# 4. Sets
# Sets are collections of unique elements, useful for data preprocessing.
# Example: Finding unique words in a sentence
sentence = "Machine learning is fun and machine learning is powerful"
words = sentence.lower().split()
unique_words = set(words)

# Set operations: intersection, union, and difference
another_set = {'powerful', 'exciting', 'fun'}
common_words = unique_words.intersection(another_set)
all_words = unique_words.union(another_set)
different_words = unique_words.difference(another_set)

# Frozenset example
frozen_set = frozenset([1, 2, 3])

# 5. String Manipulation
# String manipulation is crucial for natural language processing (NLP).
text = "Natural Language Processing with Python"
# Splitting the text into words
words_in_text = text.split()

# Converting to lowercase for uniformity
lowercase_text = text.lower()

# Finding the length of the string
text_length = len(text)

# Joining words back into a single string
joined_text = ' '.join(words_in_text)

# Replacing a substring
replaced_text = text.replace("Python", "AI")

# Function to demonstrate text preprocessing for NLP
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    return words

# Example usage of the preprocess function
raw_text = "Hello, world! Welcome to Natural Language Processing."
preprocessed_words = preprocess_text(raw_text)

# Additional string manipulation: String formatting and regex
name = "Alice"
greeting = f"Hello, {name}!"  # String formatting using f-strings

import re
# Regular expression example: finding words with exactly 4 letters
pattern = r"\b\w{4}\b"
four_letter_words = re.findall(pattern, "This is a test string.")
