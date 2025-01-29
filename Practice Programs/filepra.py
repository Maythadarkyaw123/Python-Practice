f = open("../Python-Practice/filepra.txt", "a")
f.write("This is newly added\n")
f.close()

f = open("../Python-Practice/filepra.txt", "r")
print(f.read())
f.close()

f = open("../Python-Practice/filepra.txt", "w")
f.write("Wooo Hooo!")
f.close()

f = open("../Python-Practice/filepra.txt", "r")
print(f.read())
