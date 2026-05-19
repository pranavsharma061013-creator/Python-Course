medical_cause = input("Do you have a medical cause? (yes/no):")
if medical_cause == "yes":
    print("You are allowed")
else:
    attendence = int(input("What is your attendence percentage?"))
    if attendence >= 75:
        print("allowed")
    else:
        print("not allowed")
