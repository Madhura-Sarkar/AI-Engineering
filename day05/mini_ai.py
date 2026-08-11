hungry = input("Are you hungry? ")

if hungry == "yes":
    pizza = input("Do you like pizza? ")

    if pizza == "yes":
        print("Order a pizza!")
    else:
        print("Try a sandwich.")

else:
    print("Maybe drink some water.")