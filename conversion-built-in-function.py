# int(): Converts a value to an integer.

num_str = "42"
num_int = int(num_str)
print(num_int)  # Output: 42

# float(): Converts a value to a float.

num_str = "3.14"
num_float = float(num_str)
print(num_float)  # Output: 3.14

# str(): Converts a value to a string.

num_int = 42
num_str = str(num_int)
print(num_str)  # Output: "42"

# list(): Converts an iterable (such as a string or tuple) to a list.

my_string = "Hello, world!"
my_list = list(my_string)
print(my_list)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']

# type(): Returns the type of an object.

num = 42
print(type(num))  # Output: <class 'int'>

my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>

# isinstance(): Checks if an object is an instance of a specified class or its subclass.

num = 42
print(isinstance(num, int))  # Output: True

my_list = [1, 2, 3]
print(isinstance(my_list, list))  # Output: True

# These examples demonstrate the usage of each function for type conversion (int, float, str, list) and type checking (type, isinstance) in Python.