# Program to demonstrate use of in-built string functions in Python
# accept string from user

text = input("Enter a string: ")

# convert to uppercase
print("Uppercase:", text.upper())

# convert to lowercase
print("Lowercase:", text.lower())

# convert to title case
print("Title Case:", text.title())

# find position of a substring
word = input("Enter a word to find: ")
pos = text.find(word)
if pos != -1:
    print(f"'{word}' found at position {pos}")
else:
    print(f"'{word}' not found in the string.")
    
# replace a word with another
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("After replacement:", text.replace(old, new))

# split the string into words
print("Words in string:", text.split())

# remove extra spaces
print("String after removing leading/trailing spaces:", text.strip())
