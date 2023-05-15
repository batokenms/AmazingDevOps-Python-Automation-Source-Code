# Working with sequences: Functions such as len(), sorted(), reversed(), and enumerate() 
# provide convenient ways to handle sequences like lists, strings, and tuples.
# len(): Returns the length (number of elements) of a sequence.
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5

# sorted(): Returns a new sorted list from the elements of a sequence.

my_list = [5, 2, 8, 3, 1]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 2, 3, 5, 8]

# reversed(): Returns an iterator that yields the elements of a sequence in reverse order.

my_string = "Hello, world!"
reversed_string = ''.join(reversed(my_string))
print(reversed_string)  # Output: "!dlrow ,olleH"

# enumerate(): Returns an iterator of tuples containing the index and value of each element in a sequence.

my_list = ['apple', 'banana', 'orange']
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: orange

# These examples showcase the usage of each function for working with sequences, such as lists, strings, and tuples, in Python.