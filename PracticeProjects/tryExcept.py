def countWords(txt):
    try:

        f=open(txt)
        content = f.read()
        #print lines
    except:
        print ("NO such file")

    else:
        words = content.split()
        #print words
        num = len(words)
        print num

files = "log mailbox.txt textfile"
filelist = files.split()
print filelist
for file in filelist:

    countWords(file)
