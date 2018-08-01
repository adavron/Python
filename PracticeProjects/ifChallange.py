menu = []

menu.append(['egg','spam','bac'])
menu.append(['egg','sas','bac'])
menu.append(['egg','spam'])
menu.append(['egg','bac','sas','spam'])
menu.append(['spam','bac','sas','spam'])

for meal in menu:
    if not 'egg' in meal:
        for item in meal:
            print item

        print meal