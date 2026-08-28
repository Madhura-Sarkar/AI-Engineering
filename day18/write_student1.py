import json

student = {
    "name": "Madhura",
    "course": "AI Engineering",
    "skills": ["Python", "JSON"]
}

student["skills"].append("Git")

with open ("student1.json", "w") as file:
    json.dump(student, file)

with open ("student1.json", "r") as file:
    student = json.load(file)
    
print(student["name"])
print(student["course"])
print(student["skills"][0])
print(student["skills"][1])

