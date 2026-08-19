try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Invalid input.")

else:
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")

        print(f"Valid age: {age}")

    except ValueError as error:
        print("Error:", error)

finally:
    print("Age verification completed.")