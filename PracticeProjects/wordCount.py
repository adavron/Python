text = 'but soft what kight in yonder window breaks'
words = text.split()
t = []
for word in words:
    t.append((len(word),word))
#print t
t.sort(reverse=True)
#print t
#t[2] ='oooo'
print t

res = list()
for l, i in t:
    res.append(i)
print res