# file = open("student.txt", "r")
# content = file.read()
# print(content)
# file.close()

# read mode 
with open("student.txt", "r") as file:
    content = file.read()

print(content)

# write mode 
with open("student.txt", "w") as file:
    file.write("Name: Madhura\n")
    file.write("Course: AI Engineering\n")
    file.write("Day: 11\n")

# append mode 
with open("student.txt", "a") as file:
    file.write("\nNew Course: Machine Learning")
   
# readline one by one line  
with open("student.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)

# readline all 
with open("student.txt", "r") as file:
    lines = file.readlines()

print(lines)
    
# loop through the file 
with open("student.txt", "r") as file:
    for line in file:
        print(line)
       

# remove the extra new line while printing the lines  
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())