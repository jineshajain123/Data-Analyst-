age = 18
if age >= 18:
    print("Eligible")
    
    
age = 16
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
    
score = 75

if score >= 90:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")
    
x = 10

if x == 10:
    print("Equal")

if x != 5:
    print("Not equal")
    
age = 25
country = "India"

if age >= 18 and country == "India":
    print("Allowed")
    
age = 20

if age >= 18:
    if age < 60:
        print("Adult")
        
age = 15

if age >= 18:
    pass
else:
    print("Minor")
    
age = 20
status = "Adult" if age >= 18 else "Minor"