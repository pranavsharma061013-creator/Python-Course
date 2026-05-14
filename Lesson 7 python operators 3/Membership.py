print("Enter marks of 5 subjects:")
Maths = int(input())
Science = int(input())
English = int(input())
Hindi = int(input())
Computer = int(input())
Total = Maths + Science + English + Hindi + Computer
Average = int(Total / 5)
ValidRange = range(0 , 101) 
if Average not in ValidRange:
    print("Invalid input")
elif Average in range(91 , 101):
    print("Grade A1")
elif Average in range(81 , 91):
    print("Grade A2")
elif Average in range(71 , 81):
    print("Grade B1")
elif Average in range(61 , 71):
    print("Grade B2")
elif Average in range(51 , 61):
    print("Grade C1")