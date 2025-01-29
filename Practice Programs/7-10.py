# Dictionary to store user responses
dream_vacations = {}

# Flag to indicate polling is active
polling_active = True

# Start the polling loop
while polling_active:
    # Ask the user for their name and dream vacation
    name = input("\nWhat is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary
    dream_vacations[name] = vacation

    # Ask if they want to continue the poll
    repeat = input("Would you like to let another person respond? (yes/no): ").lower()
    if repeat == 'no':
        polling_active = False

# Print the results of the poll
print("\n--- Poll Results ---")
for name, place in dream_vacations.items():
    print(f"{name} would like to visit {place}.")
