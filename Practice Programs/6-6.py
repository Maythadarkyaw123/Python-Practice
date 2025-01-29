mylist = ['jen','sarah', 'edward']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in favorite_languages.keys():
    if name in mylist:
        print(f"{name}'s favorite language is {favorite_languages[name]}")