print("Initializing....")

a = int(input("Enter a: \n")) 
b = int(input("Enter b: \n")) 
try:
    print("The value of a/b is: ", a/b)
except Exception as e: 
    print("Some error occurred! - ", e)

print("Thank you...")