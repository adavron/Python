import urllib
counts = {}
f = urllib.urlopen('http://data.pr4e.org/romeo.txt')
for line in f:
    words = line.split()
    for word in words:
        print word
        counts[word] = counts.get(word, 0) +1
print counts

string = 'Hi again we want to convert this string to list using split() method'
lists = string.split()
print ''
print string
print lists