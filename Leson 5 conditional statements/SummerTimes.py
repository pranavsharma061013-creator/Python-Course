temperature = int(input("Enter today's temperature in °C: "))

if temperature >= 35:
    print("It's blazing hot! Perfect time for ice cream ")
elif 25 <= temperature < 35:
    print("It's warm and sunny! Great for a swim ")
elif 15 <= temperature < 25:
    print("It's pleasant weather! Maybe a picnic ")
else:
    print("Not quite summer vibes... cozy up with a book ")