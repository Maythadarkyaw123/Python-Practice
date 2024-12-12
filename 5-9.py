# List of usernames
usernames = ['may', 'user1', 'user2', 'user3']

# Check if the list is empty
if not usernames:
    print("We need to find some users!")
else:
    # Greet each user
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")

# Remove all usernames from the list
usernames = []

# Test the empty list again
if not usernames:
    print("We need to find some users!")
