import json

student = {
    "name": "Madhura",
    "age": 22,
    "skills": ["Python", "HTML", "CSS"]
}

data = json.dumps(student)

print(data)
print(type(data))

data1 = '{"name": "Madhura", "age": 22}'

student1 = json.loads(data1)

print(student1)
print(type(student1))

