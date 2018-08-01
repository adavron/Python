#Linkedin log file parser, read log file and print time stamp and number of logs during tat time stamp
import re
def readLog(logname):

    f = open(logname) #opens file to use
    dic = {} #empty dictionary for latter usage
    for line in f:
        field = re.findall('^[A-Z].*[0-9][0-9]:',line) #this regex searches for date string and returs results to field  var
        tf = tuple(field)#sinceour field result is in list type we need to convert it to tuple so we can use it in dic
        if not tf in dic: #if string is not in dic it addes and couonts it
            dic[tf] = 1
        else:
            dic[tf] += 1
# if we need to sort it we need to convert it to list and sort it as shown below
    tl = []
    for key, val in dic.items():
        tl.append((key, val))

    stl = sorted(tl)
    for key, val in stl:
        print key, val


readLog('/var/log/messages')




