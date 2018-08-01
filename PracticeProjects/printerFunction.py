unprinted_item = ['iphone case','tooth','car','robot','decoration']
printed_item=[]

def print_models(unprinted, printed):
    while unprinted:
        current=unprinted.pop()
        print("Now printing "+current)
        printed.append(current)

def show_models(printed):
    for item in printed:
        print(item+" has been printed successfully!")


#print_models(unprinted_item,printed_item)
#print('\n')
#show_models(printed_item)