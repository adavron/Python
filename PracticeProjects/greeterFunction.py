def great_user():
    """Greats user"""
    print ('Hello user')

great_user()

def animal(name, type='dog'):
    """Prints animal name and type"""
    print ("I have "+type+" and its name is "+name)

animal('bob',type='colie')
def formatted_name(first_name, last_name):
    """returns formatted name"""
    full_name = first_name+' '+last_name
    return full_name.title()
hulu=formatted_name('asdae','awffff')
musi=formatted_name('bob','hikoli')
print musi
print hulu
