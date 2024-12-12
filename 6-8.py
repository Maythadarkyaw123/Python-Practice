cat = {
    'pet' : 'cat',
    'owner' : 'May',
    'age' : 3,
    'color' : 'white'
}

dog = {
    'pet' : 'dog',
    'owner' : 'Yoon',
    'age' : 5,
    'color' : 'black'
}

bird = {
    'pet' : 'bird',
    'owner' : 'Thadar',
    'age' : 2,
    'color' : 'yellow'
}

pets = [cat, dog, bird]

for pet in pets:
    print("--------------------------------------")
    for key, value in pet.items():
        print(f'{key} : {value}')