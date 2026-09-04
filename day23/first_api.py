import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# print(response)


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

# print(data)

# for user in data:
#     print(user["name"], "-", user["email"])
    
# finding particular data using api 
found = False

search_name = input("Enter a name to search: ")

for user in data:
    if search_name.lower() in user["name"].lower():
        print("user found!")
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("Phone:", user["phone"])
        print("City:", user["address"]["city"])
        
        found = True
    
if not found:
    print("user not found")