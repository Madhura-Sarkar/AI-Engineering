import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    # exercise 1 
    # for row in reader:
        # print(row)
        # print(f"{row[0]} is learning {row[2]}")
       
    # exercise 2  
    next(reader)
      
    for row in reader:  
        if int(row[1]) > 21:
            print(f"{row[0]} is {row[1]} years old")
            
    