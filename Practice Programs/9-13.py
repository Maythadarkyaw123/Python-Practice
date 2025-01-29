from collections import OrderedDict
Glossary = OrderedDict()
Glossary['Fruit'] = 'Apple'
Glossary['Vegetable'] = 'Tomato'
Glossary['Meat'] = "Beef"

for key, value in Glossary.items():
    print(key +" = " + value)
    