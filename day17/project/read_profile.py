# ===== MY VERSION =====

# import json

# try:
#     with open("profile.json", "r") as file:
#         content = json.load(file)
        
#     print("===== AI PROFILE =====")
#     print(content)
    
# except json.JSONDecodeError:
#     print("The profile file is empty or contains invalid JSON.")

# ===== UPDATED VERSION =====
import json

try:
    with open("profile.json", "r") as file:
        content = json.load(file)

    print("===== AI PROFILE =====")
    print("Name:", content["name"])
    print("Age:", content["age"])
    print("Education:", content["Education"])
    print("Skills:", content["Skills"])
    print("Goal:", content["Goal"])

except FileNotFoundError:
    print("Profile file not found.")

except json.JSONDecodeError:
    print("The profile file is empty or contains invalid JSON.")