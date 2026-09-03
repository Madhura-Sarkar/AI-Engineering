import csv

employees = []

# Read CSV and store data
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)

lowest_salary = float("inf")
lowest_paid_employee = ""

# float("inf") means infinity—a value larger than normal numbers.

for employee in employees:
    salary = int(employee["Salary"])

    if salary < lowest_salary:
        lowest_salary = salary
        lowest_paid_employee = employee["Name"]

print("Lowest Paid Employee:", lowest_paid_employee)
print("Lowest Salary:", lowest_salary)