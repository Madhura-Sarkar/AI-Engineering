# Problem Statement

# A student has learned several skills, but some were entered more than once.

# Write a program that:

# Stores the skills in a list (including duplicates).
# Converts the list into a set.
# Prints all unique skills.
# Prints the total number of unique skills.
# Stores the student's basic information in a tuple.
# Unpacks the tuple and prints the values.

skills = ["Python", "Java", "Python", "JavaScript", "Java", "C++"]
unique_skills = set(skills)
print("Unique Skills:", unique_skills)
print("Total Number of Unique Skills:", len(unique_skills))
student_info = ("Madhura", 22, "Computer Science")
name, age, major = student_info
print(f"Name: {name}, Age: {age}, Major: {major}")
print("Python" in unique_skills)