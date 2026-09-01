import csv 

with open("students.csv", "r") as file: 
    reader = csv.reader(file) 
    
    next(reader) 
    
    # practice 1
    # for row in reader: 
    #     marks = int(row[2]) 
        
    #     if marks < 80: 
    #         print(row[0])

    # practice 2 
    # count = 0    
    # for row in reader: 
    #     marks = int(row[2]) 
        
    #     if marks < 80: 
    #         count += 1
    #         print(row[0])
    # print(f"Total students below 80: {count}")

    # practice 3
    total = 0
    total_students = 0
    below_80 = 0

    for row in reader:
        marks = int(row[2])

        # Calculate total marks
        total += marks

        # Count all students
        total_students += 1

        # Find students below 80
        if marks < 80:
            below_80 += 1
            print(row[0])

    # Calculate average
    average = total / total_students

    print(f"Total students below 80: {below_80}")
    print(f"Average marks: {average}")