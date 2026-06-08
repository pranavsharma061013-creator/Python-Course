rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print spaces first (to create the mirror effect)
    for j in range(rows - i):
        print(" ", end="")
    # Print stars after spaces
    for k in range(i):
        print("*", end="")
    print()  # Move to next line