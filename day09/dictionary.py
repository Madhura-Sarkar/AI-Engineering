#1
book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "pages": 320
}

print(book["title"])
print(book["author"])

#2
car = {
    "brand": "Toyota",
    "year": 2022
}
car["color"] = "Black"
print(car)

#3
person = {
    "name": "Alex",
    "age": 25,
    "city": "London"
}
for key in person:
    print(key, ":", person[key])

