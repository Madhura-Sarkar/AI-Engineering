marks = int(input("Enter Marks: "))
income = int(input("Enter Family Income: "))

if marks >=90 and income <= 30000:
    print("Congratulations! You are eligible for a scholarship.")
else:
    print("Sorry, you are not eligible for a scholarship.")