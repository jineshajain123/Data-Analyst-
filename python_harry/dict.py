student = {
    "name": "Harry",
    "age": 25,
    "city": "Delhi"
}
print(student)  # it prints the entire dictionary

student = dict(name="Harry", age=25, city="Delhi")
print(student)

print(student["name"])
print(student["age"])

print(student.get("city"))
print(student.get("email"))

student["email"] = "test@gmail.com"
student["age"] = 26
print(student)
print(student.keys())
print(student.values()) 

age = student.pop("age")
print(age)

student.popitem()
print(student.popitem())
print(student)

#del student["age"]

student.clear()
print(student)

student.keys()
student.values()
print(student.values())
print(student.keys())

student.items()
print(student.items())

student = dict(name="Harry", age=25, city="Delhi")
for key in student:
    print(key)
    
for value in student.values():
    print(value)
    
for key, value in student.items():
    print(key, value)

print("name" in student)

new_student = student.copy()
print(new_student)

student.update({
    "course": "Python",
    "level": "Beginner"
})

user = {
    "id": 1,
    "profile": {
        "name": "Harry",
        "email": "test@gmail.com"
    }
}
print(user["profile"]["email"])

