import csv

employees = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)

print(employees)

for employee in employees:
    print(f"{employee['Name']} - {employee['Salary']}")

print(reader.fieldnames)