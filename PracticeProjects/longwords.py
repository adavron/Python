f= open('textfile')
#lines = f.rea()
string = ''
for line in f:
    string += line.rstrip()
print string

#listwords = []
#for line in f:
#    words = line.split()
#    print words
 #   for word in words:
#        listwords.append((len(word),word))

