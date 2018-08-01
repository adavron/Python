def awk(log):

    dic = {}
    f = open(log)
    for line in f:#reads each line
        column = line.split()#converts each line to list
        timeStamp = column[:3]#prints first 3 columns of each line since we are using with for loop (AWK))
        ttime = tuple(timeStamp)#this converts our list to tuple so we can put it in dictionary latter

        if ttime not in dic:# if first 3 column of each line is not in the dic it enters into dic.
            dic[ttime] = 1
        else:
            dic[ttime] += 1
#here we again convert dic to tuple, so we can sort our data and print int nicely
    loglist = []
    for key, val in dic.items():
        loglist.append((key, val))

    sortedlist = sorted(loglist)
    print "Time stamp,      Number of events"
    for key, val in sortedlist:
        print ' '.join(key), val
#print awk('/var/log/messages')
