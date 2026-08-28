import json

with open ("student.json", "r") as file:
    student = json.load(file)
    
print(student["name"])
print(student["course"])
print(student["skills"][1])
print(student["projects"])