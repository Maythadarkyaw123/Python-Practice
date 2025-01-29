Name = input("Name: ")
print(f"{Name}'s Calculator")

print("Different Calculator's Functions are:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

Choice = input("Which operation do you want?(Note: only 1,2,3,4)\n")

if Choice in ['1','2','3','4']:
    Num1 = float(input("Enter first number: "))
    Num2 = float(input("Enter second number: "))
    if Choice == '1':
        print(f"{Num1} + {Num2} = {Num1 + Num2}")
        
    if Choice == '2':
        print(f"{Num1} - {Num2} = {Num1 - Num2}")
        
    if Choice == '3':
        print(f"{Num1} x {Num2} = {Num1 * Num2}")
        
    if Choice == '4':
        print(f"{Num1} / {Num2} = {Num1 / Num2}")