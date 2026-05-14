revenue = float(input("Enter the total revenue:"))
selling_price = float(input("Enter selling price"))
if selling_price > revenue:
    profit = selling_price - revenue
    print("The profit is", profit)
else: 
    print("No profit")
