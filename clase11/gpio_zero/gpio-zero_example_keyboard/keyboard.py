
choice = ""
while choice == "":
    choice = input("Please select an option by entering a number between 1 and 4")
    options = ["1", "2", "3", "4"]

    if choice not in options:
        print("That wasn't one of the options; please try again")
        choice = ""

if choice == "1":
    print("You chose number 1")
elif choice == "2":
    print("You chose number 2")
elif choice == "3":
    print("You chose number 3")
elif choice == "4":
    print("You chose number 4")