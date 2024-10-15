# Advanced Features for AI/ML

# 1. Object-Oriented Programming (OOP) Basics
class Employee:
    def __init__(self, name, age, department):
        """Initialize an employee with name, age, and department."""
        self.name = name
        self.age = age
        self.department = department

    def introduce(self):
        """Return a string introducing the employee."""
        return f"Hello, my name is {self.name} and I work in {self.department}."

class Manager(Employee):
    def __init__(self, name, age, department, team_size):
        """Initialize a manager with additional team_size attribute."""
        super().__init__(name, age, department)
        self.team_size = team_size

    def manage_team(self):
        """Return a string about team management."""
        return f"I manage a team of {self.team_size} people."

    def introduce(self):
        """Override the introduce method to include team size."""
        return f"{super().introduce()} I manage a team of {self.team_size}."

# 2. Modules and Packages
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of a by b."""
    if b == 0:
        return "Error: Division by zero."
    return a / b

# 3. Exception Handling
def divide_numbers(a, b):
    """Return the division of a by b, handling potential errors."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Please provide numeric inputs."
    else:
        return result

# 4. File I/O Operations
def read_file(file_path):
    """Read data from a file and return it as a list of lines."""
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def write_to_file(file_path, data):
    """Write a list of strings to a file."""
    with open(file_path, 'w') as file:
        file.writelines(data)

def append_to_file(file_path, data):
    """Append a list of strings to a file."""
    with open(file_path, 'a') as file:
        file.writelines(data)

# 5. Context Managers
class FileHandler:
    """A context manager for file handling."""
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        """Open the file and return the file object."""
        self.file = open(self.file_path, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the file when done, handling exceptions if necessary."""
        if self.file:
            self.file.close()

# Additional context manager using the built-in 'open' function
def write_and_read_file(file_path, data):
    """Write data to a file and then read it back using context managers."""
    with open(file_path, 'w') as file:
        file.writelines(data)
    
    with open(file_path, 'r') as file:
        return file.readlines()

# Testing OOP and Exception Handling
if __name__ == "__main__":
    emp = Employee("Alice", 30, "HR")
    print(emp.introduce())

    mgr = Manager("Bob", 40, "IT", 5)
    print(mgr.introduce())
    
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))
    print(divide_numbers(10, "a"))

    data_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
    write_to_file('example.txt', data_to_write)
    file_contents = read_file('example.txt')

    append_to_file('example.txt', ["Appending a new line.\n"])
    with FileHandler('example.txt') as file:
        lines = file.readlines()
