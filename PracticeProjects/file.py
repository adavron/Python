
def lineCounter(file):
    #text = raw_input('Enter text file name: ')
    fhandle = open(file)
    count = 0
    for line in fhandle:
        count = count + 1
    print count

def wordCounter():
    fhandle = open('install.log')
    inp = fhandle.read()
    print (len(inp))


"""
mailbox = open('mailbox.txt')
count = 0
for line in mailbox:
    if line.startswith('From:'):
        line = line.rstrip()
l        count = count + 1
print count

"""
filename = raw_input('Enter file name: ')
try:
    fhandle = open(filename)
except:
    print('File cannot be opened: ',filename)
    exit()
count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        count = count + 1
print count