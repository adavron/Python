f = open('log')
content = f.readlines()

for item in content:
    column = item.split()
    #print column
    column_3 = ' '.join(column[:3])
    print column_3

