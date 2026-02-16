# def greet(fname, lname):
#     print("Good Morning!", fname, lname)
#     print("How are you!")
#     print("Thank you!")

# greet("Rohan", "Das") 
# greet("Harry", "Khan") 

def add(a, b):
    # print(a+b)
    return a + b

c = add(4, 6)
print(c)



def greet(name="User", city="Delhi"):
    print("Hello", name, city)

greet()
greet("Rohan")
greet(city="Alwar", name="Aakash")


# def add(a, b): 
#     return a + b

add = lambda a, b: a + b  # lambda function is an anonymous function that can take any number of arguments, but can only have one expression. It is often used for short, simple functions that are not reused elsewhere in the code.

print(add(5, 7))