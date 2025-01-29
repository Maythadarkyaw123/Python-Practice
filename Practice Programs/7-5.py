print("Welcome to Movie Theater!")

while True:
    age = int(input("Enter age: "))
    if age <= 3:
        print("Ticket fee is free for you!")
        break
    elif 3 < age <= 12:
        print("Ticket fee is $10.")
        break
    elif age > 12:
        print("Ticket fee is $15")
        break