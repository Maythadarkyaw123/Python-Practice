#Day 3 PJ
#Simple calculator
name = input("What is your name? ")
input1 = int(input("Type first input: "))
input2 = int(input("Type second input: "))

if input2 == 0:
    print("Invalid input.")
else:
    print(f"--- Welcome {name} ---")
    choose = int(input(
        "Choose your operation in number:\n"
        "1 for addition\n"
        "2 for subtraction\n"
        "3 for multiplication\n"
        "4 for division\n"
        "5 for modulus\n"
        ": "
    ))

    if choose not in [1, 2, 3, 4, 5]:
        print("Choose between 1 and 5.")
    elif choose == 1:
        print("You chose 1, which is for addition.")
        add = input1 + input2
        print(f"Addition is {add}.")
    elif choose == 2:
        print("You chose 2, which is for subtraction.")
        sub = input1 - input2
        print(f"Subtraction is {sub}.")
    elif choose == 3:
        print("You chose 3, which is for multiplication.")
        mult = input1 * input2
        print(f"Multiplication is {mult}.")
    elif choose == 4:
        print("You chose 4, which is for division.")
        div = input1 / input2
        print(f"Division is {div}.")
    elif choose == 5:
        print("You chose 5, which is for modulus.")
        mod = input1 % input2
        print(f"Modulus is {mod}.")