print("Welcome to Movie Theater!")
user = input("Do you wanna buy tickect? (y/n):")
if user == "y":
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
elif user == "n":
    usr = input("If you don't want to continue type 'quit'\n")
    if usr == "quit":
        print("Come Again!")
    
