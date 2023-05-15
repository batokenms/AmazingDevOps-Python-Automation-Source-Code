# Create a file called example.txt

file = open("example.txt", "w")
file.close()

# Command to read the content of the file 
file = open("example.txt", "r")

# read(): Reads the contents of a file.

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Allows you to call a function on the result of another function.
# Not all functions can chain together as it depends on the type and the available method of objects. 




