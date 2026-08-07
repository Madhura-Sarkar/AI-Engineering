name = input("Enter you name: ")
age = input("enter your age: ")
newage = int(age)
age_after_10years = newage + 10
print("Hello " +name)
print("Your age after 10 years will be: " + str(age_after_10years))


# using f-Strings 
# The f before the string means:
# "Python, replace everything inside {} with the variable's value."
name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))

newage_after_10years = age1 + 10

print(f"Hello {name1}")
print(f"Your age after 10 years will be: {newage_after_10years}")
