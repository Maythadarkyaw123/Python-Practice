def build_profile(fname, lname, **all): #python thinks as dictionary 
    alldata = {}
    alldata['firstname'] = fname
    alldata['lastname'] = lname
    for key, value in all.items():
        alldata[key] = value
        
    return alldata
        
print(build_profile('John', 'Doe', city='New York', country='USA'))
        