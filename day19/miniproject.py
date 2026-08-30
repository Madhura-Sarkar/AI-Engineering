import csv

with open("students2.csv", "r") as file:
    reader = csv.reader(file)
    
    next(reader)
    
    total = 0
    count = 0
    for row in reader:
        total = total + int(row[3])
        count = count + 1
        
    average = total / count
    print(average)
            
