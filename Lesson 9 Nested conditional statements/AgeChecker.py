age = int(input("Enter your age: "))


for i in range(1):
    
    for j in range(1):
        if age >= 10:
            if age <= 20:
                print("Your age is between 10 and 20.")
            else:
                print("Your age is greater than 20.")
        else:
            print("Your age is less than 10.")