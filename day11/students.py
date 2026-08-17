name1 = input("Enter student1 name: ")
name2 = input("Enter student2 name: ")
name3 = input("Enter student3 name: ")

with open("students.txt", "w") as file:
    file.write(name1 + "\n")
    file.write(name2 + "\n")
    file.write(name3 + "\n")

with open("students.txt", "r") as file:
    lines = file.readlines()
    unique_names = {line.strip() for line in lines}
    print(unique_names)
    print(len(unique_names)) 
