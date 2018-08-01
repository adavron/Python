def groceryList(item1, item2, item3):
    starter()
    print item1
    print item2
    print item3
    print 'carrot'
    print 'eggs'
    print 'fish'
    print
    seperator()


i1 = raw_input('Enter 1st item: ')
i2 = raw_input('Enter 2nd item: ')
i3 = raw_input('Enter 3rd item: ')


def seperator():
    print '***************'
    print

def starter():
    print'###########################'
    print'#  Hello This is your list#'
    print'###########################'



groceryList(i1, i2, i3)
