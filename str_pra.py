# ways to print
name = "Davic"
print("Hello ", name)
print("Nice to meet you "+ name)

# multiline 
para = '''Hello,
This is Davic's friend.
Pleasure to meet with you.
'''
print(para)

# print specific chara
print(name[0])      # output must be D

# all the characters 
for character in name:
    print(character)
    
# string slicing
myname = "Yoon"
print(myname[0:3])  # 0 is starting index, 3 is length of string which start from first character
print(myname[:3])   # this will print the same with above
print(myname[0:-2]) # 0 is starting index, (length of str is 4 - 2 = 2) output is Yo
print(myname[-1:-1]) # this won't gonna print anything coz (4-1):(4-1) = index 3 which is n : length of str is 3 which is till Yoo
print(myname[-3:-1]) # output is oo

print("'''''''''''''''''''''''''''''''''''")

#string methods
n_name = "eaiNt muE"
print(len(n_name)) 
print(n_name.upper())
print(n_name.lower())
print(n_name.capitalize()) 
print(n_name.replace("eaiNt", "yoOn"))
print(n_name.split(" "))
print(n_name.count("e"))  # times of e , don't include E

bro = "!wai!"
print(bro.rstrip("!")) #remove ! from right side
print(bro.lstrip("!")) #remove ! from left side
print(len(bro))
print(bro.center(50, ".")) # 50 is length of string, to got str length fill with .
