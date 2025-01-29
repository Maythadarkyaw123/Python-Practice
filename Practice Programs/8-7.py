#without optional argument
'''def make_album(name,title):
    myal = {
        'Artist' : name.upper(),
        'Album Title' : title.upper()
    }
    return myal

print(make_album('micle','myage'))'''

#with optional argument
def make_album(name,title,track=None):
    myal = {
        'Artist' : name.upper(),
        'Album Title' : title.upper()
    }
    if track:
        myal['Track'] = track
    return myal

print(make_album('micle','myage'))
print(make_album('jackson','mystar',track=12))