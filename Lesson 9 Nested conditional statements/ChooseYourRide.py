choice = int(input("Enter your choice:"))
if(choice == 1):
    print("What type of bike?")
    print("1: Scooty")
    print("2: Scooter\n")
    choice2 = int(input("Enter your choice2:"))
    if choice2 == 1:
        print("You have chosen scooty")
    else:
        print("You have selected scooter")
elif choice == 2:
    print("What type of car?")
    print("1: Sedan")
    print("2: XUV")
    choice3 = int(input("Enter your choice3:"))
    if choice3 == 1:
        print("You have chosen a sedan")
    else:
        print("You have chosen an XUV")

else:
    print("Wrong option!")