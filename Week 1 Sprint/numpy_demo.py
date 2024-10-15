# NumPy Fundamentals

import numpy as np

# 1. NumPy Arrays and Operations
# Creating NumPy arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Basic operations on arrays
array_sum = np.sum(array_1d)               # Sum of all elements
array_mean = np.mean(array_1d)             # Mean of all elements
array_std = np.std(array_1d)               # Standard deviation

# Element-wise operations
array_squared = array_1d ** 2              # Squaring each element
array_doubled = array_1d * 2                # Doubling each element

# 2. Array Indexing and Slicing
# Indexing
first_element = array_1d[0]                # Accessing the first element
second_row = array_2d[1, :]                # Accessing the second row of a 2D array

# Slicing
sub_array = array_1d[1:4]                   # Slicing elements from index 1 to 3
sub_array_2d = array_2d[:, 1:]              # Slicing columns from index 1 onwards

# 3. Broadcasting
# Broadcasting allows arithmetic operations between arrays of different shapes
array_a = np.array([[1], [2], [3]])
array_b = np.array([10, 20, 30])

# Adding a 1D array to a 2D array
broadcasted_sum = array_a + array_b

# 4. Basic Linear Algebra Operations
# Defining matrices for linear algebra operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)

# Determinant and inverse
determinant = np.linalg.det(matrix_a)
try:
    inverse_matrix = np.linalg.inv(matrix_a)
except np.linalg.LinAlgError:
    inverse_matrix = "Matrix is singular and cannot be inverted."

# 5. Introduction to AI/ML Concepts
# Basic introduction to AI/ML
def introduction_to_ai_ml():
    """Provide a brief overview of AI/ML concepts."""
    return (
        "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. "
        "Machine Learning (ML) is a subset of AI that enables systems to learn from data and improve "
        "their performance over time without being explicitly programmed. "
        "Python is widely used in AI/ML due to its simplicity and the availability of powerful libraries such as NumPy, pandas, and scikit-learn."
    )

# Main execution
if __name__ == "__main__":
    # Display results of NumPy operations
    print("1D Array:", array_1d)
    print("2D Array:\n", array_2d)
    print("Sum of 1D Array:", array_sum)
    print("Mean of 1D Array:", array_mean)
    print("Standard Deviation of 1D Array:", array_std)
    print("Squared Array:", array_squared)
    print("Doubled Array:", array_doubled)
    print("First Element:", first_element)
    print("Second Row of 2D Array:", second_row)
    print("Sliced Array:", sub_array)
    print("Sliced 2D Array:\n", sub_array_2d)
    print("Broadcasted Sum:\n", broadcasted_sum)
    print("Matrix Product:\n", matrix_product)
    print("Determinant of Matrix A:", determinant)
    print("Inverse of Matrix A:\n", inverse_matrix)
    print(introduction_to_ai_ml())
