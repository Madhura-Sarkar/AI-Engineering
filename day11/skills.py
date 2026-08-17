with open("skills.txt", "w") as file:
    file.write("Python\n")
    file.write("Python\n")
    file.write("HTML\n")
    file.write("HTML\n")
    file.write("CSS\n")
    file.write("JavaScript\n")
    file.write("Figma\n")
    
with open("skills.txt", "r") as file:
    for line in file:
        print(line.strip())
       
# to remove the duplicate lines 
# method1  
# with open("skills.txt", "r") as file:
#     lines = file.readlines()
#     unique_lines = set(lines)
#     print(unique_lines)

# method2 which also called 'set comprehension'
with open("skills.txt", "r") as file:
    lines = file.readlines()

unique_lines = {line.strip() for line in lines}

print(unique_lines)