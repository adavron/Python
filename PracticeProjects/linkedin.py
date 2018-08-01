def link():

    for i in range(100):
        if i%4 ==0 and not i%6 == 0:
            print 'Linked'
        elif i%6 ==0 and not i%4==0:
            print 'In'
        elif i%4==0 and i%6==0:
            print 'LinkedIn'
        else:
            print i

def prints():
    print'huuuulaaaaalaaaaa'

print __name__
if __name__ == "__main__":
    link()
    prints()
