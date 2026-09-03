import csv

employees = []

# Read CSV and store data
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)

highest_salary = 0
highest_paid_employee = ""

for employee in employees:
    salary = int(employee["Salary"])

    if salary > highest_salary:
        highest_salary = salary
        highest_paid_employee = employee["Name"]

print("Highest Paid Employee:", highest_paid_employee)
print("Highest Salary:", highest_salary)