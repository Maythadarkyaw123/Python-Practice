def make_shirt(size,message):
    print(f"Making a {size} shirt.")
    print(f"{message}")
    print(f"{message} And that must be {size}.")
    print(f"------------------------------------")
    
make_shirt("large size", "pls make it quickly.") #position argument

make_shirt(message = 'Thanks', size = 'small') #keyword argument