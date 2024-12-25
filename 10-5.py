while True:
    user_input = input("Why do you like programming?/Type 'quit' for quit.\n")
    if user_input.lower() == 'quit':
        print("Bye Bye 👋")
        break
        
    else:
        text = open("reason.txt","a")
        text.write(user_input + "\n")
        
    
    