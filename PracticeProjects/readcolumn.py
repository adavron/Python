delimeter = ' '
dic = {}
f = open('log')
for line in f:
    column = line.split()
    #print column[0], column[1], column[2]
    time = column[0:3]
#    print time
    ttime = tuple(time)
#    print ttime
    if ttime not in dic:
        dic[ttime]=1
    else:
        dic[ttime] +=1
tlist = []
for key, val in dic.items():
    tlist.append((key, val))
print 'Time stamp,      Number of events'
for key, val in tlist:
    print ' '.join((key)), val

