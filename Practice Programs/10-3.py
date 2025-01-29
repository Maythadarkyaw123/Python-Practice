user_input = input("What is your name?\n")
file = open("guest.txt","a")
file.write(user_input + "\n")
print(user_input + " is added to text file.😊")
