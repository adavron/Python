import re
f = open('mailbox.txt')
for line in f:
    line = line.strip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    if len(x) > 0:
        print x