myself = {
    "Name": "Madhura",
    "Age": 22,
    "Favourite_Language": "Python",
    "Dream_Job": "Designer and Developer"
}

print(myself["Name"])
print(myself["Age"])
print(myself["Favourite_Language"])
print(myself["Dream_Job"])


phone = {
    "brand":"Samsung",
    "price":25000
}
phone["Color"] = "Blue"
print(phone)

# Loop through:
country = {
    "India":"New Delhi",
    "Japan":"Tokyo",
    "France":"Paris"
}
for key, value in country.items():
    print(f"{key} : {value}")