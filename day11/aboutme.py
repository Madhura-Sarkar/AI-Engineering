with open("about_me.txt", "w") as file:
    file.write("Name: Madhura\n")
    file.write("Course: AI Engineering\n")
    file.write("Day: 11\n")
    file.write("Goal: Become an AI Engineer\n")
    
with open("about_me.txt", "r") as file:
    content = file.read()
print(content)

with open("about_me.txt", "a") as file:
    file.write("Current Skill: Python\n")
    
with open("about_me.txt", "r") as file:
    content = file.read()
print(content)