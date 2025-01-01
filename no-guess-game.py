import random

while True:
    up_bound = input("Enter upper bound (1-10): ")
    if up_bound.isdigit():
        up_bound = int(up_bound)
        if up_bound <= 0:
            print("Please enter a number more than 0.")
        elif up_bound >= 10:
            print("Please enter a number less than 10.")
        else:
            # Generate a random number within the given range
            gen = random.randint(1, up_bound)
            while True:
                guess = input(f"Guess the number (1-{up_bound}): ")
                if guess.isdigit():
                    guess = int(guess)
                    if guess == gen:
                        print("You are correct!")
                        break
                    else:
                        print("Try again!")
                else:
                    print("Invalid input. Please enter a number.")
            break
    else:
        print("Invalid input. Please enter a number between 1 and 10.")
