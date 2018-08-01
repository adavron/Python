engsp = {'one':'uno','two':'dos','three':'tres'}
print engsp['two']
hfile = open('textfile')
hfile = hfile.read()
lists = hfile.split()
print lists
newdic = {}
for i in lists:
    newdic[i] = ''
print newdic


dic = {}
for i in lists:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1
print dic

