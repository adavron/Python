f = open('csv')
for line in f:
    field = line.split(';')
    field1 = field[0]
    field2 = field[1]
    field3 = field[2]

    print(field1, field2, field3)