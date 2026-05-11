Value = int(input("Enter amount to withdraw:"))
notes_100 = Value // 100
notes_50 = (Value % 100) // 50
notes_10 = ((Value % 100) % 50) // 10
print("Number of 100 notes:", notes_100)
print("Number of 50 notes:", notes_50)
print("Number of 10 notes:", notes_10)