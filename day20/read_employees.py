import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name","Department","Salary"])
    writer.writerow(["Madhura","Design","35000"])
    writer.writerow(["Akash","Deployment","22000"])
    writer.writerow(["Rohan","Data Engineer","40000"])
    writer.writerow(["Sraban","Marketing","20000"])
    
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    
    next(reader)
    
    # count = 0
    # for row in reader:
    #     salary = int(row[2])
        
    #     if salary > 25000:
    #         count += 1
    #         print(row[0])
            
    # print(f"Total employees above 25000: {count}")
    
    total = 0
    total_employee = 0
    above_25k = 0
    
    for row in reader:
        salary = int(row[2])
        
        # calculate total salary 
        total += salary
        
        # Count all employee
        total_employee += 1
        
        if salary > 25000:
            above_25k += 1
            print(row[0])
            
    # Calculate average
    average = total / total_employee
    
    print(f"Total employee whose salary is above 80: {above_25k}")
    print(f"Average salary: {average}")
            