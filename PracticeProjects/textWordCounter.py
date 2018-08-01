hfile = open('romeo')
hfile = hfile.read()
rlist = hfile.split()
print rlist

rdic = {}
for i in rlist:
    if i not in rdic:
        rdic[i] = 1
    else:
        rdic[i] = rdic[i] + 1
print rdic
