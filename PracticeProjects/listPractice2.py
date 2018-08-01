chesses = ['cheddar','edam','gouda']
numbers = [17,22, 32,12]
empty = []
print chesses, numbers, empty
print chesses[1]
chesses[2] = 4
chesses.append('mosarella')
chesses.extend(numbers)
print chesses
print numbers
#for i in dir(numbers):
#    print i
chesses.remove('edam')
print chesses
print max(numbers)
print min(numbers)
print len(numbers)