guests = []

guests.insert(2,raw_input('enter 1st name: '))
guests.insert(1,raw_input('enter 3rd name: '))
guests.append(raw_input('enter 3rd name: '))


print guests
guests.sort()
print ('\nwe are sorting you list alphabetically: ')
print (guests)

for guest in guests:
    print('Dear '+guest.title()+' please call me!')
print ('loop is over '+guest.title())




