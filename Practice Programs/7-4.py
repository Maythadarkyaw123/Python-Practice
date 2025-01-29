print("Welcome to Pizza Shop!")
print("If you want to stop just type 'quit'")

while True:
    pizza = input("Enter your pizza order: ")
    if pizza == "quit":
        print("Thanks for buying pizza!")
        break
    else:
        print("Added new pizza to list")
    