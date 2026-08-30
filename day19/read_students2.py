import csv

with open("students2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["name", "age", "course", "marks"])
    writer.writerow(["Madhura", 22, "AI Engineering", 85])
    writer.writerow(["Rohan", 27, "Python", 72])
    writer.writerow(["Sayak", 28, "Data science", 92])
    
# exercise 4
with open("students2.csv", "a", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Soham", 22, "Python", 88])
    
# exercise 5
with open("students2.csv", "r") as file:
    reader = csv.reader(file)
    
    next(reader)
    
    for row in reader:
        if int(row[3]) >= 80:
            print(f"{row[0]} scored {row[3]}")
            
