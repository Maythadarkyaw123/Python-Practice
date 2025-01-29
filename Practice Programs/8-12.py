def person(*arg): #python thinks as tuple.
    for i in arg:
        print(f"{i} want pizza.")
    print("---------------------------")

person("Mg","May","Su")
person("Mike","Josep","Joe")
person("Ella","Bella","Tina")