def car(manufacter, model, **kwargs):
    carinfo = {}
    carinfo['manufacter'] = manufacter
    carinfo['model'] = model   #the same working way i have shown the following 
    '''carinfo = {
        'manufacter': manufacturer,
        'model': model
    }'''
    for key, value in kwargs.items():
        carinfo[key] = value
    return carinfo

print(car('Toyota', 'Camry', tow_package = True, color='Red', year=2020))