river = {
    'ayeyarwadi' : 'myanmar',
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'mississippi' : 'united states'
}

for r, v in river.items():
    print(f'{r} is the river that runs through {v}')
    
print('---------------------------')

for name in river.keys():
    print(name.capitalize())
    
print('---------------------------')

for country in river.values():
    print(country.capitalize())