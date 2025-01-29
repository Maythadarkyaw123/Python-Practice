mylist = ["may", "thadar", "kyaw"]
print(mylist)
left = mylist.pop(0)
print( left + " can not join")
mylist.insert(0, "Yoon")
print(mylist)
for a in mylist:
    print(a + ", Welcome to the dinner!")
print("---------------------------------")
    
for a in mylist:
    print(a + ", Thanks for joining")
print("---------------------------------")

mylist.insert(0, "Eaint")
print(mylist)

mylist.insert(2, "Mue")
print(mylist)

mylist.append("Aung")
print(mylist)
print("---------------------------------")

for a in mylist:
    print(a + ", Come to join dinner with us")