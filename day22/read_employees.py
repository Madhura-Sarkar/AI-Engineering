import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # print(row)
        # print(row["Name"], "-", row["Department"])
    
        salary = int(row["Salary"])
        if salary > 25000:
            print(row["Name"])