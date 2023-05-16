# Printing a string

print("This is me")
print(("Hello, world!"))

age = 25    # this is a variable 

print(age)  # you can print the name of the variable

# However, ypu can always format the strings to be more dynamic. using 
# "f" or .format(name of the variable)

# We can us the f and if we do so, we going to add the name of the 
# the variable inside the placeholder{}

print(f"Jane is a great girl and she now {age} years old")

# Alternative 2 - you can use the .format() method to manipulated 
# the string further. 

print("Jane is a great girl and she now {} years old.".format(age))

print(f"kenyan is now block because the country is just {age} years old")

