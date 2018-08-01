hfile  = open('install.log')
#lines = hfile.read()
for i in range(5):
    liness = hfile.next().strip()
    print liness

for i in range(10):
    field = hfile.next().split()
    print field
