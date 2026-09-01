import csv

def show_employees():
    with open("employees.csv", "r") as file:
        reader = csv.reader(file)
        
        next(reader)
        
        for rows in reader:
            print(f"{rows[0]} - {rows[1]}")
            
show_employees()

          
def high_salary_employees():
    with open("employees.csv", "r") as file:
        reader = csv.reader(file)
            
        next(reader)

        for rows in reader:
            salary = int(rows[2])  
            if salary > 25000:
                print(rows[0])
        
high_salary_employees()


def calculate_average_salary():
    with open("employees.csv", "r") as file:
            reader = csv.reader(file)
                
            next(reader)
    
            total = 0
            total_employees = 0
            
            for rows in reader:
                salary = int(rows[2]) 
                total += salary
                total_employees += 1
            average = total / total_employees
            print(f"Average salary: {average}")

calculate_average_salary()

def employee_summary():
    with open("employees.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)
        
                total_salary = 0
                total_employees = 0
                
                for rows in reader:
                    salary = int(rows[2]) 
                    total_salary += salary
                    total_employees += 1
                    
                average = total_salary / total_employees
                
                print(f"Total Employees: {total_employees}")
                print(f"Total salary: {total_salary}")
                print(f"Average salary: {average}")
                
employee_summary()


def find_employee():
    name = input("Enter employee name: ")

    found = False

    with open("employees.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for rows in reader:
            if name == rows[0]:
                print(f"Name: {rows[0]}")
                print(f"Department: {rows[1]}")
                print(f"Salary: {rows[2]}")

                found = True
                break

    if found == False:
        print("Employee not found")
        
find_employee()