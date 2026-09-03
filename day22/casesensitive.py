import csv

employees = []

# Read CSV and store data
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)

# Ask the user which department to search
department = input("Enter department name: ")

found = False

# Search employees
for employee in employees:
    if employee["Department"].lower() == department.lower():
        print(employee["Name"], "-", employee["Salary"])
        found = True

# If no employee was found
if found == False:
    print("No employee found in this department.")