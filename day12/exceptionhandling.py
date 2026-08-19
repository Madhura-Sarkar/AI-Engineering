try:
    age = int(input("Please enter your age: "))

except ValueError:
    print("Invalid input. Please enter a valid age.")

else:
    if age < 0:
        print("Age cannot be negative.")
    else:
        print(f"Your age is {age}.")