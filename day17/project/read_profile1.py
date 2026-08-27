import json

try:
    with open("profile1.json", "r") as file:
        content = json.load(file)

    print("===== AI PROFILE =====")
    print("Name:", content["name"])
    print("Age:", content["age"])
    print("Education:", content["Education"])
    print("Skills:", content["Skills"])
    print("Goal:", content["Goal"])


except (FileNotFoundError, json.JSONDecodeError):

    print("Profile file not found or empty. Let's create one!")

    def get_user_input():
        profile = {}

        print("\nEnter user profile details:")

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        Education = input("Enter your Education: ")
        Skills = input("Enter your skills: ")
        Goal = input("Enter your goal: ")

        profile["name"] = name
        profile["age"] = age
        profile["Education"] = Education
        profile["Skills"] = Skills
        profile["Goal"] = Goal

        return profile

    profile = get_user_input()

    with open("profile1.json", "w") as file:
        json.dump(profile, file, indent=4)

    print("\nProfile successfully saved!")

    print("\n===== AI PROFILE =====")
    print("Name:", profile["name"])
    print("Age:", profile["age"])
    print("Education:", profile["Education"])
    print("Skills:", profile["Skills"])
    print("Goal:", profile["Goal"])