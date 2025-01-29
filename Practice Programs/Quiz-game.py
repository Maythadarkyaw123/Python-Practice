print("Let's Play Quiz! 🙋😃")
user_input = input("Do you wanna play quiz game?\n")

if user_input.lower() != "yes":
    quit()
    
else:
    print("Let's start the quiz game. I will ask you a question and you have to answer.")
    score = 0
    q1 = input("Full form of RAM: ")
    if q1.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
        
    q2 = input("Full form of ROM: ")
    if q2.lower() == "read only memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
        
    print("Yay! You complet the quiz and got " + str(score)+ " marks.")
    print("You got "+ str((score/2)*100) + "%")
