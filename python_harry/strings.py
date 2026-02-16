name= "jinesha jain"
print(name)
print(len(name)) # it prints the length of the string   output: 9
print(name[1]) # it prints the character at index 1  o
print(name[-1]) # it prints the last character of the string
print(name[0:4]) # it prints the substring from index 0 to 3
print(name[4:8]) # it prints the substring from index 4 to 7
print(name[::-1]) # it prints the string in reverse order
print(name[:-2]) # it prints the string except the last two characters
print(name.upper()) # it prints the string in uppercase
print(name.lower()) # it prints the string in lowercase
print(name.capitalize()) # it prints the string with the first character capitalized
print(name.replace("j", "J")) # it replaces 'j' with 'J' in the string
print(name.split("e")) # it splits the string at 'e' and returns a list 
print(name.split()) # it splits the string at whitespace and returns a list

text = "Hello World"
print(text.replace("World", "Python")) # it replaces 'World' with 'Python' in the string

items = ["apple", "banana", "orange"]
text = ",".join(items) # it joins the list items into a single string separated by commas
print(items)
print(text)

text = "Hello World"
position = text.find("World") # it finds the starting index of the substring 'World' in the string
print(position)

email = "test@gmail.com"
print(email.startswith("test")) # it checks if the string starts with 'test'
print(email.endswith(".com")) # it checks if the string starts with 'test' and ends with '.com'

first = "Hello"
second = "World"

result = first + " " + second # it concatenates two strings with a space in between
print(result)

text = "Python123"
print(text.isalpha()) # it checks if all characters in the string are alphabetic
print(text.isdigit()) # it checks if all characters in the string are digits
print(text.isalnum()) # it checks if all characters in the string are alphanumeric

name = "jenny"
age = 23

print(f"My name is {name} and I am {age} years old")