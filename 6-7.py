person = {
    'first_name' : "May",
    'last_name' : 'kyaw',
    'City' : 'Rajkot'
}

food = {
    'may' : 'apple',
    'thadar' : 'banana',
    'kyaw' : 'mango'
}

vehicle = {
    'may' : 'car',
    'thadar' : 'bike',
    'kyaw' : 'bus'
}

allto = [person, food, vehicle]

for i in allto:
    print('\nDetail:')
    for key, value in i.items():
        print(f'{key}:{value}')