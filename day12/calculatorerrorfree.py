try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    division = first_number / second_number
    print("The result of the division is:", division)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

    