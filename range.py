# range(): Generates a sequence of numbers within a specified range.
# Example #1 
for i in range(5):
    print(i)

# Example #2 
for j in range(0,201):
    print(j)

# Example # 3

for k in range(0,101):
    print(k)
    print("these number are from 0 to 100")

# str.lower(): Converts a string to lowercase.

text = "Hello World"
lower_text = text.lower()
print(lower_text)  # Output: hello world

# str.upper(): Converts a string to uppercase.

text = "Hello World"
upper_text = text.upper()
print(upper_text)  # Output: HELLO WORLD

# str.strip(): Removes leading and trailing whitespace from a string.

text = "   Hello World   "
stripped_text = text.strip()
print(stripped_text)  # Output: Hello World

# str.split(): Splits a string into a list of substrings based on a delimiter.

text = "Hello,World,Python"
split_text = text.split(",")
print(split_text)  # Output: ['Hello', 'World', 'Python']

# str.join(): Joins elements of a sequence into a string using a specified delimiter.

words = ['Hello', 'World', 'Python']
joined_text = ",".join(words)
print(joined_text)  # Output: Hello,World,Python

# str.format(): Formats a string by replacing placeholders with specified values.

name = "Alice"
age = 25
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print(formatted_text)  # Output: My name is Alice and I am 25 years old.