try:
    num1, num2 = eval(input("Enter two numbers,seperated by a comma:"))
    result = num1 / num2
    print("result is",result)

except ZeroDivisionError:
    print("division by zero is an error!!")
except SyntaxError:
    print("Comma is missing,enter numbers seperated by comma like 1,2")
except:
    print("Wrong input")
else:
    print("No execptions")
finally:
    print("This will execute no matter what")
    