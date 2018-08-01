requested = ['onion','tomato','popo','ugu']

available = ['onion','tomato','behi']

for topping in requested:
    if topping in available:
        print ('adding '+topping)
    else:
        print ('we do not have '+topping)
