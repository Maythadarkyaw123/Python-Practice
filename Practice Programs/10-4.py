while True:
    name = input("Enter Name or quit: \n")
    if name.lower() == 'quit':
        print("Bye Bye 😿")
        break
    print(name + ", Welcome to Python!")
    with open("guest_book.txt", "a") as text_file:
        text_file.write(name + "\n")
