
# try and except: Used to catch and handle exceptions that may occur within a block of code.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred!")

# In this example, the try block attempts to divide 10 by 0, which would raise a ZeroDivisionError. The except block catches the exception and executes the specified code, printing an error message.

# raise: Used to raise a specific exception manually.

def validate_age(age):
    if age < 0:
        raise ValueError("Invalid age: Age cannot be negative.")

try:
    validate_age(-5)
except ValueError as e:
    print(e)

# In this example, the validate_age() function raises a ValueError if the provided age is negative. The raise statement is used to raise the exception, and the except block catches it and prints the error message.

# assert: Used for debugging and to check that a certain condition is true, otherwise raises an AssertionError.

def calculate_square_root(number):
    assert number >= 0, "Error: Cannot calculate square root of a negative number."
    return number ** 0.5

result = calculate_square_root(-9)