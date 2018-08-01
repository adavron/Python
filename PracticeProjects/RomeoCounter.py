
def topTenWordCounter(text):
    '''This opens text file converts it in one line '''
    hfile = open(text)
    line = hfile.read()
    line = line.lower()
    rlist = line.split()
    print rlist


    rdic = {}
    for i in rlist:
        if not i in rdic:
            rdic[i] = 1
        else:
            rdic[i]+=1
#print"below results of rdic"
    tlist = []
    for key, val in rdic.items():
        tlist.append((val, key))
    print tlist

    tlist.sort(reverse=True)
    print tlist
    for key, val in tlist[:8]:
        print key, val
print topTenWordCounter('mailbox.txt')


