num = int(input("Enter a decimal number: "))

binary = ""   
temp = num


for i in range(1):
    
    while temp > 0:
        remainder = temp % 2         
        binary = str(remainder) + binary  
        temp = temp // 2              

if num == 0:
    binary = "0"

print("Binary representation of", num, "is", binary)